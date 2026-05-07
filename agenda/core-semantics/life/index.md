---
layout: program-doc
title: "Life Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantics Domain"
status: "Canonical"
summary_short: "The language and structures the theory must earn in life before it can answer."
right_rail:
  related:
    - title: "Core Semantics"
      url: /agenda/core-semantics/
    - title: "Life Structural Challenges"
      url: /agenda/structural-challenge-ledger/life/
    - title: "Life Results"
      url: /results/topic/biology/
  meta:
    type: "Core Semantics Domain"
    scope: "Life"
    status: "Canonical"
    updated: "May 2026"
---

The language and structures the theory must earn in life before it can answer.

Life Core Semantics includes recovery targets for boundary, energy throughput, encoding, heredity, reproduction, variation, evolution, development, classification, ecology, and the bridge from living regulation to cognition.

Core Semantics does not require reproducing established semantics unchanged. It requires carrying what works, retyping what breaks, and making any semantic transformation explicit.

{% assign items = site.core_semantics | where: "domain", "life" | sort: "canonical_recovery_id" %}

## Structural, not instance-level

The Life Core Semantics burden is not to derive the contingent inventory of Earth biology. It is to recover the structural grammar that makes life possible: boundary, energy throughput, encoding, heredity, reproduction, variation, evolution, development, classification, ecology, and the bridge from living regulation to cognition.

Earth life is the known calibration case, not the definition of life itself.

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

## Relation to the Life Structural Challenge Ledger

Biology and neuroscience remain external stress-test ledgers. Life Core Semantics names the structural preconditions that make those open problems addressable without assuming that life reduces to physics as an input premise.
