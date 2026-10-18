"""Real JSON Schema 2020-12 validation; synthetic MCP/A2A gates, no live server."""
from dataclasses import dataclass, replace
from importlib.metadata import version
from jsonschema import Draft202012Validator as V
O,N='2025-11-25','2026-07-28'
S={'obj':{'type':'object','properties':{'v':{'type':'integer'}},'required':['v'],'additionalProperties':False},
'wrap':{'type':'object','properties':{'items':{'type':'array','items':{'type':'integer'}}},'required':['items']},
'arr':{'type':'array','items':{'type':'integer'}},'str':{'type':'string'},
'num':{'type':'number'},'bool':{'type':'boolean'},'null':{'type':'null'}}
for s in S.values():V.check_schema(s)
@dataclass(frozen=True)
class C:
 name:str
 p:str=N
 s:str='obj'
 v:object=None
 error:bool=False
 task:str='A'
 artifact:str='X'
 bound:bool=True
 state:str='COMPLETED'
 receipt:bool=True
 accept:bool=True

def gates(x):
 a=V(S[x.s]).is_valid(x.v)
 b=x.p==N or isinstance(x.v,dict)
 c=a and b and not x.error
 d=c and x.task=='A' and bool(x.artifact) and x.bound
 e=d and x.state=='COMPLETED' and x.receipt and x.accept
 return a,b,c,d,e
b=C('new_obj',v={'v':1})
rows=[(b,'11111'),(replace(b,name='old_obj',p=O),'11111')]
for n,s,v in [('arr','arr',[1,2]),('str','str','ok'),('num','num',7.5),('bool','bool',True),('null','null',None)]:
 rows.extend([(replace(b,name='new_'+n,s=s,v=v),'11111'),(replace(b,name='old_'+n,p=O,s=s,v=v),'10000')])
rows.extend([
(replace(b,name='bad_array',s='arr',v=[1,'x']),'01000'),
(replace(b,name='missing',v={}),'01000'),
(replace(b,name='extra',v={'v':1,'x':2}),'01000'),
(replace(b,name='old_wrap',p=O,s='wrap',v={'items':[1,2]}),'11111'),
(replace(b,name='new_wrap',s='wrap',v={'items':[1,2]}),'11111'),
(replace(b,name='error',error=True),'11000'),
(replace(b,name='wrong_task',task='B'),'11100'),
(replace(b,name='no_artifact',artifact=''),'11100'),
(replace(b,name='unbound',bound=False),'11100'),
(replace(b,name='working',state='WORKING'),'11110'),
(replace(b,name='no_receipt',receipt=False),'11110'),
(replace(b,name='rejected',accept=False),'11110')])
assert version('jsonschema')=='4.26.0'
checks=0
for x,bits in rows:
 for got,want in zip(gates(x),bits):
  assert got==(want=='1'),(x.name,got,want)
  checks+=1
counts=tuple(sum(gates(x)[i] for x,_ in rows) for i in range(5))
for got,want in zip(counts,(21,19,15,12,9)):
 assert got==want,(counts,want)
 checks+=1
for yes in [counts[0]>counts[2]>counts[4],gates(rows[3][0])==(True,False,False,False,False),
            gates(rows[15][0])[-1],gates(rows[16][0])[-1]]:
 assert yes
 checks+=1
print(f'cases={len(rows)} assertions={checks} schema_valid={counts[0]} wire_shape={counts[1]} usable={counts[2]} task_bound={counts[3]} accepted={counts[4]}')
