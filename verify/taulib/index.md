---
layout: program-doc
title: "TauLib Inspection Bridge"
permalink: /verify/taulib/
lane: verify
v2_lane: verify
type: "Verification Bridge"
status: "Canonical"
summary_short: "Verify-side bridge into the Corpus-native TauLib module and declaration projection."
og_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
twitter_image: /assets/images/plates/plate-06-verification-matrix-og.jpg
og_image_alt: "Scientific plate showing the Verify lane as a verification matrix for obligations, construction steps, results, formal proof checking, bridge adequacy, empirical tests, external assessment, and explicit limits."
hero_ctas:
  - label: "Browse TauLib"
    url: /verify/taulib/docs/
    primary: true
  - label: "Formalization Status"
    url: /verify/taulib/status/
  - label: "Verify Framework"
    url: /verify/verification-framework/
right_rail:
  related:
    - title: "TauLib Browser"
      url: /verify/taulib/docs/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Verification Framework"
      url: /verify/verification-framework/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Release Manifest"
      url: /verify/release-manifest/
  meta:
    type: "Verification Bridge"
    status: "Canonical"
    updated: "May 2026"
---

{% assign summary = site.data.taulib_projections.summary %}

## What TauLib Verifies

TauLib is the Lean formalization layer of the program. The active Lean development source remains the public [TauLib repository](https://github.com/Panta-Rhei-Research/taulib); the Corpus owns a pinned snapshot and generates the public module/declaration browser from that source.

The current projection contains **{{ summary.module_count }} modules** and **{{ summary.declaration_count }} declarations/evals**, pinned to commit [`{{ summary.source_commit | slice: 0, 7 }}`](https://github.com/Panta-Rhei-Research/taulib/commit/{{ summary.source_commit }}).

## TauLib inside the verification matrix

{% include scientific-plate.html id="plate-06-verification-matrix" variant="thumb" loading="lazy" caption="TauLib is one formalization surface inside the broader verification matrix. Lean compilation checks formalized obligations; it does not by itself establish empirical truth." %}

TauLib is one formalization surface inside the broader verification matrix. Lean compilation checks formalized obligations; it does not by itself establish empirical truth.

## Release Lines

<!--
  v5 next-wave W8b · IA Doctrine v5 §9.2 + Release Lines Addendum §7.
  Source: atlas/website/v5/panta-rhei-release-lines-formalization-
          surfaces-v5-addendum.md §7 (TauLib Release Lines) + §9.2
          (Verify lane TauLib representation).
  Data:   _data/release_lines.yml · formalization_release_lines.

  Inspection-bridge view of the same release lines that /corpus/
  taulib/ surfaces (Corpus side, W8a). Each line is read here as
  a trust-boundary surface: which line is citable as a proof basis,
  which is active and therefore not yet citable, and which packages
  are released per-result.
-->

TauLib is published through two release lines plus a per-result proof-package layer. From an inspection standpoint, each line is a distinct trust-boundary surface:

<ul class="v2-grid v2-card-list">
  <li><article class="v2-tile">
    <h3>TauLib v2 Snapshot</h3>
    <p><strong>Citable as a proof basis.</strong> Frozen Lean projection of the Second-Edition Corpus; pinned commit and Lean toolchain are stamped in the <a href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a>. Reviewers can clone the pinned commit, re-run <code>lake build</code>, and reproduce the compilation result that this page reports.</p>
  </article></li>
  <li><article class="v2-tile">
    <h3>TauLib v3 Library</h3>
    <p><strong>Active restructure · not yet citable.</strong> Layered library — import-isolated kernel, Mathlib-facing bridges, community-readable module structure — currently in private development. Not a proof basis for any cited Result until it ships publicly; current Results cite the v2 Snapshot.</p>
  </article></li>
  <li><article class="v2-tile">
    <h3>Proof Packages</h3>
    <p><strong>Per-result · per-package state.</strong> Isolated reproducibility bundles for specific formal results. Each package moves through five states: <em>in construction · draft · candidate · released · superseded</em>. Released packages are citable as a per-result proof basis; non-released states should not be cited as proof.</p>
  </article></li>
</ul>

> **Trust boundary.** Lean compilation checks encoded formal obligations. It does not by itself establish empirical truth, bridge adequacy, or external scientific acceptance. The release-line distinction above is about formalization status; the [Verification Framework]({{ '/verify/verification-framework/' | relative_url }}) and [How to Verify]({{ '/verify/how-to-verify/' | relative_url }}) cover the broader inspection questions.

## What Verify still owns

Verify does not stop at “the Lean code compiles.” It asks the higher-level inspection questions:

- What does the formalization cover?
- What do the formal terms mean relative to the surrounding Corpus?
- Which bridges connect formal objects to mathematical, physical, biological, or metaphysical claims?
- Which claims remain empirical, semantic, interpretive, or externally assessable?
- Where should a reviewer challenge the assumptions rather than merely re-run compilation?

## Inspection routes

<ul class="v2-grid v2-card-list">
  <li><article class="v2-tile"><h3><a href="{{ '/verify/taulib/docs/' | relative_url }}">TauLib Browser</a></h3><p>Corpus-native module and declaration pages generated directly from the pinned Lean snapshot.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/taulib/status/' | relative_url }}">Formalization Status</a></h3><p>Current counts, source commit, custom-axiom count, and projection boundary.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/formal-verification-stack/' | relative_url }}">Formal Verification Stack</a></h3><p>How formal proof checking fits into the broader review workflow.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/verification-framework/' | relative_url }}">Verification Framework</a></h3><p>How formal, bridge, empirical, and external-status checks remain distinct.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a></h3><p>The pinned public release context and count reconciliation surface.</p></article></li>
</ul>
