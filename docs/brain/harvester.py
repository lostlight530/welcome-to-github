import urllib.request
import json
import os
import datetime
import logging

# Config: Define your surveillance targets here
TARGETS = {
    "vllm-project/vllm": "tags",
    "huggingface/transformers": "tags",
    "microsoft/markitdown": "tags"
}
STATE_FILE = "docs/brain/inputs/.harvester_state.json"
OUTPUT_DIR = "docs/brain/inputs"

logging.basicConfig(level=logging.INFO, format='[Harvester] %(message)s')

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"repos": {}}

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def fetch_github_release(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url)
    # Generic User-Agent for privacy and stability
    req.add_header('User-Agent', 'Nexus-Cortex-Bot')

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return data
    except Exception as e:
        logging.error(f"Failed to fetch {repo}: {e}")
        return None
    return None

def main():
    state = load_state()
    today_dir = os.path.join(OUTPUT_DIR, datetime.datetime.now().strftime('%Y/%m'))
    os.makedirs(today_dir, exist_ok=True)

    updates_found = False

    for repo, type_ in TARGETS.items():
        logging.info(f"Scanning {repo}...")
        data = fetch_github_release(repo)

        if not data: continue

        tag = data.get('tag_name', 'unknown')
        body = data.get('body', '')
        published_at = data.get('published_at', '')

        repo_state = state["repos"].get(repo, {})
        last_tag = repo_state.get("latest_tag")

        if tag != last_tag:
            logging.info(f"🔥 New Release found: {repo} {tag}")

            # Velocity Tracking logic
            history = repo_state.get("history", [])
            history.append(datetime.datetime.now().isoformat())
            history = history[-5:] # Keep last 5 entries

            safe_name = repo.replace("/", "_")
            filename = f"{safe_name}_{tag}.md"
            filepath = os.path.join(today_dir, filename)

            # Check Velocity
            velocity_alert = ""
            if len(history) >= 2:
                last_time = datetime.datetime.fromisoformat(history[-2])
                if (datetime.datetime.now() - last_time).days < 7:
                    velocity_alert = "\n> 🔥 **HIGH VELOCITY ALERT**: Project is updating rapidly.\n"

            content = f"""# ℹ️ Intel: {repo} {tag}
> Source: GitHub Releases
> Date: {published_at}

{velocity_alert}
## 📝 Summary
{tag}

## 🔍 Changelog (Extract)
{body[:2000]}... (truncated)

## 🤖 Cognitive Analysis Required
- [ ] Is this a major version update? (False)
- [ ] Does it conflict with existing 'tech_stack' nodes?
- [ ] Action: Run `nexus.py add entity ...` or `nexus.py connect ...` to integrate.
"""
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            # Update State
            repo_state["latest_tag"] = tag
            repo_state["last_checked"] = datetime.datetime.now().isoformat()
            repo_state["history"] = history
            state["repos"][repo] = repo_state
            updates_found = True
        else:
            logging.info(f"  - No change ({tag})")

    if updates_found:
        save_state(state)
    else:
        logging.info("Status: Silent. No bandwidth wasted.")

if __name__ == "__main__":
    main()