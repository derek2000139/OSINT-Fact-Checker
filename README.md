# OSINT Fact Checker

[English](#english) | [中文](#中文)

---

<a name="中文"></a>
## 中文

### 简介

OSINT Fact Checker 是一个开源情报事实核查 Skill。给它一句网上看到的传闻，它会自动完成：意图拆解 → 多语言并行搜索 → 信源分级裁决 → 生成结构化核查报告。

**一句话概括：把专业调查记者的工作流，变成一个可以一键调用的 Skill。**

### 核心特性

- **五阶段工作流**：意图识别 → 并行调查 → 浏览器穿透 → 信源裁决 → 报告生成
- **四代理并行**：同时从中/英文信源、学术分析、辟谣方向并行搜索
- **T0-T3 信源分级**：从政府公告到自媒体的四级可信度体系
- **主动反向验证**：自动搜索 scam/debunked/辟谣 等关键词
- **报告自动归档**：每份核查报告以 md 文件持久化保存

### 触发方式

用自然语言即可触发：

```
"网上说日本发明了水动力汽车，是真的吗？"
"三星4.8万员工罢工，每人发34万美金，可靠吗？"
"腾讯文档裁员，真实情况是什么？"
"这个疗法有用吗？"
"大家怎么看这个政策？"
"这件事的时间线是什么？"
"外媒怎么报道的？"
```

或直接调用：

```
Use Skill: OSINT Fact Checker 你想核查的内容
```

### 项目结构

```
osint-fact-checker/
├── .trae/skills/osint-fact-checker/
│   ├── SKILL.md                    # 核心配置：五阶段工作流定义
│   ├── examples/
│   │   ├── input.md                # 示例输入
│   │   └── output.md               # 示例输出格式
│   ├── scripts/
│   │   ├── async_fetch.py          # 并发网页抓取
│   │   └── wayback_lookup.py       # Wayback Machine 存档查询
│   └── resources/
│       └── source-grading.md       # T0-T3 信源评级标准
├── reports/                        # 自动生成的核查报告
│   ├── water-car_20260522.md
│   └── samsung-strike_20260522.md
├── LICENSE                         # Apache License 2.0
└── README.md                       # 本文件
```

### 在 Trae 中使用

1. 克隆仓库
```bash
git clone https://github.com/derek2000139/OSINT-Fact-Checker.git
```

2. 在 Trae 中加载 Skill：
   - 打开 Trae → 设置 → Skills
   - 点击 "Add Skill" → 选择 `.trae/skills/osint-fact-checker` 目录
   - 确认 `SKILL.md` 被正确识别

3. 触发核查：在对话中输入你想核查的传闻

### 使用场景

- **日常辟谣**：查证朋友圈/群聊里的"震惊体"新闻
- **投资核实**：核实股票论坛里的"内幕消息"
- **求职背调**：核实公司裁员/扩招传闻
- **健康核实**：核实家人转发的养生偏方
- **学术研究**：快速文献调研
- **跨境信息**：突破信息茧房，获取多视角

### 许可证

[Apache License 2.0](LICENSE)

---

<a name="english"></a>
## English

### Introduction

OSINT Fact Checker is an open-source intelligence fact-checking Skill. Feed it a rumor you saw online, and it automatically completes: intent decomposition → multi-language parallel search → source grading → structured fact-checking report generation.

**In one sentence: Turn a professional investigative journalist's workflow into a one-click callable Skill.**

### Key Features

- **Five-phase workflow**: Intent recognition → Parallel investigation → Browser penetration → Source adjudication → Report generation
- **Four-agent parallelism**: Simultaneous search from Chinese/English sources, academic analysis, and debunking directions
- **T0-T3 source grading**: Four-level credibility system from government announcements to self-media
- **Proactive reverse verification**: Automatically search for scam/debunked/辟谣 keywords
- **Automatic report archiving**: Each verification report is persistently saved as an md file

### Trigger Methods

Trigger with natural language:

```
"I heard Japan invented a water-powered car, is it true?"
"Samsung 48k employees on strike, $340k each, is it reliable?"
"Tencent Docs layoffs, what's the real situation?"
"Is this therapy useful?"
"What do people think about this policy?"
"What's the timeline of this event?"
"How do foreign media report it?"
```

Or call directly:

```
Use Skill: OSINT Fact Checker [content you want to verify]
```

### Project Structure

```
osint-fact-checker/
├── .trae/skills/osint-fact-checker/
│   ├── SKILL.md                    # Core config: five-phase workflow
│   ├── examples/
│   │   ├── input.md                # Example input
│   │   └── output.md               # Example output format
│   ├── scripts/
│   │   ├── async_fetch.py          # Concurrent web scraping
│   │   └── wayback_lookup.py       # Wayback Machine archive lookup
│   └── resources/
│       └── source-grading.md       # T0-T3 source grading standard
├── reports/                        # Auto-generated verification reports
│   ├── water-car_20260522.md
│   └── samsung-strike_20260522.md
├── LICENSE                         # Apache License 2.0
└── README.md                       # This file
```

### Usage in Trae

1. Clone the repository
```bash
git clone https://github.com/derek2000139/OSINT-Fact-Checker.git
```

2. Load Skill in Trae:
   - Open Trae → Settings → Skills
   - Click "Add Skill" → Select `.trae/skills/osint-fact-checker` directory
   - Confirm `SKILL.md` is correctly recognized

3. Trigger verification: Enter the rumor you want to verify in the conversation

### Use Cases

- **Daily debunking**: Verify "shocking" news from social media
- **Investment verification**: Verify "insider information" from stock forums
- **Job background check**: Verify company layoff/expansion rumors
- **Health verification**: Verify health tips forwarded by family
- **Academic research**: Quick literature research
- **Cross-border information**: Break information cocoons, get multiple perspectives

### License

[Apache License 2.0](LICENSE)
