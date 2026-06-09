import os
import glob

for fp in glob.glob('docs/brain/inputs/*.md'):
    if 'archive' in fp: continue
    with open(fp, 'r') as f:
        content = f.read()

    # Let's completely replace the content to follow the EXACT output format requested
    # The current one has "## 🛡️ 信任评分 (Trust Score)" etc. and we want it to be very strict
    # "1 自动联网拉取目标生态最新动态", "2 将原始数据格式化为对【人类友好】的 Markdown"
    # User format requested:
    # # 🎯 监控目标 (Target)
    # [项目名称自然语言摘要]
    #
    # # 🚀 新版本发布 (New Release)
    # [更新内容的流畅自然语言描述]
    #
    # # 💡 架构洞察 (Architectural Insight)
    # [分析影响并保留友好格式]
    #
    # ---

    import re
    # parse the parts roughly from the existing
    target = re.search(r'# 🎯 监控目标 \(Target\)\s*>(.*)', content)
    target_str = target.group(1).strip() if target else 'Target'

    version = re.search(r'> Version: (.*)', content)
    version_str = version.group(1).strip() if version else ''

    release = re.search(r'# 🚀 新版本发布 \(New Release\).*?> Date:[^\n]*\n(.*?)# 💡', content, re.DOTALL)
    release_str = release.group(1).strip() if release else ''

    insight = re.search(r'# 💡 架构洞察 \(Architectural Insight\)\s*>(.*)', content)
    insight_str = insight.group(1).strip() if insight else 'No insight'

    commits = re.search(r'## 🔨 最近提交 \(Recent Commits\)\s*\*Summary from release notes:\*\n(.*)', content, re.DOTALL)
    commits_str = commits.group(1).strip() if commits else ''

    final_release_str = f"版本 {version_str} 发布。\n\n" + commits_str

    new_content = f"""# 🎯 监控目标 (Target)
{target_str}生态最新动态

# 🚀 新版本发布 (New Release)
{final_release_str}

# 💡 架构洞察 (Architectural Insight)
{insight_str}

---
"""
    with open(fp, 'w') as f:
        f.write(new_content)
