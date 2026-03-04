# Contributing to AI Red Teaming Index

Thank you for your interest in contributing! This project aims to be the most comprehensive open index of AI red teaming tools, benchmarks, and vulnerability data.

## How to Contribute

### Adding a New Tool
1. Fork the repository
2. Add the tool entry to `data/red-team-tools.json`
3. Follow the existing JSON schema (name, organization, github_url, stars, language, probes, license, category, description, last_updated)
4. Submit a pull request with a clear description

### Updating Leaderboard Data
1. Add or update entries in `data/vulns-leaderboard.csv`
2. Include source references for all benchmark scores
3. Use the standard column format

### Reporting Issues
- Use GitHub Issues for bug reports and feature requests
- Label issues appropriately (bug, enhancement, data-update, help-wanted)

## Data Quality Standards
- All data must come from primary sources (official docs, papers, vendor disclosures)
- Include citations for benchmark scores
- Verify tool star counts and activity status
- Follow ISO 8601 date format (YYYY-MM-DD)

## Code of Conduct
This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct. Be respectful and constructive.

## License
By contributing, you agree that your contributions will be licensed under the MIT License.
