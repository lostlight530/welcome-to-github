"""Profile-driven GitHub document harvester using only the standard library"""
import base64, datetime as dt, difflib, fnmatch, hashlib, json, os, re
import urllib.error, urllib.request
from pathlib import Path

class Harvester:
    def __init__(self, root=None):
        here=Path(__file__).resolve()
        if root is not None and (Path(root)/"inputs").exists():
            self.inputs=Path(root)/"inputs"; self.profile_path=Path(root)/"source_profiles.json"
        else:
            project=Path(root) if root else here.parents[3]
            self.inputs=project/"data"/"inputs"; self.profile_path=self.inputs/"source_profiles.json"
        self.state_path=self.inputs/".harvester_state.json"; self.cache=self.inputs/".raw_cache"
        self.token=os.environ.get("GITHUB_TOKEN",""); self.dry=os.environ.get("HARVESTER_DRY_RUN","0")=="1"
        self.profiles=self._json(self.profile_path,{})
        old=self._json(self.state_path,{})
        self.state=old if "repositories" in old else {"schema_version":2,"legacy_state":old,"repositories":{}}

    @staticmethod
    def _json(path, default):
        try: return json.loads(Path(path).read_text(encoding="utf-8"))
        except (OSError,json.JSONDecodeError): return default

    def _api(self,url):
        headers={"Accept":"application/vnd.github+json","User-Agent":"Nexus-Document-Harvester/2"}
        if self.token: headers["Authorization"]=f"Bearer {self.token}"
        with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))

    @staticmethod
    def _selected(path,patterns,ignored):
        value=path.lower()
        if any(fnmatch.fnmatch(value,p.lower()) for p in ignored): return False
        return value=="readme.md" or any(fnmatch.fnmatch(value,p.lower()) for p in patterns)

    @staticmethod
    def _normalized(text):
        kept=[]
        for line in text.splitlines():
            if re.search(r"(?i)(badge|shields\.io|updated[_ -]?at|last[_ -]?updated)",line): continue
            line=re.sub(r"\s+"," ",line).strip()
            if line: kept.append(line)
        return "\n".join(kept)

    def validate_profiles(self):
        owner=self.profiles.get("owner"); seen=set()
        for p in self.profiles.get("sources",[]):
            key=p.get("repo","").lower()
            if p.get("primary_owner")!=owner: raise ValueError(f"owner mismatch: {key}")
            if owner=="zero" and not p.get("promotion_approved"): raise ValueError(f"unapproved source: {key}")
            if key in seen: raise ValueError(f"duplicate source: {key}")
            seen.add(key)
        return True

    def _source(self,p):
        repo=p["repo"]; meta=self._api(f"https://api.github.com/repos/{repo}")
        tree=self._api(f"https://api.github.com/repos/{repo}/git/trees/{meta['default_branch']}?recursive=1")
        rs=self.state["repositories"].setdefault(repo,{"documents":{}}); changed=[]
        items=[x for x in tree.get("tree",[]) if x.get("type")=="blob" and self._selected(x["path"],p.get("documents",[]),p.get("ignore_patterns",[]))]
        for item in sorted(items,key=lambda x:x["path"]):
            path,sha=item["path"],item["sha"]; previous=rs["documents"].get(path,{})
            if previous.get("sha")==sha: continue
            blob=self._api(f"https://api.github.com/repos/{repo}/git/blobs/{sha}")
            if blob.get("encoding")!="base64": continue
            text=base64.b64decode(blob["content"]).decode("utf-8",errors="replace")
            digest=hashlib.sha256(self._normalized(text).encode()).hexdigest()
            if previous.get("content_hash")==digest:
                rs["documents"][path]={**previous,"sha":sha}; continue
            namespace=repo.lower().replace("/","_").replace("-","_")
            entity=f"doc_{namespace}_{re.sub(r'[^a-z0-9]+','_',path.lower()).strip('_')}_{sha[:12]}"
            target=self.inputs/"current"/p["layer"]/namespace/(path.replace("/","__")+f"__{sha[:12]}.md")
            cache=self.cache/namespace/(path.replace("/","__")+".txt")
            old=cache.read_text(encoding="utf-8") if cache.exists() else ""
            diff="\n".join(difflib.unified_diff(old.splitlines(),text.splitlines(),fromfile="previous",tofile=sha,n=3))
            provenance={"source_repo":repo,"source_path":path,"source_sha":sha,"retrieved_at":dt.datetime.now(dt.timezone.utc).isoformat(),"confidence":1.0,"primary_owner":p["primary_owner"],"entity_id":entity}
            if not self.dry:
                target.parent.mkdir(parents=True,exist_ok=True); cache.parent.mkdir(parents=True,exist_ok=True)
                target.write_text("PROVENANCE: "+json.dumps(provenance,ensure_ascii=False,sort_keys=True)+"\n\n# Source Document\n\n"+text+"\n\n# Document Diff\n\n```diff\n"+diff+"\n```\n",encoding="utf-8")
                cache.write_text(text,encoding="utf-8")
            rs["documents"][path]={"sha":sha,"content_hash":digest,"entity_id":entity,"output":str(target)}; changed.append(str(target))
        rs["last_checked_at"]=dt.datetime.now(dt.timezone.utc).isoformat(); return changed

    def fetch_github_data(self):
        self.validate_profiles(); changed=[]
        for p in self.profiles.get("sources",[]):
            try: changed.extend(self._source(p))
            except (urllib.error.URLError,KeyError,ValueError) as exc: print(f"[Harvester] {p.get('repo')}: {exc}")
        if not self.dry: self.state_path.write_text(json.dumps(self.state,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8")
        return changed
