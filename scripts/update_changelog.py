#!/usr/bin/env python3
"""Auto-update CHANGELOG.md with weekly data refresh entries."""
import json
import datetime

def main():
    today = datetime.date.today().isoformat()
    changelog_path = "CHANGELOG.md"
    tools_path = "data/red-team-tools.json"

    # Get tool count
    tool_count = "?"
    try:
        with open(tools_path) as f:
            tools = json.load(f)
        tool_count = len(tools)
        updated = sum(1 for t in tools if t.get("last_updated") == today)
    except Exception:
        updated = 0

    # Build the new entry
    entry = f"\n### Auto-Refresh -- {today}\n\n"
    entry += f"- Red team tools refreshed: {tool_count} tools, {updated} updated with latest GitHub stats\n"
    entry += f"- Data files refreshed via automated pipeline\n"

    # Read existing changelog
    with open(changelog_path, "r") as f:
        content = f.read()

    # Check if today's entry already exists
    if f"Auto-Refresh -- {today}" in content:
        print(f"CHANGELOG already has entry for {today}, skipping")
        return

    # Insert after first --- separator
    idx = content.find("[1.1.0]")
    if idx == -1:
        idx = content.find("[1.0.0]")
    if idx == -1:
        idx = content.find("---")
    if idx != -1:
        hr_idx = content.rfind("---", 0, idx)
        if hr_idx != -1:
            insert_pos = hr_idx + 3
            content = content[:insert_pos] + "\n" + entry + content[insert_pos:]
        else:
            # Insert right before the version header
            content = content[:idx] + entry + "\n" + content[idx:]

    with open(changelog_path, "w") as f:
        f.write(content)

    print(f"CHANGELOG.md updated with auto-refresh entry for {today}")

if __name__ == "__main__":
    main()
