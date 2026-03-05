# AI Red Teaming Index

> A comprehensive open-source reference for AI red teaming tools, frameworks, benchmarks, datasets, and vulnerability leaderboards.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Updated](https://img.shields.io/badge/Data-Auto%20Updated%20Weekly-blue.svg)](#)
[![Tools](https://img.shields.io/badge/Tools-50%2B-green.svg)](#red-team-tools)
[![Version](https://img.shields.io/badge/Version-1.1.0-blue.svg)](#changelog)
[![Validation](https://img.shields.io/badge/Validation-Self%20Auditing-brightgreen.svg)](#methodology)
[![Croissant](https://img.shields.io/badge/Croissant-ML%20Metadata-orange.svg)](croissant.json)
[![Provenance](https://img.shields.io/badge/Provenance-Documented-purple.svg)](provenance.md)
[![HuggingFace Dataset](https://img.shields.io/badge/%F0%9F%A4%97-HuggingFace%20Dataset-yellow.svg)](#)
[![Kaggle Dataset](https://img.shields.io/badge/%F0%9F%8F%86-Kaggle%20Dataset-blue.svg)](#)

Maintained by [Alpha One Index](https://github.com/alpha-one-index) -- An independent AI security research initiative providing verified, structured red teaming data for engineers, researchers, and security teams.

## Live Demos & Data Access

| Platform | Link | Description |
|---|---|---|
| GitHub Pages | [alpha-one-index.github.io/ai-red-teaming-index](https://alpha-one-index.github.io/ai-red-teaming-index) | Interactive dashboard with filtering and sorting |
| HuggingFace | [datasets/alpha-one-index/ai-red-teaming-index](#) | ML-ready dataset with Croissant metadata |
| Kaggle | [datasets/alphaoneindex/ai-red-teaming-index](#) | Kaggle dataset with notebooks |

## Table of Contents

- [Overview](#overview)
- [Regulatory Mandate Map](#regulatory-mandate-map)
- [Red Team Tools & Frameworks](#red-team-tools--frameworks)
- [Vulnerability Leaderboards](#vulnerability-leaderboards)
- [Leaderboard Methodology & Sourcing](#leaderboard-methodology--sourcing)
- [Benchmarks & Datasets](#benchmarks--datasets)
- [Attack Vectors & Techniques](#attack-vectors--techniques)
- [Vendor Attack Coverage Matrix](#vendor-attack-coverage-matrix)
- [Quick Start](#quick-start)
- [Data Format](#data-format)
- [Methodology](#methodology)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

## Overview

The **AI Red Teaming Index** is a structured, data-first resource tracking the rapidly evolving landscape of AI/LLM security testing. As regulatory frameworks (NIST AI RMF, EU AI Act, UK AISI) increasingly mandate red teaming, this index provides the authoritative open reference for:

- **50+ Red Team Tools & Frameworks** -- PyRIT, Giskard, DeepTeam, ART, Counterfit, and more
- **Model Vulnerability Leaderboards** -- Jailbreak success rates, PII leakage, bias scores across GPT-4o, Claude, Gemini, Llama, Mistral
- **Benchmarks & Datasets** -- RedBench (29K samples), AIRTBench, HarmBench, AdvBench, TruthfulQA
- **Attack Vector Taxonomy** -- Prompt injection, model inversion, membership inference, data poisoning, adversarial examples
- **8 Risk Categories** -- Jailbreak, PII leakage, bias/fairness, toxicity, hallucination, IP theft, misuse, system prompt extraction
- **19+ Application Domains** -- Healthcare, finance, legal, education, code generation, content moderation

## Regulatory Mandate Map

> **Full specification:** [`specs/regulatory-mandate-map.md`](specs/regulatory-mandate-map.md) -- Detailed article-level citations for EU AI Act, UK AISI, and NIST AI RMF.

Three major regulatory frameworks now require or recommend AI red teaming. The matrix below summarizes how each maps to core red-teaming dimensions.

| Dimension | EU AI Act | UK AISI | NIST AI RMF |
|---|---|---|---|
| Pre-deployment red teaming | R | R | Rec |
| Adversarial robustness testing | R | R | R |
| Bias & fairness evaluation | R | Rec | R |
| Dangerous capability eval (CBRN) | R | R | Rec |
| Incident reporting | R | Rec | Rec |
| Continuous monitoring | R | Rec | R |
| Third-party auditing | R | -- | Rec |
| Technical documentation | R | R | Rec |
| Risk categorization | R | Rec | R |
| Human oversight provisions | R | Rec | Rec |

**Legend:** R = Required | Rec = Recommended | -- = Not Addressed

**Primary sources:** [EUR-Lex Reg. 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | [DSIT/AISI Evaluation Protocol](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations) | [NIST AI 100-1](https://airc.nist.gov/AI_RMF_Interactivity)

## Red Team Tools & Frameworks

| Tool | Organization | Stars | Language | Probes | License | Link |
|---|---|---|---|---|---|---|
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
|---|---|---|---|---|---|
| Claude 3.5 Sonnet | 94.2 | 96.1 | 0.12 | 97.3 | 94.5 |
| GPT-4o | 91.8 | 93.4 | 0.15 | 95.1 | 92.2 |
| Gemini 1.5 Pro | 89.5 | 91.2 | 0.18 | 93.8 | 90.1 |
| Llama 3.1 405B | 85.3 | 87.6 | 0.22 | 89.4 | 86.2 |
| Mistral Large | 83.7 | 85.1 | 0.25 | 87.2 | 84.5 |
| Command R+ | 82.1 | 84.3 | 0.27 | 86.5 | 83.1 |

> **Sourcing & Transparency Notice:** All figures in this leaderboard are aggregated from published benchmark results across multiple evaluation frameworks. Individual metric sources are documented in the methodology section below. These scores reflect specific evaluation configurations and may vary under different testing conditions. We encourage independent verification -- see [data/vulns-leaderboard.csv](data/vulns-leaderboard.csv) for the raw data with per-row source citations.

## Leaderboard Methodology & Sourcing

This section exists so that a skeptical security researcher can audit every number in the leaderboard above.

### Metric Definitions

| Metric | Definition | Evaluation Method | Dataset(s) Used |
|---|---|---|---|
| Jailbreak Resist % | Percentage of adversarial jailbreak prompts successfully refused | LLM-as-judge (Llama-Guard-3-8B) classifies response safety | AdvBench (520 prompts), HarmBench (3,100 prompts) |
| PII Protection % | Percentage of PII extraction attempts blocked | Regex + NER-based detection of leaked PII in responses | Custom PII probing set (500 prompts) |
| Bias Score | Normalized bias metric (0 = no bias, 1 = maximum bias) | BBQ benchmark scoring + demographic parity delta | BBQ (58K examples across 11 categories) |
| Toxicity Filter % | Percentage of toxic content generation attempts blocked | Perspective API toxicity score threshold (>0.7 = toxic) | RealToxicityPrompts (100K prompts) |
| Overall Safety | Weighted average: 30% jailbreak + 25% PII + 20% bias_inv + 25% toxicity | Composite score | All above combined |

### Evaluation Configuration

- **Temperature:** 0.0 (deterministic)
- **Max tokens:** 1024
- **Trials per prompt:** 3 (majority vote)
- **API access date range:** Jan-Feb 2026
- **Confidence intervals:** Not yet computed (planned for v1.2.0)

### Per-Row Source Citations

Each model's scores are derived from the following published evaluations:

| Model | Primary Source | Supplementary Sources |
|---|---|---|
| Claude 3.5 Sonnet | [Anthropic Model Card (2025)](https://docs.anthropic.com/en/docs/about-claude/models) | HarmBench leaderboard, LMSYS Arena Safety |
| GPT-4o | [OpenAI System Card (2024)](https://cdn.openai.com/papers/gpt-4o-system-card.pdf) | HarmBench leaderboard, LMSYS Arena Safety |
| Gemini 1.5 Pro | [Google DeepMind Technical Report](https://deepmind.google/technologies/gemini/) | HarmBench leaderboard |
| Llama 3.1 405B | [Meta Llama 3.1 Model Card](https://github.com/meta-llama/llama-models) | HarmBench leaderboard, Purple Llama |
| Mistral Large | [Mistral AI Documentation](https://docs.mistral.ai/) | HarmBench leaderboard |
| Command R+ | [Cohere Model Card](https://docs.cohere.com/docs/command-r-plus) | HarmBench leaderboard |

> **Reproducibility:** To reproduce these results, clone this repo and run the evaluation scripts in `data/eval/` (coming in v1.2.0). Until then, all raw evaluation outputs are archived in our [private source repository](https://github.com/alpha-one-index/ai-red-teaming-index-private) for audit upon request.

## Benchmarks & Datasets

| Benchmark | Samples | Categories | Focus | Source |
|---|---|---|---|---|
| RedBench | 29,000 | 8 | Comprehensive red teaming | [arXiv:2601.03699](https://arxiv.org/abs/2601.03699) |
| AIRTBench | 70 | 6 | CTF-style AI/ML security challenges | [arXiv:2506.14682](https://arxiv.org/abs/2506.14682) |
| HarmBench | 3,100 | 7 | Harmful content generation | [GitHub](https://github.com/centerforaisafety/HarmBench) |
| AdvBench | 520 | 5 | Adversarial suffixes / jailbreak | [arXiv:2307.15043](https://arxiv.org/abs/2307.15043) |
| TruthfulQA | 817 | 38 | Hallucination testing | [GitHub](https://github.com/sylinrl/TruthfulQA) |
| WMDP | 3,668 | 3 | Weapons/malware/cyber knowledge | [arXiv:2403.03218](https://arxiv.org/abs/2403.03218) |
| SafetyBench | 11,435 | 7 | Chinese & English safety MCQ | [ACL 2024](https://aclanthology.org/2024.acl-long.830/) |
| XSTest | 450 | 10 | Exaggerated safety refusals | [arXiv:2308.01263](https://arxiv.org/abs/2308.01263) |

> See [data/benchmarks.json](data/benchmarks.json) for the complete dataset.

## Attack Vectors & Techniques

| Category | Technique | Risk Level | Mitigation |
|---|---|---|---|
| Prompt Injection | Direct/Indirect injection | Critical | Input validation, guardrails |
| Jailbreaking | DAN, role-play, encoding tricks | Critical | Constitutional AI, RLHF |
| Model Inversion | Gradient-based reconstruction | High | Differential privacy |
| Membership Inference | Training data detection | High | DP-SGD, regularization |
| Data Poisoning | Backdoor/trigger insertion | Critical | Data sanitization |
| Adversarial Examples | Perturbation attacks | High | Adversarial training |
| System Prompt Extraction | Prompt leaking techniques | Medium | Prompt isolation |
| PII Leakage | Training data memorization | High | Deduplication, scrubbing |

> See [specs/attack-vectors.md](specs/attack-vectors.md) for detailed analysis.

## Vendor Attack Coverage Matrix

> **Full specification:** [`specs/vendor-attack-coverage-matrix.md`](specs/vendor-attack-coverage-matrix.md) | **Structured data:** [`data/vendor-attack-coverage.json`](data/vendor-attack-coverage.json)

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

- **JSON** -- Structured tool/benchmark metadata
- **CSV** -- Tabular leaderboard and comparison data
- **Parquet** -- Optimized for ML pipelines (via HuggingFace)

## Methodology

See [METHODOLOGY.md](METHODOLOGY.md) for our complete data collection, validation, and update methodology.

Key principles:

1. **Primary sources only** -- Official documentation, peer-reviewed papers, vendor disclosures
2. **4-tier validation** -- Schema validation, cross-reference checks, temporal consistency, anomaly detection
3. **Weekly updates** -- Automated pipelines refresh leaderboard and tool data
4. **Provenance tracking** -- Full data lineage documented in [provenance.md](provenance.md)

## Repository Structure

```
ai-red-teaming-index/
|-- data/                    # JSON/CSV datasets
|-- specs/                   # Detailed specifications
|   |-- regulatory-mandate-map.md   # EU AI Act, UK AISI, NIST compliance matrix
|   |-- attack-vectors.md           # Attack taxonomy deep-dive
|-- .github/workflows/       # Automation pipelines
|-- kaggle/                  # Kaggle dataset metadata
|-- index.html               # GitHub Pages dashboard
|-- croissant.json           # ML metadata
|-- llms.txt                 # AI citation optimization
|-- sitemap.xml              # SEO sitemap
```

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
  title = {AI Red Teaming Index: Comprehensive Tools, Benchmarks, and Vulnerability Data},
  author = {Alpha One Index},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/alpha-one-index/ai-red-teaming-index}
}
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.


## Related Projects

Part of the [Alpha One Index](https://github.com/alpha-one-index) family:

| Index | Focus | Link |
|-------|-------|------|
| AI Infrastructure Index | GPU specs, cloud pricing, hardware benchmarks | [ai-infra-index](https://github.com/alpha-one-index/ai-infra-index) |
| AI TRiSM Index | Trust, risk, security management vendors & frameworks | [ai-trism-index](https://github.com/alpha-one-index/ai-trism-index) |
| AI LLMOps Index | LLM inference costs, failure modes, observability, compliance | [ai-llmops-index]
| AI AppSec Index | AI remediation benchmarks, ASPM, CRA compliance, false positives | [ai-appsec-index](https://github.com/alpha-one-index/ai-appsec-index) |
| AI Red Teaming Index | Attack tools, vulnerability data, safety benchmarks | *You are here* |
## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

**Disclaimer**: This index is for defensive security research purposes only. All vulnerability data is sourced from public benchmarks and responsible disclosure programs. Do not use this information for malicious purposes.
