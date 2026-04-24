---
layout: program-doc
title: "Metaphysics / Philosophy Problem Ledger"
lane: program
v2_lane: program
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "Philosophical problems as stress tests for ontology, knowledge, mind, meaning, and ethics."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Philosophy Results"
      url: /results/topic/philosophy/
  meta:
    type: "Domain Ledger"
    scope: "Metaphysics / Philosophy"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "metaphysics_philosophy" | sort: "title" %}

## Source rule

Metaphysics / Philosophy uses Wikipedia's list of philosophical problems. The site does not rename that source as an unsolved-problems-in-philosophy ledger.

## Current seed items

<div class="dep-list">
  {% for problem in items %}
  <a class="dep-link" href="{{ problem.url | relative_url }}">
    <span class="dep-id">{{ problem.canonical_problem_id }}</span>
    <span class="dep-title">{{ problem.title }}</span>
    <span class="chip" style="margin-left:auto">{{ problem.program.result_status | replace: "_", " " }}</span>
  </a>
  {% endfor %}
</div>

