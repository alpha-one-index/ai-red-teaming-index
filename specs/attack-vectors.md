# Attack Vector Taxonomy

Standardized classification of AI/LLM attack vectors tracked in the AI Red Teaming Index.

## Categories

| Category | Vector | Description | MITRE ATLAS ID |
|----------|--------|-------------|----------------|
| Prompt Injection | Direct injection | Malicious instructions in user prompt | AML.T0051 |
| Prompt Injection | Indirect injection | Hidden instructions in retrieved content | AML.T0051.001 |
| Prompt Injection | System prompt extraction | Eliciting system-level instructions | AML.T0051.002 |
| Jailbreaking | Role-play bypass | Persona-based safety circumvention | AML.T0054 |
| Jailbreaking | Encoding bypass | Base64/ROT13/translation evasion | AML.T0054 
| Jailbreaking | Multi-turn escalation | Gradual boundary erosion across turns | AML.T0054 |
| Data Poisoning | Training data manipulation | Corrupted data influencing model behavior | AML.T0020 |
| Data Poisoning | Backdoor insertion | Trigger-activated malicious behavior | AML.T0020.001 |
| Model Extraction | API query attacks | Reconstructing model via query patterns | AML.T0024 |
| Model Extraction | Side-channel inference | Exploiting latency/token probabilities | AML.T0024 |
| Evasion | Adversarial suffixes | Appended tokens that alter model behavior | AML.T0043 |
| Evasion | Token smuggling | Unicode/homoglyph-based filter bypass | AML.T0043 |
| Supply Chain | Plugin/tool exploitation | Compromised external tool integrations | AML.T0010 |
| Supply Chain | Model weight tampering | Modified weights in shared model repos | AML.T0010 |

## Severity Levels

| Level | Label | Description |
|-------|-------|-------------|
| 1 | Low | Information disclosure, minor policy bypass |
| 2 | Medium | Consistent safety filter bypass |
| 3 | High | Systematic harmful content generation |
| 4 | Critical | Remote code execution, data exfiltration |

## References

- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI Systems
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI 100-2](https://csrc.nist.gov/publications/detail/nistir/8269/final) - Adversarial ML Taxonomy|
