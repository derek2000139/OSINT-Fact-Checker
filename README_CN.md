# OSINT Fact Checker

<p align="right">
  <a href="README.md"><img src="https://raw.githubusercontent.com/hjnilsson/country-flags/master/png100px/gb.png" width="20" height="15" alt="English"> English</a>
</p>

---

## 简介

OSINT Fact Checker 是一个开源情报事实核查 Skill。给它一句网上看到的传闻，它会自动完成：意图拆解 → 多语言并行搜索 → 信源分级裁决 → 生成结构化核查报告。

**一句话概括：把专业调查记者的工作流，变成一个可以一键调用的 Skill。**

## 核心特性

- **五阶段工作流**：意图识别 → 并行调查 → 浏览器穿透 → 信源裁决 → 报告生成
- **四代理并行**：同时从中/英文信源、学术分析、辟谣方向并行搜索
- **T0-T3 信源分级**：从政府公告到自媒体的四级可信度体系
- **主动反向验证**：自动搜索 scam/debunked/辟谣 等关键词
- **报告自动归档**：每份核查报告以 md 文件持久化保存

## 触发方式

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

## 快速开始

1. **克隆仓库**
```bash
git clone https://github.com/derek2000139/OSINT-Fact-Checker.git
```

2. **在 Trae 中加载 Skill**
   - 打开 Trae → 设置 → Skills
   - 点击 "Add Skill" → 选择 `.trae/skills/osint-fact-checker` 目录
   - 确认 `SKILL.md` 被正确识别

3. **触发核查**：在对话中输入你想核查的传闻

## 项目结构

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
├── README.md                       # 英文版
└── README_CN.md                    # 本文件（中文版）
```

## 真实案例

| 案例 | 输入 | 结论 | 报告 |
|------|------|------|------|
| 水动力汽车 | "日本发明了加水就能跑的汽车" | ❌ 证伪 | [查看报告](reports/water-car_20260522.md) |
| 三星罢工 | "4.8万人罢工，每人34万美金" | 🔄 混合/误导 | [查看报告](reports/samsung-strike_20260522.md) |

## 许可证

[Apache License 2.0](LICENSE)