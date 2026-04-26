---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
updated: "April 2026"
title: "Research Monographs"
permalink: "/publications/research-monographs/"
type: "Publication Category"
summary_short: "Full book-length canonical releases of the Panta Rhei framework."
---

## Research Monographs

Research Monographs are the full book-length canonical releases of the Panta Rhei framework. They carry the long-form proof-order exposition of the program.

<div class="notice note"><strong>Category boundary.</strong> Research Monographs are the main canonical volumes. Omitted chapters, ledgers, appendices, and book-style supporting parts released separately belong under Monograph Supplements.</div>

{% for book in site.data.publications.books %}
- **Book {{ book.roman }}**: [{{ book.title }}]({{ book.url | relative_url }}) - *{{ book.subtitle }}* ({{ book.pages }} pages)
{% endfor %}
