---
layout: program-doc
title: "Mathematics Problem Ledger"
lane: program
v2_lane: program
section: research-agenda
type: "Problem Ledger Domain"
status: "Canonical"
summary_short: "Clay 7 + Langlands as selected foundational stress tests."
right_rail:
  related:
    - title: "Problem Ledger"
      url: /program/research-agenda/problem-ledger/
    - title: "Source Policy"
      url: /program/research-agenda/problem-ledger-source-policy/
    - title: "Mathematics Results"
      url: /results/topic/mathematics/
  meta:
    type: "Domain Ledger"
    scope: "Mathematics"
    status: "Canonical"
    updated: "April 2026"
---

{% assign items = site.problem_ledger | where: "domain", "mathematics" | sort: "title" %}

## Source rule

Mathematics uses selected foundational stress tests, not a wholesale open-math import. The v2 ledger starts with the Clay Millennium Problems and the Langlands Program.

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

