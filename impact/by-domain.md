---
layout: program-doc
title: Impact by Domain
permalink: /impact/by-domain/
lane: impact
summary_short: Portfolios grouped by public-good domain.
right_rail:
  meta:
    type: Index
    updated: April 2026
---

## Portfolios by Domain

This support index remains available for readers who arrive from older links. The canonical portfolio home is [Global Public Good]({{ '/impact/global-public-good/' | relative_url }}).

{% for slug in site.data.impact.portfolio_order %}
{% assign p = site.data.impact.portfolios[slug] %}
- **[{{ p.title }}]({{ p.url | relative_url }})** - {{ p.summary_short }} ({{ p.paper_count }} {% if p.paper_count == 1 %}paper{% else %}papers{% endif %})
{% endfor %}
