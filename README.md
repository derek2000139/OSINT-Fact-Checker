# OSINT Fact Checker

<p align="right">
  <a href="README_CN.md"><img src="https://raw.githubusercontent.com/hjnilsson/country-flags/master/png100px/cn.png" width="20" height="15" alt="中文"> 中文</a>
</p>

---

## Introduction

OSINT Fact Checker is an open-source intelligence fact-checking Skill for [Trae](https://www.trae.ai). Feed it a rumor you saw online, and it automatically completes: intent decomposition → multi-language parallel search → source grading → structured fact-checking report generation.

**In one sentence: Turn a professional investigator's workflow into a one-click callable Skill.**

## Key Features

- **Five-phase workflow**: Intent recognition → Parallel investigation → Browser penetration → Source adjudication → Report generation
- **Four-agent parallelism**: Simultaneous search from Chinese/English sources, academic analysis, and debunking directions
- **T0-T3 source grading**: Four-level credibility system from government announcements to self-media
- **Proactive reverse verification**: Automatically search for scam/debunked/rumor keywords
- **Report auto-archiving**: Each report is saved as an md file for future reference

## Trigger Examples

```
I heard Japan invented a water-powered car, is it true?
Samsung 48k employees on strike, each gets $340k premium, is it reliable?
Tencent Docs layoffs, what's the real situation?
Is this therapy effective?
What do people think about this policy?
What's the timeline of this event?
How do foreign media report this?
```

Or call directly:

```
Use Skill: OSINT Fact Checker [content you want to verify]
```

## Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/derek2000139/OSINT-Fact-Checker.git
```

2. **Load in Trae**
   - Open Trae → Settings → Skills
   - Click "Add Skill" → Select `.trae/skills/osint-fact-checker` directory
   - Confirm `SKILL.md` is correctly recognized

3. **Start verifying**: Type a rumor you want to check into the conversation

## Project Structure

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
├── README.md                       # This file (English)
└── README_CN.md                    # Chinese version
```

## Real-World Results

| Case | Input | Verdict | Report |
|------|-------|---------|--------|
| Water-powered car | "Japan invented a car that runs on water" | ❌ Debunked | [water-car report](reports/water-car_20260522.md) |
| Samsung strike | "48k workers striking, $340k each" | 🔄 Misleading | [samsung-strike report](reports/samsung-strike_20260522.md) |

## License

[Apache License 2.0](LICENSE)