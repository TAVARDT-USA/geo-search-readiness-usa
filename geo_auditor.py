#!/usr/bin/env python3
import sys
import re
import json
import ssl
import argparse
import urllib.request

AI_CRAWLERS = [
    "GPTBot",
    "OAI-SearchBot",
    "PerplexityBot",
    "ClaudeBot",
    "Google-Extended",
    "Applebot-Extended"
]

def audit_target(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    base_url = url.rstrip("/")
    domain = re.sub(r"^https?://", "", base_url).split("/")[0]

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    results = {
        "domain": domain,
        "robots_txt_status": "Not Checked",
        "blocked_bots": [],
        "has_schema_jsonld": False,
        "has_meta_description": False,
        "has_h1": False,
        "score": 0,
        "status": "Pending",
        "recommendations": []
    }

    # 1. Inspect robots.txt for AI crawlers
    robots_url = f"https://{domain}/robots.txt"
    try:
        req = urllib.request.Request(robots_url, headers={"User-Agent": "TAVARDT-GEO-Auditor/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=4) as resp:
            text = resp.read().decode("utf-8", errors="ignore")
            results["robots_txt_status"] = "Found (HTTP 200)"
            for bot in AI_CRAWLERS:
                pattern = rf"(?i)User-agent:\s*{bot}\s+Disallow:\s*/"
                if re.search(pattern, text):
                    results["blocked_bots"].append(bot)
    except Exception:
        results["robots_txt_status"] = "Unavailable or 404"

    # 2. Inspect Homepage HTML
    try:
        req = urllib.request.Request(f"https://{domain}/", headers={"User-Agent": "TAVARDT-GEO-Auditor/1.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=5) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            if 'type="application/ld+json"' in html or "type='application/ld+json'" in html:
                results["has_schema_jsonld"] = True
            if re.search(r'(?i)<meta\s+name=["']description["']\s+content=["'][^"']+["']', html):
                results["has_meta_description"] = True
            if re.search(r'(?i)<h1[^>]*>.*?</h1>', html, re.DOTALL):
                results["has_h1"] = True
    except Exception:
        pass

    # Scoring
    score = 0
    if results["robots_txt_status"].startswith("Found"):
        score += 20
    if not results["blocked_bots"]:
        score += 30
    else:
        results["recommendations"].append(f"AI crawlers blocked in robots.txt: {', '.join(results['blocked_bots'])}")

    if results["has_schema_jsonld"]:
        score += 30
    else:
        results["recommendations"].append("Missing Schema.org JSON-LD structured data for entity extraction")

    if results["has_meta_description"]:
        score += 10
    else:
        results["recommendations"].append("Missing or empty meta description tag")

    if results["has_h1"]:
        score += 10
    else:
        results["recommendations"].append("Missing clear H1 heading for topic grounding")

    results["score"] = score
    if score >= 85:
        results["status"] = "AI-Search Ready (High Visibility)"
    elif score >= 50:
        results["status"] = "Moderate Visibility (Optimization Required)"
    else:
        results["status"] = "Restricted (Critical Inconformities Detected)"

    return results

def main():
    parser = argparse.ArgumentParser(description="TAVARDT USA: Generative Engine Optimization (GEO) Auditor")
    parser.add_argument("domain", help="Target domain or base URL to inspect")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    domain = args.domain.strip()
    res = audit_target(domain)

    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return

    border = "=" * 76
    print(border)
    print(f" TAVARDT USA: GENERATIVE ENGINE OPTIMIZATION (GEO) AUDITOR")
    print(border)
    print(f" Target Domain: {res['domain']}")
    print(f" GEO Readiness Score: {res['score']}/100")
    print(f" Overall Assessment: {res['status']}")
    print("-" * 76)
    print(f" AI Crawler Access: {'Allowed' if not res['blocked_bots'] else 'Blocked (' + ', '.join(res['blocked_bots']) + ')'}")
    print(f" Schema.org JSON-LD Markup: {'Present' if res['has_schema_jsonld'] else 'Not Detected'}")
    print(f" Semantic Hierarchy (H1/Meta): H1={'OK' if res['has_h1'] else 'Missing'}, Meta={'OK' if res['has_meta_description'] else 'Missing'}")
    print("-" * 76)
    print(f" Technical Recommendations:")
    if res["recommendations"]:
        for r in res["recommendations"]:
            print(f"   * {r}")
    else:
        print(f"   * Arquitetura semantica e permissões alinhadas para indexacao em motores de IA.")
    print(border)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python geo_auditor.py <domain_or_url> [--json]")
        sys.exit(1)
    main()
