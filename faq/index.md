---
layout: program-doc
title: "Frequently Asked Questions"
permalink: /faq/
lane: support
shell: home
type: support_page
support_type: faq
status: canonical
last_updated: 2026-05-09
updated: "May 2026"
summary: "First-contact, journalist, technical, and expert-handoff questions about the Panta Rhei Research Program."
summary_short: "Public-epistemic FAQ infrastructure: 73 structured entries across 5 layers — what to believe, what not to believe, where inspection begins, and which expert reviews which claim layer."
right_rail:
  related:
  - title: Discover
    url: /discover/
  - title: Verify
    url: /verify/
  - title: Journalist FAQ
    url: /media/journalist-faq/
  - title: Review Kit
    url: /media/review-kit/
  meta:
    type: "Support page"
    scope: "Public FAQ"
    status: "Canonical"
    updated: "May 2026"
---

{%- comment -%}
  Sum entries across all five FAQ layer files. Liquid for-loops do NOT accept
  inline filters on the iterable expression — applying `| split: ","` directly
  to the for-loop's iterable is a syntax error and silently leaves the
  iteration empty (the cause of the /faq/ page showing "0 entries" instead of
  73). Assign the split result first, then iterate over the named array.
{%- endcomment -%}
{% assign all_entries_count = 0 %}
{% assign faq_layer_files = "first_contact,first_orientation,journalist_due_diligence,technical_credibility,expert_handoff" | split: "," %}
{% for fname in faq_layer_files %}
  {% assign coll = site.data.faqs[fname] %}
  {% if coll and coll.faqs %}
    {% assign all_entries_count = all_entries_count | plus: coll.faqs.size %}
  {% endif %}
{% endfor %}

<section class="faq-intro" aria-labelledby="faq-intro-heading">
  <h2 id="faq-intro-heading">Public-epistemic FAQ infrastructure</h2>
  <p>FAQ records are <strong>Corpus entities</strong> rendered here as public projections. The corpus repository owns the structured records; this page and the five layer pages render them as a navigable directory.</p>
  <p class="faq-intro-totals">
    <span class="faq-totals-chip"><strong>{{ all_entries_count }}</strong> entries</span>
    <span class="faq-totals-chip"><strong>5</strong> layers</span>
    <span class="faq-totals-chip">Source: <code>corpus/faqs/</code></span>
  </p>
</section>

{% include faqs/faq-layer-nav.html current_layer="index" %}

<section class="faq-layer-cards" aria-labelledby="faq-layer-cards-heading">
  <h2 id="faq-layer-cards-heading">FAQ layers</h2>
  <ul class="faq-layer-card-grid" role="list">
    <li class="faq-layer-card faq-layer-card-fc">
      <a href="{{ '/faq/first-contact/' | relative_url }}">
        <p class="faq-layer-card-eyebrow">Layer 0 · {{ site.data.faqs.first_contact.faqs.size }} entries</p>
        <h3>First Contact</h3>
        <p>Immediate credibility filter — what is this, is it proven, peer-reviewed, who is behind it.</p>
        <span class="faq-layer-card-cta">Open layer →</span>
      </a>
    </li>
    <li class="faq-layer-card faq-layer-card-or">
      <a href="{{ '/faq/first-orientation/' | relative_url }}">
        <p class="faq-layer-card-eyebrow">Layer 1 · {{ site.data.faqs.first_orientation.faqs.size }} entries</p>
        <h3>First Orientation</h3>
        <p>Where to start, lanes, Corpus, Results, master constant, failure paths — your first 1–3 minute read.</p>
        <span class="faq-layer-card-cta">Open layer →</span>
      </a>
    </li>
    <li class="faq-layer-card faq-layer-card-jd">
      <a href="{{ '/faq/journalist-due-diligence/' | relative_url }}">
        <p class="faq-layer-card-eyebrow">Layer 2 · {{ site.data.faqs.journalist_due_diligence.faqs.size }} entries</p>
        <h3>Journalist / Editor Due Diligence</h3>
        <p>What to write, avoid, link, and cite. Which experts to call and what bounded question to give them.</p>
        <span class="faq-layer-card-cta">Open layer →</span>
      </a>
    </li>
    <li class="faq-layer-card faq-layer-card-tc">
      <a href="{{ '/faq/technical-credibility/' | relative_url }}">
        <p class="faq-layer-card-eyebrow">Layer 3 · {{ site.data.faqs.technical_credibility.faqs.size }} entries</p>
        <h3>Technical Credibility</h3>
        <p>TauLib, Lean, Release Manifest, <code>sorry</code>, custom axioms, TCB, Mathlib, build reproduction.</p>
        <span class="faq-layer-card-cta">Open layer →</span>
      </a>
    </li>
    <li class="faq-layer-card faq-layer-card-eh">
      <a href="{{ '/faq/expert-handoff/' | relative_url }}">
        <p class="faq-layer-card-eyebrow">Layer 4 · {{ site.data.faqs.expert_handoff.faqs.size }} entries</p>
        <h3>Expert Handoff</h3>
        <p>Which expert to call, what packet to send, and what bounded question to ask.</p>
        <span class="faq-layer-card-cta">Open layer →</span>
      </a>
    </li>
  </ul>
</section>

<section class="faq-section" aria-labelledby="faq-featured-heading">
  <h2 id="faq-featured-heading">Five-minute orientation</h2>
  <p class="muted-note">A short, ordered route into the program for first-time readers.</p>
  {% include faqs/faq-list.html ids="FAQ-FC-001,FAQ-FC-002,FAQ-FC-003,FAQ-OR-001,FAQ-OR-002" style="accordion" show_layer_label="true" %}
</section>

<section class="faq-section" aria-labelledby="faq-all-heading">
  <h2 id="faq-all-heading">All FAQ entries — by layer</h2>
  <p class="muted-note">All {{ all_entries_count }} entries across 5 layers, sorted by layer and priority. Click any question to expand the full answer.</p>
  {% include faqs/faq-list.html style="accordion" show_layer_label="true" %}
</section>

## Source-of-truth discipline

> The Corpus owns the FAQ entities. The website renders FAQ projections.

The 73 entries above are mirrored from the [corpus FAQ entity collection](https://github.com/Panta-Rhei-Research/corpus/tree/main/faqs). Edits land in the corpus repo first, then sync into this site via `scripts/sync_faqs_from_corpus.py`. Each entry has a stable ID (`FAQ-FC-###`, `FAQ-OR-###`, `FAQ-JD-###`, `FAQ-TC-###`, `FAQ-EH-###`) that never changes once published; retired entries get `status: retired` rather than being deleted.

## See also

- [Discover]({{ '/discover/' | relative_url }}) — guided first-contact entry into the program
- [Verify]({{ '/verify/' | relative_url }}) — verification framework, formalization, release manifest
- [Journalist FAQ]({{ '/media/journalist-faq/' | relative_url }}) — coverage-specific subset
- [Review Kit]({{ '/media/review-kit/' | relative_url }}) — expert-handoff packets

{% include faqs/faq-jsonld.html %}
