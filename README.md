<p align="center">
  <a href="https://ag.tavardt.com/">
    <img src="https://ag.tavardt.com/img/tavardt-banner.png" alt="TAVARDT" width="1024" />
  </a>
</p>

# Generative Engine Optimization (GEO) Auditor

[![GEO Auditor](https://img.shields.io/badge/TAVARDT-AI%20Search%20GEO-5b3cf5.svg)](https://tools.tavardt.com/ai-search-readiness-checker/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Automated diagnostic engine for Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO), auditing AI crawler access, structured entity graph extraction, and semantic citation signals.

The toolkit evaluates web properties against retrieval-augmented generation (RAG) pipelines powering systems such as SearchGPT, Perplexity AI, Claude, Gemini, and Apple Intelligence. Built with zero third-party dependencies, the utility runs natively in Python CLI environments and automated CI/CD compliance workflows.

***

## GEO Verification Capabilities and Algorithmic Scope

Traditional search optimization focused on string matching and link equity. Generative search engines synthesize conversational answers by executing neural passage retrieval over structured knowledge graphs and authoritative web content.

* **AI Crawler Directive Inspection**: In-depth verification of `robots.txt` access rules for prominent AI user agents: GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended, and Applebot-Extended.
* **Structured Data Entity Graph Extraction**: Verification of Schema.org JSON-LD markup (`application/ld+json`), enabling LLMs to ground facts and disambiguate corporate entities.
* **Semantic Hierarchy and Context Anchors**: Validation of single H1 heading hierarchy and meta description completeness for accurate passage chunking.
* **Quantitative GEO Readiness Scoring**: Algorithmic 0-100 diagnostic index categorizing web properties into High Visibility, Moderate Visibility, or Restricted status.
* **Zero Dependency Footprint**: Pure standard library implementation with zero external package risk, ensuring sub-second execution across developer workstations.

***

## GEO Verification and Scoring Matrix

<table>
  <thead>
    <tr>
      <th align="left">Audit Dimension</th>
      <th align="left">Weight Allocation</th>
      <th align="left">Validation Rule</th>
      <th align="left">Impact on AI Synthesis and Citation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>robots.txt Availability</strong></td>
      <td>20 Points</td>
      <td>HTTP 200 verification on /robots.txt endpoint.</td>
      <td>Ensures search crawlers can deterministically fetch indexing directives.</td>
    </tr>
    <tr>
      <td><strong>AI Crawler Permissions</strong></td>
      <td>30 Points</td>
      <td>No wild card Disallow: / blocking designated AI bots.</td>
      <td>Prevents complete exclusion from LLM retrieval pipelines and citation indices.</td>
    </tr>
    <tr>
      <td><strong>Schema.org JSON-LD</strong></td>
      <td>30 Points</td>
      <td>Presence of valid application/ld+json entity scripts.</td>
      <td>Provides high-fidelity entity grounding, knowledge graph placement, and semantic truth.</td>
    </tr>
    <tr>
      <td><strong>Meta Description Framing</strong></td>
      <td>10 Points</td>
      <td>Non-empty meta name=description tag in document head.</td>
      <td>Supplies clean thematic summarization for AI answer synthesizers and snippets.</td>
    </tr>
    <tr>
      <td><strong>H1 Semantic Anchor</strong></td>
      <td>10 Points</td>
      <td>Presence of top-level h1 heading element.</td>
      <td>Establishes primary contextual root for passage chunking and topic relevance.</td>
    </tr>
  </tbody>
</table>

***

## Installation and Quick Start

Requires Python 3.8 or higher utilizing strictly standard library modules (`sys`, `re`, `json`, `ssl`, `argparse`, `urllib.request`). Zero external packages or pip installations are required.

Clone the repository and inspect a target domain:

```bash
git clone https://github.com/TAVARDT-USA/geo-search-readiness-usa.git
cd geo-search-readiness-usa
python geo_auditor.py example.com
```

To export results in clean JSON format for automated reporting:

```bash
python geo_auditor.py example.com -j
```

Inspect target domains utilizing explicit URL formatting:

```bash
python geo_auditor.py https://example.com -j
```

Sample JSON response payload:

```json
{
  "domain": "example.com",
  "robots_txt_status": "Found (HTTP 200)",
  "blocked_bots": [],
  "has_schema_jsonld": true,
  "has_meta_description": true,
  "has_h1": true,
  "score": 100,
  "status": "AI-Search Ready (High Visibility)",
  "recommendations": []
}
```

Readiness classification brackets:

* **Score 85 to 100**: AI-Search Ready (High Visibility). Complete crawler access and structured semantic anchors.
* **Score 50 to 84**: Moderate Visibility (Optimization Required). Partial indexing barriers or missing structured data.
* **Score 0 to 49**: Restricted (Critical Inconformities Detected). Active crawler blocks or missing semantic foundations.

***

## Frequently Asked Questions

### Why does blocking OAI-SearchBot or PerplexityBot in robots.txt impair real-time conversational search visibility?
OAI-SearchBot and PerplexityBot power active retrieval in answer engines such as ChatGPT Search and Perplexity. Blocking these user agents prevents conversational engines from fetching, referencing, and linking to your web domain during user query resolution.

### How does Schema.org JSON-LD structured data enhance entity extraction in Large Language Models?
LLMs utilize knowledge graphs to resolve ambiguities and verify factual claims. Schema.org JSON-LD explicit markup allows neural processors to ingest structured Organization, Product, FAQ, and Article definitions with high confidence without parsing noise.

### What algorithmic scoring methodology determines the 0 to 100 GEO readiness score?
The score allocates 20 points for accessible robots.txt, 30 points for unblocked AI agents, 30 points for Schema.org JSON-LD, 10 points for a meta description, and 10 points for an H1 heading. Domains achieving 85 points or greater qualify as AI-Search Ready.

### How does the scanner inspect robots.txt and homepage markup without requiring browser rendering?
The engine executes fast HTTP GET requests with custom User-Agent headers directly to `/robots.txt` and the root URL. It parses raw text and HTML streams using regular expressions, bypassing resource-heavy headless browser rendering while delivering sub-second audits.

### How can security and marketing teams integrate the JSON output into continuous deployment gates?
Passing the `-j` flag streams standardized JSON to standard output. CI/CD pipelines can evaluate the `score` and `blocked_bots` attributes using jq, automatically failing builds if staging changes inadvertently introduce crawler disallow directives or purge structured data.

***

## AI Search and Semantic Consulting

For structured data modeling, entity knowledge graph engineering, and AI agent visibility optimization in United States, contact **TAVARDT United States**.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/
* **Diagnostic Suite:** https://tools.tavardt.com/
* **Technical Contact:** https://ag.tavardt.com/contact/

***

### License
Released under the MIT License.

***

© 2026 TAVARDT. All rights reserved.
