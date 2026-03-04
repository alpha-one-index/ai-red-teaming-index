# Regulatory Mandate Map for AI Red Teaming

> How EU AI Act, UK AI Safety Institute (AISI), and NIST AI RMF requirements map to red teaming practices.

**Last updated:** 2026-03-04 | **Maintained by:** [Alpha One Index](https://github.com/alpha-one-index)

---

## Compliance Matrix

The table below maps 10 key red-teaming dimensions against three major regulatory frameworks. Each cell indicates whether the requirement is **Required (R)**, **Recommended (Rec)**, or **Not Addressed (—)**.

| Dimension | EU AI Act | UK AISI | NIST AI RMF | Notes |
|---|---|---|---|---|
| Pre-deployment red teaming | R | R | Rec | EU: Art. 55; UK: AISI pre-deployment protocol; NIST: MEASURE 2.7 |
| Adversarial robustness testing | R | R | R | EU: Art. 15; UK: dangerous capability evals; NIST: MEASURE 2.6 |
| Bias & fairness evaluation | R | Rec | R | EU: Art. 10; NIST: MEASURE 2.5; UK: bias included in broader evals |
| Dangerous capability eval (CBRN) | R | R | Rec | EU: Art. 55(1)(b); UK: CBRN, cyber, persuasion, autonomy evals |
| Incident reporting | R | Rec | Rec | EU: Art. 73 (72-hour reporting); NIST: GOVERN 6.1 |
| Continuous monitoring | R | Rec | R | EU: Art. 72; NIST: MANAGE 4.2 |
| Third-party auditing | R | — | Rec | EU: Art. 43 (conformity assessment); NIST: GOVERN 1.1 |
| Technical documentation | R | R | Rec | EU: Art. 53 (technical docs); UK: hardware submission |
| Risk categorization | R | Rec | R | EU: Art. 6 (risk tiers); NIST: MAP 1.5 |
| Human oversight provisions | R | Rec | Rec | EU: Art. 14; NIST: MEASURE 1.3 |

**Legend:** R = Required | Rec = Recommended | — = Not Addressed

---

## EU AI Act (Regulation 2024/1689)

**Primary source:** [EUR-Lex Official Text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

### Key provisions for red teaming:

- **Art. 6 & Annex III** — Risk classification system (unacceptable / high / limited / minimal)
- **Art. 10** — Data governance requirements including bias testing
- **Art. 14** — Human oversight requirements for high-risk AI
- **Art. 15** — Accuracy, robustness, and cybersecurity requirements
- **Art. 43** — Conformity assessment (third-party audit for high-risk)
- **Art. 51** — GPAI models: 10^25 FLOPs threshold triggers systemic risk classification
- **Art. 53** — Technical documentation obligations for GPAI providers
- **Art. 55** — Adversarial testing (red teaming) required for systemic risk models
- **Art. 72** — Post-market monitoring obligations
- **Art. 73** — Serious incident reporting (72-hour window)

### Enforcement timeline:
- Feb 2025: Prohibited AI practices in force
- Aug 2025: GPAI model obligations apply
- Aug 2026: Full enforcement for high-risk AI systems

---

## UK AI Safety Institute (AISI)

**Primary source:** [DSIT / AISI Pre-Deployment Evaluation Protocol](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations)

### Key evaluation requirements:

- **Pre-deployment evaluations** — Required before release of frontier models under voluntary commitments (Seoul Summit, Nov 2023; Bletchley Declaration)
- **Dangerous capability evaluations** — Structured assessment across four domains:
  1. **CBRN** — Chemical, biological, radiological, nuclear uplift
  2. **Cyber offense** — Autonomous vulnerability discovery and exploitation
  3. **Persuasion & manipulation** — Influence operations capability
  4. **Autonomous replication** — Self-propagation and resource acquisition
- **Hardware submission requirements** — Compute details for training runs
- **Model access** — AISI requires API or weight access for evaluation
- **Inspect framework** — Open-source eval framework ([ukgovernmentbeis/inspect_evals](https://github.com/ukgovernmentbeis/inspect_evals))

### Legal status:
- Currently voluntary (Frontier AI Safety Commitments)
- UK AI Bill expected to formalize requirements

---

## NIST AI Risk Management Framework (AI RMF 1.0)

**Primary source:** [NIST AI 100-1](https://airc.nist.gov/AI_RMF_Interactivity)

### Key functions mapped to red teaming:

- **GOVERN 1.1** — Policies for AI risk management including third-party assessment
- **GOVERN 6.1** — Incident response and escalation procedures
- **MAP 1.5** — Risk identification and categorization
- **MEASURE 1.3** — Human oversight and review processes
- **MEASURE 2.5** — Bias testing and fairness evaluation
- **MEASURE 2.6** — Adversarial robustness and security testing
- **MEASURE 2.7** — Red teaming and adversarial simulation
- **MANAGE 4.2** — Continuous monitoring and response

### Companion documents:
- [NIST AI 600-1: AI RMF Generative AI Profile](https://airc.nist.gov/Docs/1) — GenAI-specific guidance
- [NIST Adversarial ML Taxonomy (NIST AI 100-2e2023)](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) — Attack classification

---

## How This Maps to the AI Red Teaming Index

Each dimension in the compliance matrix above corresponds to sections of this repository:

| Dimension | Index Section |
|---|---|
| Pre-deployment red teaming | [Red Team Tools & Frameworks](../README.md#red-team-tools--frameworks) |
| Adversarial robustness testing | [Benchmarks & Datasets](../README.md#benchmarks--datasets) |
| Bias & fairness evaluation | [Vulnerability Leaderboards](../README.md#vulnerability-leaderboards) |
| Dangerous capability eval | [Attack Vectors & Techniques](../README.md#attack-vectors--techniques) |
| Incident reporting | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| Continuous monitoring | [GitHub Actions Workflows](../.github/workflows/) |

---

## Citation

If referencing this regulatory mapping:

```bibtex
@misc{alphaoneindex2026regmap,
  title = {Regulatory Mandate Map for AI Red Teaming},
  author = {Alpha One Index},
  year = {2026},
  url = {https://github.com/alpha-one-index/ai-red-teaming-index/blob/main/specs/regulatory-mandate-map.md}
}
```
