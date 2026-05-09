---
layout: program-doc
title: "Expert Handoff — FAQ"
permalink: /faq/expert-handoff/
lane: support
shell: home
type: support_page
support_type: faq
status: canonical
last_updated: 2026-05-09
updated: "May 2026"
summary: "Layer 4 — which expert to call, what packet to send, and what bounded question to ask."
summary_short: "Layer 4 — expert-handoff questions: which expert, what packet, what bounded question."
right_rail:
  related:
  - title: All FAQ
    url: /faq/
  - title: Technical Credibility
    url: /faq/technical-credibility/
  - title: Review Kit
    url: /media/review-kit/
  - title: Assessment Protocols
    url: /verify/assessment-protocols/
  - title: How to Verify by Role
    url: /verify/how-to-verify-by-role/
  meta:
    type: "Support page"
    scope: "FAQ — Layer 4 Expert Handoff"
    status: "Canonical"
    updated: "May 2026"
---

{% include faqs/faq-layer-nav.html current_layer=4 %}

<section class="faq-layer-intro" aria-labelledby="faq-layer-intro-heading">
  <h2 id="faq-layer-intro-heading">Layer 4 · Expert Handoff</h2>
  <p>{{ site.data.faqs.expert_handoff.layer.description }}</p>
  <p class="muted-note">{{ site.data.faqs.expert_handoff.faqs.size }} entries · last reviewed {{ site.data.faqs.expert_handoff.last_reviewed }} · version {{ site.data.faqs.expert_handoff.version }}</p>
  <p>Each entry below identifies a candidate expert type and a <strong>bounded first question</strong> to ask them — the question they can actually answer with their own discipline's tools, not the program's full claim set.</p>
</section>

{% include faqs/faq-list.html layer=4 style="accordion" %}

## Read next

- [Technical Credibility]({{ '/faq/technical-credibility/' | relative_url }}) — Layer 3: TauLib, Lean, custom axioms
- [Review Kit]({{ '/media/review-kit/' | relative_url }}) — expert-handoff packets ready to send
- [Assessment Protocols]({{ '/verify/assessment-protocols/' | relative_url }}) — manual + LLM-assisted protocols
- [How to Verify by Reviewer Role]({{ '/verify/how-to-verify-by-role/' | relative_url }}) — per-role inspection routes

{% include faqs/faq-jsonld.html layer=4 %}
