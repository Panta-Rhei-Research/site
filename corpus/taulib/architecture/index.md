---
layout: program-doc
title: "TauLib Architecture"
permalink: /corpus/taulib/architecture/
lane: corpus
v2_lane: corpus
type: "Corpus Projection Architecture"
status: "Canonical"
summary_short: "Book and family structure of the Corpus-owned TauLib projection."
---

{% assign modules = site.data.taulib["module-inventory"] %}
{% assign books = modules | group_by: "book" %}

## Book and family structure

TauLib follows the Corpus construction rather than standing outside it. Module families track books, construction layers, and local formalization neighborhoods.

{% for book in books %}
{% assign families = book.items | group_by: "family" %}
### {{ book.name | default: "Root" }}

<ul class="v2-grid v2-card-list">
{% for family in families %}
  <li><article class="v2-tile"><h3>{{ family.name | default: "Root" }}</h3><p>{{ family.items | size }} module{% unless family.items.size == 1 %}s{% endunless %}.</p></article></li>
{% endfor %}
</ul>
{% endfor %}

## Relation to Verify

Architecture here means Corpus architecture: modules, imports, and Registry anchors. Verify uses this architecture to ask higher-level questions about coverage, bridge adequacy, and claim boundaries.
