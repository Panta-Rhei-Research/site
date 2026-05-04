---
layout: program-doc
title: "Mathematics Core Semantics"
lane: agenda
v2_lane: agenda
section: research-agenda
type: "Core Semantics Domain"
status: "Canonical"
summary_short: "The language and structures the theory must earn in mathematics before it can answer."
right_rail:
  related:
    - title: "Core Semantics"
      url: /agenda/core-semantics/
    - title: "Mathematical Refusals"
      url: /agenda/core-semantics/mathematics/refusals/
    - title: "Mathematics Problem Ledger"
      url: /agenda/problem-ledger/mathematics/
  meta:
    type: "Core Semantics Domain"
    scope: "Mathematics"
    status: "Canonical"
    updated: "May 2026"
---

# Mathematics Core Semantics

The language and structures the theory must earn in mathematics before it can answer.

Mathematics Core Semantics includes recovery targets for formal checkability, finite syntax and proof objects, finite arithmetic and algebraic calculation, Euclidean geometry, representation of standard formal systems as object theories, and explicit bridge criteria into standard mathematics.

Core Semantics does not require reproducing established semantics unchanged. It requires carrying what works, retyping what breaks, and making any semantic transformation explicit.

{% assign items = site.core_semantics | where: "domain", "mathematics" | sort: "canonical_recovery_id" %}

## Why Core Semantics differs from open problems

The Mathematics Problem Ledger asks whether the kernel can express or re-ground Clay- and Langlands-scale stress tests. Mathematics Core Semantics asks which mathematical capacities must be earned before those stress tests can even be handled responsibly.

The recovery burden is not to import standard foundations wholesale. It is to recover formal checkability, finite syntax and proof objects, finite arithmetic and algebraic calculation, Euclidean geometry, representation of standard formal systems as object theories, and explicit bridge criteria into standard mathematics.

## Mathematical refusals

These recovery targets must be read together with the [Mathematical Refusals]({{ '/agenda/core-semantics/mathematics/refusals/' | relative_url }}). The tau-kernel does not recover mathematics by silently importing unrestricted classical background assumptions.

## Recovery targets

<div class="dep-list">
  {% for item in items %}
  {% if item.item_type == "recovery_requirement" %}
  <a class="dep-link" href="{{ item.url | relative_url }}">
    <span class="dep-id">{{ item.canonical_recovery_id }}</span>
    <span class="dep-title">{{ item.title }}</span>
    <span class="badge {% if item.recovery_status == 'partial' %}badge-partial{% else %}badge-neutral{% endif %}" style="margin-left:auto">{{ item.recovery_status | replace: "_", " " }}</span>
  </a>
  {% endif %}
  {% endfor %}
</div>

## Relation to Verify

Mathematics Core Semantics connects directly to formal verification, bridge verification, TauLib, and the meta-verification frontier. The page fixes the public burden; the Verify lane records how much of that burden has actually been discharged.
