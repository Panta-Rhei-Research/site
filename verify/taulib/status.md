---
layout: program-doc
title: "TauLib Formalization Status"
permalink: /verify/taulib/status/
lane: verify
v2_lane: verify
type: "Formalization Status"
status: "Canonical"
summary_short: "Pinned TauLib projection counts, source commit, and formal-status boundary."
hero_ctas:
  - label: "Browse TauLib"
    url: /verify/taulib/docs/
    primary: true
  - label: "Release Manifest"
    url: /verify/release-manifest/
right_rail:
  related:
    - title: "TauLib Browser"
      url: /verify/taulib/docs/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Custom Axiom Inventory"
      url: /verify/custom-axioms/
    - title: "Release Manifest"
      url: /verify/release-manifest/
  meta:
    type: "Formalization Status"
    status: "Canonical"
    updated: "April 2026"
---

{% assign summary = site.data.taulib_projections.summary %}
{% assign build = site.data.verify.build %}

## Pinned Source

This status page is generated against the Corpus-native TauLib projection, pinned to TauLib commit [`{{ summary.source_commit | slice: 0, 7 }}`](https://github.com/Panta-Rhei-Research/taulib/commit/{{ summary.source_commit }}). The active contributor-facing Lean development repo remains GitHub; the Corpus projection owns the pinned browse metadata used by this site.

## Current Counts

<table>
  <thead>
    <tr>
      <th scope="col">Metric</th>
      <th scope="col">Current projection</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Modules</th><td>{{ summary.module_count }}</td></tr>
    <tr><th scope="row">Declarations / evaluations</th><td>{{ summary.declaration_count }}</td></tr>
    <tr><th scope="row">Theorems</th><td>{{ summary.declaration_kind_counts.theorem }}</td></tr>
    <tr><th scope="row">Definitions</th><td>{{ summary.declaration_kind_counts.def }}</td></tr>
    <tr><th scope="row">Structures</th><td>{{ summary.declaration_kind_counts.structure }}</td></tr>
    <tr><th scope="row">Examples</th><td>{{ summary.declaration_kind_counts.example }}</td></tr>
    <tr><th scope="row">#eval checks</th><td>{{ summary.declaration_kind_counts.eval }}</td></tr>
    <tr><th scope="row">Custom axioms</th><td>{{ summary.declaration_kind_counts.axiom }}</td></tr>
    <tr><th scope="row">Registry-linked modules</th><td>{{ summary.registry_linked_module_count }}</td></tr>
    <tr><th scope="row">Registry-linked declarations</th><td>{{ summary.registry_linked_declaration_count }}</td></tr>
  </tbody>
</table>

## Verification Boundary

TauLib verifies Lean-formalized statements and executable checks. It does not, by itself, verify empirical adequacy, semantic correspondence to manuscript prose, bridge sufficiency, life-recovery interpretation, or external acceptance. Those layers are inspected through the broader Verify matrix.

## Build Context

- Lean toolchain: `{{ build.lean.version }}`
- Mathlib revision: `{{ build.mathlib.commit_short }}`
- Source license: [{{ build.taulib.license }}]({{ build.taulib.license_url }})
- Public source repo: [{{ build.taulib.repo }}]({{ build.taulib.url }})

For release-level count reconciliation and trusted-base framing, use the [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}).
