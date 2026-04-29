---
layout: program-doc
title: "TauLib Inspection Bridge"
permalink: /verify/taulib/
lane: verify
v2_lane: verify
type: "Verification Bridge"
status: "Compatibility"
summary_short: "Verify-side bridge from the Corpus-owned TauLib projection to semantic inspection, bridge adequacy, and external assessment."
hero_ctas:
  - label: "Open Corpus TauLib"
    url: /corpus/taulib/
    primary: true
  - label: "Verify Framework"
    url: /verify/verification-framework/
  - label: "Release Manifest"
    url: /verify/release-manifest/
right_rail:
  related:
    - title: "Corpus TauLib"
      url: /corpus/taulib/
    - title: "TauLib Modules"
      url: /corpus/taulib/modules/
    - title: "Verification Framework"
      url: /verify/verification-framework/
    - title: "Formal Verification Stack"
      url: /verify/formal-verification-stack/
    - title: "Release Manifest"
      url: /verify/release-manifest/
  meta:
    type: "Verification Bridge"
    status: "Compatibility"
    updated: "April 2026"
---

## What moved

TauLib is now Corpus-owned as the compiled Lean projection of the Corpus: module inventory, generated docs, Registry links, import graph, source metadata, and projection status.

Use [Corpus TauLib]({{ '/corpus/taulib/' | relative_url }}) for the artifact itself.

## What Verify still owns

Verify does not primarily ask whether the site has a Lean projection. The Corpus publishes that projection as a baseline artifact. Verify asks the higher-level inspection questions:

- What does the formalization cover?
- What do the formal terms mean relative to the surrounding Corpus?
- Which bridges connect formal objects to mathematical, physical, biological, or metaphysical claims?
- Which claims remain empirical, semantic, interpretive, or externally assessable?
- Where should a reviewer challenge the assumptions rather than merely re-run compilation?

## Inspection routes

<ul class="v2-grid v2-card-list">
  <li><article class="v2-tile"><h3><a href="{{ '/corpus/taulib/' | relative_url }}">Corpus TauLib</a></h3><p>The compiled Lean projection, module inventory, docs, and Registry-link map.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/formal-verification-stack/' | relative_url }}">Formal Verification Stack</a></h3><p>How formal proof checking fits into the broader review workflow.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/verification-framework/' | relative_url }}">Verification Framework</a></h3><p>How formal, bridge, empirical, and external-status checks remain distinct.</p></article></li>
  <li><article class="v2-tile"><h3><a href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a></h3><p>The pinned public release context and count reconciliation surface.</p></article></li>
</ul>
