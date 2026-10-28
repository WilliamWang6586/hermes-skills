# 王子涵的 Hermes 技能包合集

> 一句话：把这份文件（或下面的地址）丢给你的 Hermes Agent，它能自己装好这些技能。

## 怎么装（任选一种，推荐第一种）

**A. 让 agent 自己装（最快）**

把 `skills-bundle.md` 和 `install_bundle.py` 一起发给你的 Hermes Agent，说一句：

```
读 skills-bundle.md 末尾的 SKILLBUNDLE-B64，用 install_bundle.py 解到我的 skills 目录，然后列出装好的清单。
```

或自己跑：

```powershell
py install_bundle.py skills-bundle.md            # 全部
py install_bundle.py skills-bundle.md humanizer-zh agent-reach   # 只装某几个
```

**B. 单个技能 zip**：把 `skills-xxx.zip` 发给 agent 说「解压到 skills 目录」，或解压到系统 skills 目录下的 `xxx\`。

**C. 手动**：解压到 `%LOCALAPPDATA%\Hermes Agent CN Desktop\data\hermes-home\skills\<技能名>\`，重启会话。


> 技能的本质就是一个目录：`SKILL.md`（frontmatter 的 name/description 决定何时触发）+ 可选 `references/ scripts/ templates/`。


## 清单（43 个技能，合集 zip 约 11.5 MB）

| # | 技能 | 干什么 | 体积 | 备注 |
|---|---|---|---|---|
| 1 | `memory-system` | Use when setting up or improving an agent memory workflow for OpenClaw, Codex, o | 21KB | 公开 · [来源](https://github.com/cjke84/agent-memory-system-guide) |
| 2 | `agent-reach` | 零配置联网调研：Jina/YouTube/V2EX/RSS/B站/GitHub 免 key 抓取 | 5KB | 公开 · [来源](https://github.com/Panniantong/Agent-Reach) |
| 3 | `ai-text-humanizer` | 把 AI 味文本改写成自然人类口吻，附检测报告 | 11KB | 公开 |
| 4 | `autocad-drawing` | 用 COM 驱动本机 AutoCAD 参数化绘图、读图、落盘校验 | 10KB | 公开 |
| 5 | `browser-testing-with-devtools` | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging a | 14KB | 公开 |
| 6 | `cad-automation` | CAD 二次开发知识库：pyautocad/C#/LISP 自动化绘图 | 32KB | 公开 |
| 7 | `cad-designer` | CAD 制图规范（国标）+参数化设计指导 | 22KB | 公开 |
| 8 | `content-multi-platform` | 一篇内容改写为九大平台适配版本（小红书/公众号/知乎/抖音…） | 25KB | 公开 |
| 9 | `hainan-university-baixiaosheng` | 海南大学知识库：校区、选课、专业、宿舍等 | 6KB | 公开 |
| 10 | `hallmark` | 反 AI-slop 网页设计规范：新建页面与审计 | 66KB | 公开 |
| 11 | `humanizer-zh` | 中文去 AI 味写作（维基百科 AI 写作特征清单） | 18KB | 公开 |
| 12 | `incremental-implementation` | 小步增量实现，每次改动可验证 | 9KB | 公开 |
| 13 | `planning-and-task-breakdown` | 把需求拆成有顺序、可执行的任务 | 7KB | 公开 |
| 14 | `ppt-master` | 生成原生可编辑 PPTX（模板+渲染+校验，89MB 含资源） | 10KB | 公开 |
| 15 | `reverse-engineer-anything` | 逆向分析原生/托管/Electron/移动端程序 | 23KB | 公开 |
| 16 | `scientific-figure-making` | 论文级 matplotlib 配图规范 | 2KB | 公开 |
| 17 | `spec-driven-development` | 先写规格再写代码 | 8KB | 公开 |
| 18 | `tech-daily-report` | 生成「科技观察报」HTML 报纸（米色纸张+衬线字体+深度内容+全中文+可点击链接），覆盖 AI·半导体·智能汽车·摄影器材·机器人·量子·政策 七大板块。当用 | 26KB | 私有 |
| 19 | `wayfinder` | 规划超出单次会话的大段工作 | 12KB | 公开 |
| 20 | `web-access` | 统一联网通道：搜索、抓站、登录后操作 | 18KB | 公开 |
| 21 | `codex` | 把编码任务委派给 OpenAI Codex CLI | 6KB | 公开 |
| 22 | `hermes-agent` | Hermes Agent 自身的配置/扩展/贡献指南 | 51KB | 公开 |
| 23 | `claude-design` | 单页 HTML 设计（落地页/演示/原型） | 25KB | 公开 |
| 24 | `interactive-map-design` | 交互地图设计模式 | 8KB | 公开 |
| 25 | `windows-maintenance` | Windows 清理、大目录归档、计划任务修复 | 32KB | 公开 |
| 26 | `windows-wsl2-script-exec` | Windows+WSL2 上写/跑脚本的路由与坑 | 38KB | 公开 |
| 27 | `minecraft-forge-modpack-debug` | Forge 整合包崩溃排查（MC 启动失败） | 7KB | 私有 |
| 28 | `hermes-cn-desktop-ops` | Hermes 桌面端运维总入口：升级/配置/网关/语音视觉 | 27KB | 私有 |
| 29 | `download-and-verify` | 找可靠下载源 + 四重安全校验（魔数/SHA256/Defender/行为） | 11KB | 公开 |
| 30 | `memory-library-ops` | Hermes 记忆库外置与压缩运维 | 25KB | 私有 |
| 31 | `document-generation` | 生成 Word/PDF/HTML 文档（中文排版、Edge 转 PDF） | 19KB | 公开 |
| 32 | `officecli` | Office 文档创建/分析/校对/修改 | 4KB | 公开 · [来源](https://officecli.ai) |
| 33 | `ppt-master-ops` | ppt-master 实战运维：路由、门禁、坑（中文汇报/竞选/答辩） | 34KB | 公开 |
| 34 | `china-university-web-research` | 高校官网抓取与批量下载（中文 URL、编码坑） | 17KB | 公开 |
| 35 | `china-web-research` | 中国大陆网络环境下的检索与抓取实战（B站/Bing/反爬） | 18KB | 公开 |
| 36 | `jlu-knowledge-ops` | 吉林大学知识库运维+发布全流程 | 53KB | 校内 |
| 37 | `c-native-cli-programs` | 用 C/C++ 写单文件 CLI 程序并自动化测试 | 10KB | 校内 |
| 38 | `plan` | 写可执行的 markdown 计划 | 9KB | 公开 |
| 39 | `python-beginner-teaching` | 零基础 Python 教学：周任务包、review、补缺口 | 31KB | 校内 |
| 40 | `skill-collection-install` | 从 GitHub 技能合集批量安装到 Hermes（含 .ps1 编码坑） | 24KB | 公开 |
| 41 | `test-driven-development` | TDD：红-绿-重构，测试先写 | 10KB | 公开 |
| 42 | `vscode-agent-pairing` | 把代码写进用户正开着的 VSCode | 5KB | 公开 |
| 43 | `xiaping` | 虾评技能交易平台 API 对接（发布/下载/评测） | 35KB | 公开 · [来源](https://xiaping.coze.com) |

## 说明

- 「校内」标记的技能里含吉林大学内部资料/个人学习路径，自己人用就行，别公开传播。
- 部分技能依赖本机环境（AutoCAD、Windows、WSL2）；换机器也能装，但脚本要自己适配路径。

---

## 下载地址

| 内容 | 地址 |
|---|---|
| 合集 zip（43 个技能） | https://github.com/WilliamWang6586/hermes-skills/releases/download/v1.0.0/skills-bundle.zip |
| ppt-master 大件 | https://github.com/WilliamWang6586/hermes-skills/releases/download/v1.0.0/skills-ppt-master.zip |
| 单技能 zip 列表 | https://github.com/WilliamWang6586/hermes-skills/tree/main/skills |
| 合集说明 md | https://github.com/WilliamWang6586/hermes-skills/blob/main/skills-bundle.md |

装法：

```powershell
py install_bundle.py skills-bundle.md              # 全装
py install_bundle.py skills-bundle.md humanizer-zh # 只装某个
```
