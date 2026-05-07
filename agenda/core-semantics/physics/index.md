---
layout: program-doc
title: "Physics Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantics Domain"
status: "Canonical"
summary_short: "The language and structures the theory must earn in physics before it can answer."
right_rail:
  related:
    - title: "Core Semantics"
      url: /agenda/core-semantics/
    - title: "Physics Structural Challenges"
      url: /agenda/structural-challenge-ledger/physics/
    - title: "Physics Results"
      url: /results/topic/physics/
  meta:
    type: "Core Semantics Domain"
    scope: "Physics"
    status: "Canonical"
    updated: "May 2026"
---

The language and structures the theory must earn in physics before it can answer.

Physics Core Semantics includes recovery targets for quantity, dimensional algebra, unit bridges, constants, laws, regimes, and measurement.

Core Semantics does not require reproducing established semantics unchanged. It requires carrying what works, retyping what breaks, and making any semantic transformation explicit. In physics this is decisive: established quantity types, dimensional algebra, unit conventions, and law statements may be carried forward, retyped, or replaced — but every such move must be made explicit rather than assumed.

{% assign items = site.core_semantics | where: "domain", "physics" | sort: "canonical_recovery_id" %}

## Why physics Core Semantics begins with measurement

Physics Core Semantics is not just equation recovery. A candidate kernel must recover physical quantity types, dimensional algebra, internal units, empirical calibration bridges, constants, dynamical laws, regime transitions, and measurement conditions.

SI is a bridge target, not a primitive input. Dimensionful constants require unit bridges; dimensionless constants and ratios are sharper numerical targets.

## Recovery targets

<div class="dep-list">
  {% for item in items %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="badge badge-neutral" style="margin-left:auto">{{ item.verification_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>

## Relation to the Physics Structural Challenge Ledger

The Physics Structural Challenge Ledger tracks open questions. Physics Core Semantics tracks the baseline measurement-and-law architecture those questions presuppose.
