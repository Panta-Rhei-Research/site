---
layout: program-doc
title: "Core Semantics"
deck: "The language, structures, laws, grammars, and refusal boundaries a coherent theory of reality must be able to carry, retype, or explicitly challenge before it can answer."
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Agenda Ledger"
status: "Canonical"
summary_short: "The language, structures, laws, grammars, and refusal boundaries a coherent theory of reality must be able to carry, retype, or explicitly challenge before it can answer."
tags:
  - core-semantics
  - recovery-requirements
  - recovery
  - refusal
  - earned-language
  - agenda
  - theory-of-reality
hero_ctas:
  - label: "Mathematics"
    url: /agenda/core-semantics/mathematics/
    primary: true
  - label: "Physics"
    url: /agenda/core-semantics/physics/
  - label: "Life"
    url: /agenda/core-semantics/life/
  - label: "Metaphysics"
    url: /agenda/core-semantics/metaphysics/
right_rail:
  related:
    - title: "Structural Challenge Ledger"
      url: /agenda/problem-ledger/
    - title: "Construction Roadmap"
      url: /agenda/construction-roadmap/
    - title: "Coherent Theory of Reality"
      url: /program/about/coherent-theory-of-reality/
    - title: "Result Criteria"
      url: /agenda/result-criteria/
    - title: "Progress Against Agenda"
      url: /results/progress-against-agenda/
  meta:
    type: "Core Semantics"
    scope: "Agenda"
    status: "Canonical"
    updated: "May 2026"
last_updated: "May 2026"
---

{% assign recovery_items = site.core_semantics | sort: "canonical_recovery_id" %}
{% assign math_items = recovery_items | where: "domain", "mathematics" %}
{% assign physics_items = recovery_items | where: "domain", "physics" %}
{% assign life_items = recovery_items | where: "domain", "life" %}
{% assign metaphysics_items = recovery_items | where: "domain", "metaphysics" %}

# Core Semantics

Core Semantics is the language the theory must earn before it can answer.

This section records the structures, laws, grammars, and refusal boundaries that a coherent theory of reality must be able to carry, retype, refine, bridge, or explicitly challenge before its answers can be taken seriously.

This is not a promise to reproduce current semantics unchanged. Where established semantics works, the theory must carry it. Where established semantics breaks, the theory must retype, bridge, or replace it with reasons.

## Why this is separate

Open problems test how the theory behaves where current knowledge does not yet close.

Core Semantics asks an earlier question: can the theory carry the language, structures, laws, grammars, and refusal boundaries those questions presuppose?

The two burdens belong together, but they are not the same. A theory cannot credibly answer open problems if it cannot first earn the language in which those problems are asked.

The current canonical v0.1 public projection contains {{ recovery_items.size }} Core Semantics items (recovery and refusal items).

## Core Semantic domains

- **Mathematics** — formal checkability, finite syntax, arithmetic, geometry, ZFC as object theory, bridge adequacy, and mathematical refusals.
- **Physics** — quantity types, dimensional algebra, unit bridges, constants, laws, regimes, and measurement.
- **Life** — boundary, metabolism, heredity, evolution, development, ecology, and the life–mind bridge.
- **Metaphysics** — being, identity, relation, causality, modality, time, truth, mind, language, value, and ultimate boundary.

<div class="v2-grid">
  <a class="v2-tile" href="{{ '/agenda/core-semantics/mathematics/' | relative_url }}">
    <strong>Mathematics</strong>
    <span>{{ math_items.size }} Core Semantics items (recovery/refusal) covering formal checkability, finite syntax, arithmetic, geometry, ZFC as object theory, bridge adequacy, and mathematical refusals.</span>
  </a>
  <a class="v2-tile" href="{{ '/agenda/core-semantics/physics/' | relative_url }}">
    <strong>Physics</strong>
    <span>{{ physics_items.size }} Core Semantics items covering quantity types, dimensional algebra, unit bridges, constants, laws, regimes, and measurement.</span>
  </a>
  <a class="v2-tile" href="{{ '/agenda/core-semantics/life/' | relative_url }}">
    <strong>Life</strong>
    <span>{{ life_items.size }} Core Semantics items covering boundary, metabolism, heredity, evolution, development, ecology, and the life–mind bridge.</span>
  </a>
  <a class="v2-tile" href="{{ '/agenda/core-semantics/metaphysics/' | relative_url }}">
    <strong>Metaphysics</strong>
    <span>{{ metaphysics_items.size }} Core Semantics items covering being, identity, relation, causality, modality, time, truth, mind, language, value, and ultimate boundary.</span>
  </a>
</div>

## Core Semantics vs problem solving

The Structural Challenge Ledger asks whether the theory can express, classify, constrain, answer, defer, reclassify, or reject external stress-test challenges with reasons.

Core Semantics asks whether the theory can carry the baseline language and structures those questions require: formal reasoning, measurement architecture, life-organization grammar, reflective meaning, and metaphysical intelligibility.

Core Semantics is not a promise to reproduce established semantics unchanged.

## Canonical v0.1 items

<div class="dep-list">
  {% for item in recovery_items %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="chip" style="margin-left:auto">{{ item.display_domain }}</span>
    <span class="badge {% if item.recovery_status == 'partial' %}badge-partial{% elsif item.recovery_status == 'not_applicable' %}badge-muted{% else %}badge-neutral{% endif %}">{{ item.recovery_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>
