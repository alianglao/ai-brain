from pathlib import Path
import argparse, datetime, hashlib, json, re, shutil, sys

ROOT=Path(__file__).resolve().parents[1]
CFG=ROOT/'98-AI-Context/research-config.json'
def load(): return json.loads(CFG.read_text(encoding='utf-8'))
def frontmatter(text):
 if text.startswith('---\n') and '\n---\n' in text[4:]:
  end=text.index('\n---\n',4); return text[4:end],text[end+5:]
 return '',text
def clean_one(src):
 raw=src.read_bytes(); digest=hashlib.sha256(raw).hexdigest(); text=raw.decode('utf-8-sig',errors='replace')
 for base in [ROOT/'04-Research',ROOT/'00-Inbox/Cleaned']:
  for old in base.rglob('*.md'):
   if f'original_sha256: "{digest}"' in old.read_text(encoding='utf-8-sig',errors='replace'):
    return old
 cfg=load(); low=' '+text.lower()+' '; scores={d:sum(low.count(k.lower()) for k in ks) for d,ks in cfg['keywords'].items()}
 best=max(scores,key=scores.get); confident=scores[best]>0 and list(scores.values()).count(scores[best])==1
 target=ROOT/'04-Research'/best/src.name if confident else ROOT/'00-Inbox/Cleaned'/src.name
 if target.exists(): target=target.with_name(target.stem+'-'+digest[:8]+target.suffix)
 original=ROOT/'99-Archive/Originals'/digest[:2]/(digest+'.md'); original.parent.mkdir(parents=True,exist_ok=True)
 if not original.exists(): shutil.copy2(src,original)
 fm,body=frontmatter(text); title=next((m.group(1).strip() for line in body.splitlines() if (m:=re.match(r'^#\s+(.+)',line))),src.stem)
 url=next(iter(re.findall(r'https?://[^\s)>]+',text)),'')
 tags=[]; hubs=[]
 for group,terms in cfg['topic_groups'].items():
  for term in terms:
   if term.lower() in low: tags.append('topic/'+re.sub(r'\s+','-',term.lower())); hubs.append(term)
 meta=['---',f'title: "{title.replace(chr(34), chr(39))}"',f'source: "{url}"',f'captured: "{datetime.date.today()}"',f'primary_category: "{best if confident else "unclassified"}"','tags: ['+', '.join(tags)+']',f'original_sha256: "{digest}"','status: cleaned','---','']
 relation='\n\n## Knowledge Graph\n'+('\n'.join(f'- [[07-Topics/{h} Hub]]' for h in hubs) if hubs else '- 待建立主题关系')+'\n'
 target.parent.mkdir(parents=True,exist_ok=True); target.write_text('\n'.join(meta)+body.rstrip()+relation,encoding='utf-8')
 return target
def clean():
 files=[p for p in (ROOT/'00-Inbox/Downloaded').glob('*.md') if p.name!='Downloaded.md']; out=[]
 for f in files: out.append(str(clean_one(f).relative_to(ROOT)))
 print(json.dumps({'processed':len(out),'outputs':out},ensure_ascii=False))
def graph():
 cfg=load(); files=[p for p in (ROOT/'04-Research').rglob('*.md') if not p.name.endswith(' Index.md')]; counts={}
 for f in files:
  text=f.read_text(encoding='utf-8-sig',errors='replace')
  for terms in cfg['topic_groups'].values():
   for term in terms:
    if term.lower() in text.lower(): counts.setdefault(term,[]).append(f)
 lines=['# Topic Index','','基于 04-Research 的实际扫描结果生成。','','## 已达到建 Hub 阈值的主题']
 eligible={k:v for k,v in counts.items() if len(v)>=cfg['minimum_topic_documents']}
 if not eligible: lines+=['','当前没有主题达到阈值（至少 2 篇研究笔记），因此未虚构高频 Topic Hub。']
 for topic,notes in sorted(eligible.items()):
  hub=ROOT/'07-Topics'/(topic+' Hub.md'); body='# '+topic+' Hub\n\n## 研究笔记\n'+''.join('\n- [['+str(n.relative_to(ROOT)).replace('\\','/')[:-3]+']]' for n in notes)+'\n\n## 待研究问题\n'
  hub.write_text(body,encoding='utf-8'); lines.append(f'- [[07-Topics/{topic} Hub]]（{len(notes)} 篇）')
 lines+=['','## 领域入口']+[f'- [[04-Research/{d}/{d} Index|{d}]]：{len([p for p in (ROOT/"04-Research"/d).rglob("*.md") if not p.name.endswith(" Index.md")])} 篇' for d in cfg['domains']]
 (ROOT/'07-Topics/Topic Index.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(json.dumps({'research_notes':len(files),'eligible_topics':{k:len(v) for k,v in eligible.items()}},ensure_ascii=False))
def audit():
 files=[p for p in ROOT.rglob('*.md') if '.git' not in p.parts]; hashes={}; broken=[]; links=set(); bad=[]
 for p in files:
  text=p.read_text(encoding='utf-8-sig',errors='replace'); h=hashlib.sha256(text.encode()).hexdigest(); hashes.setdefault(h,[]).append(p)
  if re.search(r'[<>:"|?*]',p.name): bad.append(p)
  links.update(re.findall(r'\[\[([^]|#]+)',text))
 stems={p.stem for p in files}; broken=sorted(x for x in links if Path(x).name not in stems and not (ROOT/(x+'.md')).exists())
 empty=[p for p in ROOT.rglob('*') if p.is_dir() and '.git' not in p.parts and not any(p.iterdir())]
 linked={Path(x).name for x in links}; orphan=[p for p in files if p.stem not in linked and p.name not in {'Home.md','AGENTS.md','CLAUDE.md'}]
 dup=[v for v in hashes.values() if len(v)>1]
 report=['# Knowledge Base Audit',f'\n生成时间：{datetime.datetime.now().isoformat(timespec="minutes")}',f'\n- Markdown：{len(files)}','- 重复组：'+str(len(dup)),'- 异常文件名：'+str(len(bad)),'- 空目录：'+str(len(empty)),'- 孤立笔记：'+str(len(orphan)),'- 断链：'+str(len(broken))]
 for title,items in [('重复内容',[', '.join(str(p.relative_to(ROOT)) for p in x) for x in dup]),('异常文件名',[str(x.relative_to(ROOT)) for x in bad]),('空目录',[str(x.relative_to(ROOT)) for x in empty]),('孤立文件',[str(x.relative_to(ROOT)) for x in orphan]),('断链',broken)]: report+=['','## '+title]+(['- '+x for x in items] or ['- 无'])
 out=ROOT/'98-AI-Context/Knowledge Base Audit Report.md'; out.write_text('\n'.join(report)+'\n',encoding='utf-8'); print(str(out))
def project(name):
 p=ROOT/'06-Projects'/name/'Project-Status.md'; p.parent.mkdir(parents=True,exist_ok=True)
 if not p.exists(): p.write_text('# '+name+' — Project Status\n\n## 当前状态\n规划中\n\n## 已完成事项\n\n## 待办事项\n\n## 下一步\n\n## 风险\n\n## 决策\n',encoding='utf-8')
 print(p)
if __name__=='__main__':
 ap=argparse.ArgumentParser(); ap.add_argument('command',choices=['clean','graph','audit','project']); ap.add_argument('name',nargs='?'); a=ap.parse_args()
 {'clean':clean,'graph':graph,'audit':audit,'project':lambda:project(a.name or 'New Project')}[a.command]()
