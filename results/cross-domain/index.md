---
layout: program-doc
title: "Cross-Domain Edges"
permalink: /results/cross-domain/
lane: results
v2_lane: results
type: "Cross-Domain Surface"
status: "Canonical"
hero_eyebrow: "Results · Cross-Domain"
summary_short: "The structural junctions where physics, life, and metaphysics readouts meet — auto-derived from glossary cross-references."
---

The τ-framework's three glossary domains (physics, life, metaphysics) are not independent silos. Every empirical observation in physics has its life-sector amplification; every life-sector chirality bias has its categorical readout; every metaphysical commitment has its empirical anchor. **Cross-domain edges** are the explicit structural bridges between these.

This page surfaces every cross-domain `related_glossary_entries` link in the glossary as a navigable graph. The current count and edge list below regenerate automatically as glossary entries are extended.

## Summary

{% assign cross_data = site.data.glossary["cross-domain-links"] %}
{% assign edges = cross_data.edges %}
{% assign by_id = site.data.glossary["by-id"].by_id %}

<div class="v2-grid">
  <a class="v2-tile" href="#all-edges">
    <strong>{{ edges | size }} cross-domain edges</strong>
    <span>Direct glossary references that span ≥2 domains.</span>
  </a>
  <a class="v2-tile" href="#physics-life">
    <strong>Physics ↔ Life</strong>
    <span>The neutron mass anchor + K_χ chain.</span>
  </a>
  <a class="v2-tile" href="#physics-metaphysics">
    <strong>Physics ↔ Metaphysics</strong>
    <span>Empirical Reg_E reads physics observables.</span>
  </a>
  <a class="v2-tile" href="#life-metaphysics">
    <strong>Life ↔ Metaphysics</strong>
    <span>Consciousness, qualia, K_χ → Reg_E bridges.</span>
  </a>
</div>

## How cross-domain edges work

Each glossary entry's `related_glossary_entries` field can name terms from **any** of the three domains. When a Physics entry references a Life or Metaphysics term (or vice versa), that edge is a **cross-domain bridge**. The export pipeline counts and surfaces these:

```
exports/public/glossary/cross-domain-links.json:
{
  "edge_count": <total>,
  "edges": [{ "from": <id>, "from_domain": <d>, "to": <id>, "to_domain": <d> }, ...]
}
```

These edges are how the framework keeps its three domains coherent. When the K_χ channel (LG-Y02) explicitly references the neutron-mass anchor (PG-P01), it's not metaphor — it's a structural commitment that the chirality amplifier is anchored to physics.

## Bridge categories

### <span id="physics-life"></span>Physics ↔ Life

The most fundamental bridge. Every life-sector observable inherits its calibration from m_n via the K_χ chain. The pivots:

<ul class="cross-domain-edge-list">
{% for edge in edges %}
  {% if edge.from_domain == "physics" and edge.to_domain == "life" %}
    {% assign source_e = by_id[edge.from] %}
    {% assign target_e = by_id[edge.to] %}
    {% if source_e and target_e %}
    <li>
      <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
      <span class="cross-domain-edge-arrow">→</span>
      <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
    </li>
    {% endif %}
  {% endif %}
  {% if edge.from_domain == "life" and edge.to_domain == "physics" %}
    {% assign source_e = by_id[edge.from] %}
    {% assign target_e = by_id[edge.to] %}
    {% if source_e and target_e %}
    <li>
      <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
      <span class="cross-domain-edge-arrow">→</span>
      <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
    </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### <span id="physics-metaphysics"></span>Physics ↔ Metaphysics

Metaphysics's empirical register Reg_E reads physics observables; physics's anchor m_n is the canonical Reg_E example.

<ul class="cross-domain-edge-list">
{% for edge in edges %}
  {% if edge.from_domain == "physics" and edge.to_domain == "metaphysics" %}
    {% assign source_e = by_id[edge.from] %}
    {% assign target_e = by_id[edge.to] %}
    {% if source_e and target_e %}
    <li>
      <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
      <span class="cross-domain-edge-arrow">→</span>
      <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
    </li>
    {% endif %}
  {% endif %}
  {% if edge.from_domain == "metaphysics" and edge.to_domain == "physics" %}
    {% assign source_e = by_id[edge.from] %}
    {% assign target_e = by_id[edge.to] %}
    {% if source_e and target_e %}
    <li>
      <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
      <span class="cross-domain-edge-arrow">→</span>
      <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
    </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

### <span id="life-metaphysics"></span>Life ↔ Metaphysics

Where biology meets categorical architecture. Consciousness (LG-M01) bridges to the CI operator graph (MG-A01) and qualia (MG-H01); the K_χ channel feeds Reg_E.

<ul class="cross-domain-edge-list">
{% for edge in edges %}
  {% if edge.from_domain == "life" and edge.to_domain == "metaphysics" %}
    {% assign source_e = by_id[edge.from] %}
    {% assign target_e = by_id[edge.to] %}
    {% if source_e and target_e %}
    <li>
      <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
      <span class="cross-domain-edge-arrow">→</span>
      <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
    </li>
    {% endif %}
  {% endif %}
  {% if edge.from_domain == "metaphysics" and edge.to_domain == "life" %}
    {% assign source_e = by_id[edge.from] %}
    {% assign target_e = by_id[edge.to] %}
    {% if source_e and target_e %}
    <li>
      <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
      <span class="cross-domain-edge-arrow">→</span>
      <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
    </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

## <span id="all-edges"></span>All cross-domain edges

<ul class="cross-domain-edge-list">
{% for edge in edges %}
  {% assign source_e = by_id[edge.from] %}
  {% assign target_e = by_id[edge.to] %}
  {% if source_e and target_e %}
  <li>
    <a href="{{ '/results/' | append: source_e.domain | append: '/glossary/' | append: source_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ source_e.domain }}"><code>{{ source_e.id }}</code> {{ source_e.name }}</a>
    <span class="cross-domain-edge-arrow">→</span>
    <a href="{{ '/results/' | append: target_e.domain | append: '/glossary/' | append: target_e.id | append: '/' | relative_url }}" class="chip chip-glossary chip-glossary-{{ target_e.domain }}"><code>{{ target_e.id }}</code> {{ target_e.name }}</a>
  </li>
  {% endif %}
{% endfor %}
</ul>

## Read next

- [Physics Glossary]({{ '/results/physics/glossary/' | relative_url }}) — 95 entries
- [Life Glossary]({{ '/results/life/glossary/' | relative_url }}) — 78 entries
- [Metaphysics Glossary]({{ '/results/metaphysics/glossary/' | relative_url }}) — 68 entries
- [Glossary Onboarding]({{ '/results/glossary-onboarding/' | relative_url }}) — vocabulary primer for τ-framework newcomers
