---
layout: program-doc
title: "Technical Credibility — FAQ"
permalink: /faq/technical-credibility/
lane: support
shell: home
type: support_page
support_type: faq
status: canonical
last_updated: 2026-05-09
updated: "May 2026"
summary: "Layer 3 — TauLib, Lean, Release Manifest, sorry, custom axioms, TCB, Mathlib, build reproduction."
summary_short: "Layer 3 — technical credibility questions: TauLib, Lean, custom axioms, build reproduction."
right_rail:
  related:
  - title: All FAQ
    url: /faq/
  - title: Verify
    url: /verify/
  - title: TauLib
    url: /verify/taulib/
  - title: Release Manifest
    url: /verify/release-manifest/
  - title: Expert Handoff
    url: /faq/expert-handoff/
  meta:
    type: "Support page"
    scope: "FAQ — Layer 3 Technical Credibility"
    status: "Canonical"
    updated: "May 2026"
---

{% include faqs/faq-layer-nav.html current_layer=3 %}

<section class="faq-layer-intro" aria-labelledby="faq-layer-intro-heading">
  <h2 id="faq-layer-intro-heading">Layer 3 · Technical Credibility</h2>
  <p>{{ site.data.faqs.technical_credibility.layer.description }}</p>
  <p class="muted-note">{{ site.data.faqs.technical_credibility.faqs.size }} entries · last reviewed {{ site.data.faqs.technical_credibility.last_reviewed }} · version {{ site.data.faqs.technical_credibility.version }}</p>
</section>

{% include faqs/faq-list.html layer=3 style="accordion" %}

## Read next

- [Expert Handoff]({{ '/faq/expert-handoff/' | relative_url }}) — Layer 4: which expert to call, what packet to send
- [Verify]({{ '/verify/' | relative_url }}) — verification framework, formalization stack, release manifest
- [TauLib]({{ '/verify/taulib/' | relative_url }}) — formalization status surface
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — current quantitative facts
- [How to Verify]({{ '/verify/how-to-verify/' | relative_url }}) — by reviewer role

{% include faqs/faq-jsonld.html layer=3 %}
