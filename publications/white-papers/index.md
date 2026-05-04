---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
updated: "May 2026"
title: "White Papers"
permalink: "/publications/white-papers/"
type: "Publication Category"
summary_short: "Structured explanatory artifacts for framework, formalization, infrastructure, method, and verification context."
og_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
twitter_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
og_image_alt: "Scientific plate showing White Papers as one category inside the Publications artifact taxonomy."
---

## White Papers

White Papers are structured explanatory artifacts.

They clarify the framework, formalization, research infrastructure, verification architecture, methodology, or public research system. White Papers may be overview-oriented or technical.

<div class="notice note"><strong>Category boundary.</strong> This White Paper category is explanatory. It clarifies framework structure, implementation, method, or verification context; it is not by itself a primary research result.</div>

## White Papers inside the publication taxonomy

{% capture white_papers_plate_caption %}White Papers are explanatory artifacts in the stable publication layer. They clarify framework, formalization, infrastructure, methodology, or verification context without primarily carrying new original research claims.{% endcapture %}
{% include scientific-plate.html id="plate-07-stable-artifact-layer" variant="thumb" class="scientific-plate--compact" caption=white_papers_plate_caption loading="lazy" %}

White Papers belong to Publications because they are stable citable artifacts. Their purpose is explanatory: to clarify how the framework, infrastructure, method, or verification architecture should be read.

## White paper types

- Overview White Papers
- Technical White Papers
- Formalization White Papers
- Infrastructure White Papers
- Verification White Papers
- Architecture White Papers
- Methodology White Papers
- Orientation White Papers

## Released

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/publications/white-papers/executive-overview/' | relative_url }}">
        <span class="chip" style="font-size: 0.72rem;">Overview · Public-outreach</span>
        <h3>Panta Rhei Research Program — Executive Overview</h3>
        <p><em>A 30-minute review route for a 30-minute first-contact reader.</em> v4.0, May 2026. The door, not the proof — routing readers from a single entry point to Corpus, Verify, and Publications surfaces.</p>
      </a>
      <p class="hero-meta"><a href="{{ '/assets/pdfs/white-papers/white-paper-2026-05-04-panta-rhei-executive-overview.pdf' | relative_url }}">PDF (≈ 230 KB)</a></p>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/publications/white-papers/taulib/' | relative_url }}">
        <span class="chip" style="font-size: 0.72rem;">Technical · Formalization</span>
        <h3>TauLib: A Self-Contained Lean 4 Library for Category τ</h3>
        <p><em>Kernel + Mathlib Bridges + Registry-Driven Correspondence.</em> v2.0, May 2026. The formalization white paper for the τ-kernel — 4,863 theorems and lemmas, 0 sorry, 3 disclosed custom axioms (Book III).</p>
      </a>
      <p class="hero-meta"><a href="{{ '/assets/pdfs/white-papers/white-paper-2026-05-01-taulib-self-contained-lean-4-library.pdf' | relative_url }}">PDF (≈ 210 KB)</a> · <a href="https://doi.org/10.5281/zenodo.19976503">DOI 10.5281/zenodo.19976503</a></p>
    </article>
  </li>
</ul>

## Adjacent overview artifacts

- [Framework Conspectus]({{ '/publications/conspectus/' | relative_url }}) — Overview White Paper (lighter touch than the Executive Overview).
- Corpus Pipeline — Infrastructure White Paper, planned.
- Verification Stack Overview — Verification White Paper, routed through [Verify]({{ '/verify/' | relative_url }}).
