---
layout: program-doc
title: "First Contact — FAQ"
permalink: /faq/first-contact/
lane: support
shell: home
type: support_page
support_type: faq
status: canonical
last_updated: 2026-05-09
updated: "May 2026"
summary: "Layer 0 — immediate credibility filter for first-time readers. What is this, is it proven, is it peer-reviewed, who is behind it."
summary_short: "Layer 0 — immediate credibility-filter questions for first-time readers."
right_rail:
  related:
  - title: All FAQ
    url: /faq/
  - title: Discover
    url: /discover/
  - title: First Orientation
    url: /faq/first-orientation/
  - title: Journalist FAQ
    url: /media/journalist-faq/
  meta:
    type: "Support page"
    scope: "FAQ — Layer 0 First Contact"
    status: "Canonical"
    updated: "May 2026"
---

{% include faqs/faq-layer-nav.html current_layer=0 %}

<section class="faq-layer-intro" aria-labelledby="faq-layer-intro-heading">
  <h2 id="faq-layer-intro-heading">Layer 0 · First Contact</h2>
  <p>{{ site.data.faqs.first_contact.layer.description }}</p>
  <p class="muted-note">{{ site.data.faqs.first_contact.faqs.size }} entries · last reviewed {{ site.data.faqs.first_contact.last_reviewed }} · version {{ site.data.faqs.first_contact.version }}</p>
</section>

{% include faqs/faq-list.html layer=0 style="accordion" %}

## Read next

- [First Orientation]({{ '/faq/first-orientation/' | relative_url }}) — Layer 1: where to start, lanes, Corpus, Results
- [Journalist Due Diligence]({{ '/faq/journalist-due-diligence/' | relative_url }}) — Layer 2: coverage questions for editors and reporters
- [Technical Credibility]({{ '/faq/technical-credibility/' | relative_url }}) — Layer 3: TauLib, Lean, custom axioms

{% include faqs/faq-jsonld.html layer=0 %}
