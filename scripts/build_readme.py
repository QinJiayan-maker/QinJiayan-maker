"""Build a Simon Willison-inspired profile from public project metadata only."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
projects=json.loads((ROOT/'projects.json').read_text(encoding='utf-8'))
FEATURED=['echoagent','volvo','order-agent','gea','disney','lilly','fusion-matrix','visual-tracking']
CASES=[('七阶段研究流程','Research orchestration','volvo'),('语音 / 文字 / 拍照改单','Multimodal order editing','order-agent'),('SSO 与组织同步','SSO and organization sync','gea'),('多模态资产检索','Multimodal asset search','disney'),('人物记忆与来源治理','Memory and provenance','echoagent'),('数字藏品后端','Collectibles backend','fusion-matrix')]
NOTES=[('Agent 在哪里等待确认','Where agents pause for approval','agent-approval'),('区分事实与表达风格','Separating facts from style','memory-and-style'),('检索结果如何带上依据','Retrieval with provenance','retrieval-evidence'),('为什么登录和组织同步分开','Login versus organization sync','identity-and-sync'),('改单工具如何处理单位','Units in order-editing tools','order-units'),('私有源码的公开展示','Presenting private projects','private-projects')]

def build(english=False):
    if english:
        intro="I'm **Jiayan Qin (秦嘉言)**, a full-stack Agent developer and intern at **Tezign**. Currently building [EchoAgent](projects/echoagent.md) and working across agent workflows, RAG, and enterprise integrations. Browse [my projects](PROJECTS.md), read [engineering notes](notes/README.md), or [get in touch](mailto:qjyvictory@163.com). [中文](README.md)."
        headings=['Projects','Case studies','Engineering notes']
        more=['All projects','More case studies','All notes']
    else:
        intro="我是 **秦嘉言 Jiayan Qin**，全栈 Agent 开发者，目前在 **特赞 Tezign** 实习。正在做 [EchoAgent](projects/echoagent.md)，关注 Agent 工作流、RAG 和企业系统集成。可以看看[我的项目](PROJECTS.md)、读读[技术笔记](notes/README.md)，或[通过邮箱联系我](mailto:qjyvictory@163.com)。[English](README.en.md)。"
        headings=['Projects · 项目','Case studies · 实践','Notes · 技术笔记']
        more=['全部项目','更多项目实践','全部技术笔记']
    cols=[]
    rows=[]
    for slug in FEATURED:
        p=next(x for x in projects if x['id']==slug)
        rows.append(f"[{p['name_en' if english else 'name']}](projects/{slug}.md) — {p['short_en' if english else 'short']}")
    cols.append('### '+headings[0]+'\n\n'+'\n\n'.join(rows)+f'\n\n[{more[0]}](PROJECTS.md)')
    rows=[f'[{en if english else zh}](projects/{slug}.md)' for zh,en,slug in CASES]
    cols.append('### '+headings[1]+'\n\n'+'\n\n'.join(rows)+f'\n\n[{more[1]}](PROJECTS.md)')
    rows=[f'[{en if english else zh}](notes/{slug}.md)' for zh,en,slug in NOTES]
    cols.append('### '+headings[2]+'\n\n'+'\n\n'.join(rows)+f'\n\n[{more[2]}](notes/README.md)')
    table='<table width="100%"><tr><td valign="top" width="33%">\n\n'+cols[0]+'\n\n</td><td valign="top" width="34%">\n\n'+cols[1]+'\n\n</td><td valign="top" width="33%">\n\n'+cols[2]+'\n\n</td></tr></table>'
    if english:
        footer='Beijing Jiaotong University · CS undergraduate, 2022–2026. Admitted to a computer science master\'s program at ANU; entry July 2027. Open to internships through July 2027.\n\nPublic pages contain project overviews; source archives and packaged builds are private. [About this profile](MAINTAINING.md).'
    else:
        footer='北京交通大学 · 计算机科学与技术本科（2022–2026）。澳大利亚国立大学 · 计算机科学硕士已获录取，2027 年 7 月入学。可长期实习至 2027 年 7 月。\n\n公开页面展示项目介绍，源码与发行包保存在私有仓库。[主页维护说明](MAINTAINING.md)。'
    return intro+'\n\n'+table+'\n\n'+footer+'\n'

if __name__=='__main__':
    (ROOT/'README.md').write_text(build(),encoding='utf-8')
    (ROOT/'README.en.md').write_text(build(True),encoding='utf-8')
    print('Profile READMEs generated from public metadata.')
