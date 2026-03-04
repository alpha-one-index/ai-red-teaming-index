# AI Red Teaming Index

> A comprehensive open-source reference for AI red teaming tools, frameworks, benchmarks, datasets, and vulnerability leaderboards.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Updated](https://img.shields.io/badge/Data-Auto%20Updated%20Weekly-blue.svg)](#)
[![Tools](https://img.shields.io/badge/Tools-50%2B-green.svg)](#red-team-tools)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](#changelog)
[![Validation](https://img.shields.io/badge/Validation-Self%20Auditing-brightgreen.svg)](#methodology)
[![Croissant](https://img.shields.io/badge/Croissant-ML%20Metadata-orange.svg)](croissant.json)
[![Provenance](https://img.shields.io/badge/Provenance-Documented-purple.svg)](provenance.md)
[![HuggingFace Dataset](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace%20Dataset-yellow.svg)](#)
[![Kaggle Dataset](https://img.shields.io/badge/%F0%9F%8F%86-Kaggle%20Dataset-blue.svg)](#)

Maintained by [Alpha One Index](https://github.com/alpha-one-index) — An independent AI security research initiative providing verified, structured red teaming data for engineers, researchers, and security teams.

## Live Demos & Data Access

| Platform | Link | Description |
|----------|------|-------------|
| GitHub Pages | [alpha-one-index.github.io/ai-red-teaming-index](https://alpha-one-index.github.io/ai-red-teaming-index) | Interactive dashboard with filtering and sorting |
| HuggingFace | [datasets/alpha-one-index/ai-red-teaming-index](#) | ML-ready dataset with Croissant metadata |
| Kaggle | [datasets/alphaoneindex/ai-red-teaming-index](#) | Kaggle dataset with notebooks |

## Table of Contents

- [Overview](#overview)
- [Red Team Tools & Frameworks](#red-team-tools--frameworks)
- [Vulnerability Leaderboards](#vulnerability-leaderboards)
- [Benchmarks & Datasets](#benchmarks--datasets)
- [Attack Vectors & Techniques](#attack-vectors--techniques)
- [Quick Start](#quick-start)
- [Data Format](#data-format)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## Overview

The **AI Red Teaming Index** is a structured, data-first resource tracking the rapidly evolving landscape of AI/LLM security testing. As regulatory frameworks (NIST AI RMF, EU AI Act) increasingly mandate red teaming, this index provides the authoritative open reference for:

- **50+ Red Team Tools & Frameworks** — PyRIT, Giskard, DeepTeam, ART, Counterfit, and more
- **Model Vulnerability Leaderboards** — Jailbreak success rates, PII leakage, bias scores across GPT-4o, Claude, Gemini, Llama, Mistral
- **Benchmarks & Datasets** — RedBench (29K samples), AIRTBench, HarmBench, AdvBench, TruthfulQA
- **Attack Vector Taxonomy** — Prompt injection, model inversion, membership inference, data poisoning, adversarial examples
- **8 Risk Categories** — Jailbreak, PII leakage, bias/fairness, toxicity, hallucination, IP theft, misuse, system prompt extraction
- **19+ Application Domains** — Healthcare, finance, legal, education, code generation, content moderation

## Red Team Tools & Frameworks

| Tool | Organization | Stars | Language | Probes | License | Link |
|------|-------------|-------|----------|--------|---------|------|
| PyRIT | Microsoft | 2.8K | Python | 40+ | MIT | [GitHub](https://github.com/Azure/PyRIT) |
| Giskard | Giskard AI | 4.2K | Python | 50+ | Apache 2.0 | [GitHub](https://github.com/Giskard-AI/giskard) |
| DeepTeam | Confident AI | 1.5K | Python | 40+ | Apache 2.0 | [GitHub](https://github.com/confident-ai/deepteam) |
| ART | IBM/Trusted AI | 4.8K | Python | 30+ | MIT | [GitHub](https://github.com/Trusted-AI/adversarial-robustness-toolbox) |
| Counterfit | Microsoft | 800 | Python | 20+ | MIT | [GitHub](https://github.com/Azure/counterfit) |
| TextAttack | QData | 2.9K | Python | 25+ | MIT | [GitHub](https://github.com/QData/TextAttack) |
| Guardrails AI | Guardrails | 4.0K | Python | 35+ | Apache 2.0 | [GitHub](https://github.com/guardrails-ai/guardrails) |
| NeMo Guardrails | NVIDIA | 4.5K | Python | 30+ | Apache 2.0 | [GitHub](https://github.com/NVIDIA/NeMo-Guardrails) |
| LLM Guard | Protect AI | 1.2K | Python | 28+ | MIT | [GitHub](https://github.com/protectai/llm-guard) |
| Rebuff | Protect AI | 800 | Python | 15+ | Apache 2.0 | [GitHub](https://github.com/protectai/rebuff) |

> See [data/red-team-tools.json](data/red-team-tools.json) for the complete dataset with 50+ tools.

## Vulnerability Leaderboards

### Model Safety Scores (Lower = More Vulnerable)

| Model | Jailbreak Resist % | PII Protection % | Bias Score | Toxicity Filter % | Overall Safety |
|-------|-------------------|-------------------|------------|-------------------|----------------|
| Claude 3.5 Sonnet | 94.2 | 96.1 | 0.12 | 97.3 | 94.5 |
| GPT-4o | 91.8 | 93.4 | 0.15 | 95.1 | 92.2 |
| Gemini 1.5 Pro | 89.5 | 91.2 | 0.18 | 93.8 | 90.1 |
| Llama 3.1 405B | 85.3 | 87.6 | 0.22 | 89.4 | 86.2 |
| Mistral Large | 83.7 | 85.1 | 0.25 | 87.2 | 84.5 |
| Command R+ | 82.1 | 84.3 | 0.27 | 86.5 | 83.1 |

> See [data/vulns-leaderboard.csv](data/vulns-leaderboard.csv) for the complete leaderboard.

## Benchmarks & Datasets

| Benchmark | Samples | Categories | Focus | Source |
|-----------|---------|------------|-------|--------|
| RedBench | 29,000 | 8 | Comprehensive red teaming | [Paper](#) |
| AIRTBench | 5,200 | 6 | CTF-style challenges | [Paper](#) |
| HarmBench | 3,100 | 7 | Harmful content generation | [GitHub](https://github.com/centerforaisafety/HarmBench) |
| AdvBench | 1,500 | 5 | Adversarial suffixes | [GitHub](#) |
| TruthfulQA | 817 | 38 | Hallucination testing | [GitHub](https://github.com/sylinrl/TruthfulQA) |
| WMDP | 4,000 | 3 | Weapons/malware/cyber | [Paper](#) |
| SafetyBench | 11,435 | 7 | Chinese & English safety | [GitHub](#) |
| XSTest | 450 | 10 | Exaggerated safety refusals | [GitHub](#) |

> See [data/benchmarks.json](data/benchmarks.json) for the complete dataset.

## Attack Vectors & Techniques

| Category | Technique | Risk Level | Mitigation |
|----------|-----------|------------|------------|
| Prompt Injection | Direct/Indirect injection | Critical | Input validation, guardrails |
| Jailbreaking | DAN, role-play, encoding tricks | Critical | Constitutional AI, RLHF |
| Model Inversion | Gradient-based reconstruction | High | Differential privacy |
| Membership Inference | Training data detection | High | DP-SGD, regularization |
| Data Poisoning | Backdoor/trigger insertion | Critical | Data sanitization |
| Adversarial Examples | Perturbation attacks | High | Adversarial training |
| System Prompt Extraction | Prompt leaking techniques | Medium | Prompt isolation |
| PII Leakage | Training data memorization | High | Deduplication, scrubbing |

> See [specs/attack-vectors.md](specs/attack-vectors.md) for detailed analysis.

## Quick Start

### Python
```python
import pandas as pd

# Load vulnerability leaderboard
leaderboard = pd.read_csv('https://raw.githubusercontent.com/alpha-one-index/ai-red-teaming-index/main/data/vulns-leaderboard.csv')
print(leaderboard.head())

# Load tools index
import json, urllib.request
url = 'https://raw.githubusercontent.com/alpha-one-index/ai-red-teaming-index/main/data/red-team-tools.json'
tools = json.loads(urllib.request.urlopen(url).read())
print(f"Total tools indexed: {len(tools)}")
```

### HuggingFace
```python
from datasets import load_dataset
ds = load_dataset("alpha-one-index/ai-red-teaming-index")
print(ds)
```

## Data Format

All data is available in multiple formats:
- **JSON** — Structured tool/benchmark metadata
- **CSV** — Tabular leaderboard and comparison data
- **Parquet** — Optimized for ML pipelines (via HuggingFace)

## Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for our complete data collection, validation, and update methodology.

Key principles:
1. **Primary sources only** — Official documentation, peer-reviewed papers, vendor disclosures
2. **4-tier validation** — Schema validation, cross-reference checks, temporal consistency, anomaly detection
3. **Weekly updates** — Automated pipelines refresh leaderboard and tool data
4. **Provenance tracking** — Full data lineage documented in [provenance.md](provenance.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome:
- New tool submissions via PR
- Benchmark result updates
- Vulnerability disclosure references
- Attack technique documentation

## Citation

If you use this data in your research, please cite:

```bibtex
@misc{alphaoneindex2026airedteaming,
  title={AI Red Teaming Index: Comprehensive Tools, Benchmarks, and Vulnerability Data},
  author={Alpha One Index},
  year={2026},
  publisher={GitHub},
  url={https://github.com/alpha-one-index/ai-red-teaming-index}
}
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

**Disclaimer**: This index is for defensive security research purposes only. All vulnerability data is sourced from public benchmarks and responsible disclosure programs. Do not use this information for malicious purposes.
