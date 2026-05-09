---
layout: program-doc
title: "First Orientation — FAQ"
permalink: /faq/first-orientation/
lane: support
shell: home
type: support_page
support_type: faq
status: canonical
last_updated: 2026-05-09
updated: "May 2026"
summary: "Layer 1 — first 1–3 minute orientation. Where to start, lanes, Corpus, Results, master constant, failure paths."
summary_short: "Layer 1 — first 1–3 minute orientation for the program."
right_rail:
  related:
  - title: All FAQ
    url: /faq/
  - title: First Contact
    url: /faq/first-contact/
  - title: Discover
    url: /discover/
  - title: Corpus
    url: /corpus/
  meta:
    type: "Support page"
    scope: "FAQ — Layer 1 First Orientation"
    status: "Canonical"
    updated: "May 2026"
---

{% include faqs/faq-layer-nav.html current_layer=1 %}

<section class="faq-layer-intro" aria-labelledby="faq-layer-intro-heading">
  <h2 id="faq-layer-intro-heading">Layer 1 · First Orientation</h2>
  <p>{{ site.data.faqs.first_orientation.layer.description }}</p>
  <p class="muted-note">{{ site.data.faqs.first_orientation.faqs.size }} entries · last reviewed {{ site.data.faqs.first_orientation.last_reviewed }} · version {{ site.data.faqs.first_orientation.version }}</p>
</section>

{% include faqs/faq-list.html layer=1 style="accordion" %}

## Read next

- [First Contact]({{ '/faq/first-contact/' | relative_url }}) — Layer 0: credibility filter
- [Journalist Due Diligence]({{ '/faq/journalist-due-diligence/' | relative_url }}) — Layer 2
- [Technical Credibility]({{ '/faq/technical-credibility/' | relative_url }}) — Layer 3
- [Discover]({{ '/discover/' | relative_url }}) — guided first-contact entry into the program

{% include faqs/faq-jsonld.html layer=1 %}
