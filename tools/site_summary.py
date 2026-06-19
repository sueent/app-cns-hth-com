# tools/site_summary.py

import json
from datetime import date


def load_sites_database():
    """Return a list of site records as structured dictionaries."""
    return [
        {
            "name": "HTH Central",
            "url": "https://app-cns-hth.com",
            "keywords": ["hth", "central", "portal"],
            "tags": ["main", "live"],
            "description": "Central access point for HTH operations and dashboards."
        },
        {
            "name": "HTH Info",
            "url": "https://docs-cns-hth.com",
            "keywords": ["hth", "docs", "help"],
            "tags": ["reference", "support"],
            "description": "Documentation and knowledge base for the HTH platform."
        },
        {
            "name": "HTH Status",
            "url": "https://status-cns-hth.com",
            "keywords": ["hth", "uptime", "health"],
            "tags": ["monitoring", "live"],
            "description": "Real‑time status and incident reports for HTH services."
        },
        {
            "name": "HTH Sandbox",
            "url": "https://sandbox-cns-hth.com",
            "keywords": ["hth", "test", "staging"],
            "tags": ["development", "internal"],
            "description": "Isolated environment for testing HTH integrations."
        }
    ]


def build_summary_entry(record):
    """Construct a concise summary string from a site record."""
    kw_str = ", ".join(record["keywords"])
    tag_str = ", ".join(record["tags"])
    return (
        f"Site: {record['name']}\n"
        f"  URL:        {record['url']}\n"
        f"  Keywords:   {kw_str}\n"
        f"  Tags:       {tag_str}\n"
        f"  Description: {record['description']}"
    )


def generate_report(sites):
    """Produce a full structured report as a string."""
    lines = []
    lines.append("=" * 60)
    lines.append("SITE SUMMARY REPORT")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append("=" * 60)
    lines.append("")

    for idx, site in enumerate(sites, start=1):
        lines.append(f"[#{idx}]")
        lines.append(build_summary_entry(site))
        lines.append("")

    lines.append("-" * 60)
    lines.append(f"Total sites listed: {len(sites)}")
    lines.append("=" * 60)

    return "\n".join(lines)


def export_json(sites, filepath="site_summary.json"):
    """Write the sites data to a JSON file for external usage."""
    payload = {
        "report_date": str(date.today()),
        "site_count": len(sites),
        "sites": sites
    }
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    return filepath


def main():
    """Orchestrate the summary generation and display."""
    sites = load_sites_database()
    report = generate_report(sites)
    print(report)

    json_path = export_json(sites)
    print(f"\nJSON export saved to: {json_path}")


if __name__ == "__main__":
    main()