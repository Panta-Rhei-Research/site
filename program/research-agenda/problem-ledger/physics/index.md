---
layout: program-doc
title: "Physics Problem Ledger"
lane: program
v2_lane: program
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "The physics master ledger as an external stress test for formalized reality-description."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Physics Results"
      url: /results/topic/physics/
  meta:
    type: "Domain Ledger"
    scope: "Physics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "physics" | sort: "title" %}

## Source rule

Physics uses the full Wikipedia list of unsolved problems in physics as the master ledger. The seed item below proves the projection path before the wholesale import wave.

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

