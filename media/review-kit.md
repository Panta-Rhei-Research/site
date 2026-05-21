---
layout: program-doc
title: "Review Kit"
permalink: /media/review-kit/
lane: support
type: support_page
support_type: media
status: canonical
last_updated: 2026-05-09
updated: "May 2026"
summary: "A bounded-question kit for editors and journalists routing claims to expert reviewers — which expert to call for which claim layer, and the bounded first question to ask them."
summary_short: "Bounded-question kit: which expert reviews which claim layer, and the first question to ask them."
summary_cards:
- title: "For editors and journalists"
  body: "Use this when a story angle requires an expert quote. Each entry gives a candidate expert type and a bounded first question they can actually answer with their discipline's tools."
- title: "Not a peer review surface"
  body: "Expert handoff is preparation for review, not a substitute for it. The Review Kit helps you route the right question to the right expert; the expert's answer is what counts."
- title: "Sourced from corpus/faqs/"
  body: "All entries below are canonical FAQ entities (FAQ-EH-* and selected FAQ-TC-*) from the corpus repo. Stable IDs let you cite individual entries."
right_rail:
  related:
  - title: "Media Kit"
    url: /media/
  - title: "Journalist FAQ"
    url: /media/journalist-faq/
  - title: "Expert Handoff FAQ"
    url: /faq/expert-handoff/
  - title: "Technical Credibility FAQ"
    url: /faq/technical-credibility/
  - title: "How to Verify"
    url: /verify/how-to-verify/
  - title: "How to Verify by Reviewer Role"
    url: /verify/how-to-verify-by-role/
  - title: "Assessment Protocols"
    url: /verify/assessment-protocols/
  meta:
    type: "Support page"
    scope: "Review Kit — expert handoff packets"
    status: "Canonical"
    updated: "May 2026"
---

## How to use this page

The Review Kit is for editors, journalists, podcast hosts, and institutional readers who need to route a claim to an expert reviewer. The pattern is: pick the layer of claim that matters (formalization? physics derivation? life-domain bridge?), find the suggested expert type, and ask them the **bounded first question** below. That question is one they can answer with their own discipline's tools — without first learning the entire τ-framework.

This is preparation for review, not a substitute for review. The expert's answer is what counts. The Review Kit just helps you put the question in front of the right reader.

## Expert handoff

All 16 entries from the canonical Expert Handoff layer of the FAQ. Each entry surfaces a candidate expert type and a bounded first question to ask them.

{%- comment -%}
  HF-04-v2 (polish wave) · expand the first Expert Handoff entry so a
  reviewer arriving here sees a real answer immediately.
{%- endcomment -%}
{% include faqs/faq-list.html layer=4 expand_first="true" %}

## Technical credibility (selected)

Subset of Technical Credibility FAQ entries that pair with expert handoff: what TauLib actually proves, the role of `sorry` and custom axioms, the trust budget, and what's currently bridge-pending.

{% include faqs/faq-list.html ids="FAQ-TC-001,FAQ-TC-002,FAQ-TC-005,FAQ-TC-008,FAQ-TC-010,FAQ-TC-015,FAQ-TC-017,FAQ-TC-018" %}

{%- comment -%}
  AUD-30 · Deep-link into the canonical FAQ filtered for reviewers.
  The /faq/?audience=reviewer query param triggers the audience-
  filter chips on the canonical FAQ page, surfacing only entries
  whose audience array includes "reviewer" — collapses the
  overlapping surfaces (First-Contact / Journalist / Review Kit /
  Media Kit) onto a single canonical directory with filtered views.
{%- endcomment -%}
<p class="audience-filter-cta">
  <a class="btn-secondary" href="{{ '/faq/?audience=reviewer' | relative_url }}">Open all reviewer FAQs in the canonical directory →</a>
</p>
<p class="muted-note"><a href="{{ '/faq/technical-credibility/' | relative_url }}">All {{ site.data.faqs.technical_credibility.faqs.size }} Technical Credibility entries →</a></p>

## Adjacent surfaces

- [How to Verify by Reviewer Role]({{ '/verify/how-to-verify-by-role/' | relative_url }}) — per-role inspection routes (mathematician, physicist, life-sciences reviewer, philosopher, formal-methods reviewer)
- [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) — manual + LLM-assisted protocols for structured critique
- [Custom Axioms]({{ '/verify/custom-axioms/' | relative_url }}) and [TCB Disclosure]({{ '/verify/tcb/' | relative_url }}) — the trust budget that scopes any formal-methods review
- [TauLib]({{ '/verify/taulib/' | relative_url }}) — the Lean 4 formalization surface

## Source-of-truth discipline

> The Corpus owns the FAQ entities. The website renders FAQ projections.

Every entry above is mirrored from `corpus/faqs/expert_handoff.yml` and `corpus/faqs/technical_credibility.yml`. Edits land in the corpus repo first, then sync into this site. Each entry has a stable ID (`FAQ-EH-###`, `FAQ-TC-###`) that you can cite directly when corresponding with an expert.

## Contact

- **Press / interview routing**: [press@panta-rhei.site](mailto:press@panta-rhei.site)
- **Structured review / technical inspection**: [review@panta-rhei.site](mailto:review@panta-rhei.site)
- **Errata & corrections**: [errata@panta-rhei.site](mailto:errata@panta-rhei.site)
