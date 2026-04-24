---
layout: program-doc
title: "Life Problem Ledger"
lane: program
v2_lane: program
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "Biology and neuroscience as external stress tests for life and mind."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Life Results"
      url: /results/topic/biology/
  meta:
    type: "Domain Ledger"
    scope: "Life"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "life" | sort: "title" %}

## Source rule

Life uses the biology and neuroscience master ledgers. Medicine is excluded as a v2 master ledger because it is primarily clinical and translational rather than the core life-system stress test.

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

