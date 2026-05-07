---
layout: program-doc
title: "Metaphysics Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantics Domain"
status: "Canonical"
summary_short: "The language and structures the theory must earn in metaphysics before it can answer."
right_rail:
  related:
    - title: "Core Semantics"
      url: /agenda/core-semantics/
    - title: "Metaphysics / Philosophy Structural Challenges"
      url: /agenda/structural-challenge-ledger/metaphysics/
    - title: "Metaphysics World Readout"
      url: /results/world-readout/metaphysics/
  meta:
    type: "Core Semantics Domain"
    scope: "Metaphysics"
    status: "Canonical"
    updated: "May 2026"
---

The language and structures the theory must earn in metaphysics before it can answer.

Metaphysics Core Semantics includes recovery targets for being, identity, relation, grounding, causality, modality, time, truth, mind, language, value, and ultimate boundary.

Core Semantics does not require reproducing established semantics unchanged. It requires carrying what works, retyping what breaks, and making any semantic transformation explicit.

{% assign items = site.core_semantics | where: "domain", "metaphysics" | sort: "canonical_recovery_id" %}

## Conceptual grammar recovery

Metaphysics Core Semantics is not the claim that the program has solved all philosophy. It is the requirement that the kernel recover the conceptual grammar by which reality becomes intelligible at all: being, identity, relation, grounding, causality, modality, time, truth, mind, language, value, and ultimate boundary.

Ultimate questions must not be invisible to the kernel, but this page does not claim final answers to all ultimate questions.

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

## Relation to Life Core Semantics

The life-mind bridge belongs to Life Core Semantics, while Metaphysics Core Semantics asks how mind, subjectivity, meaning, and value become intelligible in the larger architecture of reality-description.
