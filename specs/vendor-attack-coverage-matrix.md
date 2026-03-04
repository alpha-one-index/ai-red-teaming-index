# Vendor Attack Coverage Matrix

Which red teaming tools cover which attack classes? This matrix maps each vendor to the specific attack categories their tools address, sourced to their documentation or published materials.

> **Transparency note**: Every coverage claim below is version-pinned and linked to a source URL. Cells marked with a dash indicate the vendor does not currently support that attack class. See [data/vendor-attack-coverage.json](../data/vendor-attack-coverage.json) for the full machine-readable dataset.

## Coverage Matrix

| Attack Class | PyRIT (Microsoft) | Giskard | DeepTeam (Confident AI) | ART (IBM) | Garak (NVIDIA) | Promptfoo |
|---|---|---|---|---|---|---|
| **Prompt Injection** | Yes: direct, indirect | Yes: direct, indirect | Yes: direct, indirect | — | Yes: direct, indirect | Yes: direct, indirect |
| **Jailbreaking** | Yes: role-play, encoding, multi-turn, crescendo, PAIR | Yes: role-play, crescendo, multi-turn | Yes: role-play, multi-turn | — | Yes: role-play, encoding, multi-turn | Yes: role-play, encoding, multi-turn, crescendo |
| **Data Poisoning** | — | — | — | Yes: training-data, backdoor, detection-evasion | — | — |
| **Model Extraction** | — | — | — | Yes: API query, distillation | — | — |
| **Membership Inference** | — | — | — | Yes: shadow-model, attribute-inference | — | — |
| **Multimodal** | Yes: image | — | — | Yes: adversarial-image, audio | — | — |
| **Agentic AI** | — | Yes: tool-misuse | — | — | — | Yes: tool-misuse |
| **Evasion** | Yes: encoding, token-smuggling | Yes: encoding | Yes: encoding | Yes: adversarial-suffixes, perturbation (50+) | Yes: encoding, token-smuggling | Yes: encoding |
| **Supply Chain** | — | — | — | — | — | — |

## Key Findings

- **No single tool covers all 9 attack classes.** Organizations need a multi-tool strategy.
- **Agentic AI attacks are the least covered** — only Giskard and Promptfoo have initial support. This is an emerging gap as agent deployments accelerate.
- **Membership inference and model extraction** are only covered by IBM's ART, which focuses on traditional ML rather than LLMs.
- **Multimodal attacks** are poorly covered in LLM-focused tools. Only PyRIT (image) and ART (image + audio) address this.
- **Supply chain attacks** have zero automated tool coverage across all vendors assessed.

## Assessment Methodology

- **Version-pinned**: Each assessment is tied to a specific tool version (see JSON data).
- **Source-linked**: Every "Yes" claim links to vendor documentation, GitHub code, or published blog posts.
- **Negative evidence tracked**: "No" claims include notes explaining why (e.g., "not in scope" vs. "planned for future release").
- **Last assessed**: 2026-03-04

## Data Source

The structured data behind this matrix is available at [`data/vendor-attack-coverage.json`](../data/vendor-attack-coverage.json) for programmatic consumption.

## Related Specs

- [Attack Vector Taxonomy](./attack-vectors.md) — Full classification of all 29 attack vectors with MITRE ATLAS IDs
- [Regulatory Mandate Map](./regulatory-mandate-map.md) — EU AI Act, NIST, and UK AISI compliance mapping
