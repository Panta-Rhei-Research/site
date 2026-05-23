---
layout: program-doc
title: "Corpus"
lane: corpus
v2_lane: corpus
permalink: /corpus/
type: "Lane Root"
status: "Canonical"
summary_short: "The construction body of the theory: definitions, derivations, monographs, registry objects, TauLib projection, and dependency relations."
og_image: /assets/images/plates/plate-04-construction-spine-og.jpg
twitter_image: /assets/images/plates/plate-04-construction-spine-og.jpg
og_image_alt: "Scientific plate showing the Corpus Construction Spine as a ten-step build sequence from Kernel to Ontic Closure."
summary_cards:
  - title: "Research body"
    body: "Definitions, lemmas, theorems, structures, and dependency relations."
  - title: "Construction spine"
    body: "The public build-order narrative traces the Corpus through ten canonical construction steps."
  - title: "Public projections"
    body: "The Corpus appears through Construction Spine, Monograph Corpus, Registry, TauLib, Corpus Graph, Results, Verify, and Publications as distinct public surfaces."
hero_ctas:
  - label: "Follow the Construction Spine"
    url: /corpus/construction-spine/
    primary: true
  - label: "Open the Monograph Corpus"
    url: /corpus/monograph-corpus/
  - label: "Browse the Registry"
    url: /corpus/registry/
  - label: "How to Read"
    url: /corpus/how-to-read/
right_rail:
  related:
    - title: "Construction Spine"
      url: /corpus/construction-spine/
    - title: "Monograph Corpus"
      url: /corpus/monograph-corpus/
    - title: "Bi-Square Motif"
      url: /corpus/bi-square/
    - title: "Construction Review Packet"
      url: /corpus/foundational-hinges/
    - title: "Registry"
      url: /corpus/registry/
    - title: "Types"
      url: /corpus/types/
    - title: "How to Read"
      url: /corpus/how-to-read/
    - title: "Corpus Graph"
      url: /corpus/graph/
    - title: "TauLib"
      url: /verify/taulib/
    - title: "Versioning · Filter Rules"
      url: /verify/filter-rules/
    - title: "Public Observatory Blueprint"
      url: /publications/white-papers/building-a-public-research-observatory/
  meta:
    type: "Lane Root"
    status: "Canonical"
    updated: "May 2026"
---

## What the corpus is

{% assign registry_objects = site.data.registry.objects %}
{% assign wave3 = site.data.corpus.wave3_index %}
{% assign wave3_counts = wave3.counts %}
{% assign type_groups = registry_objects | group_by: "type" | sort: "name" %}

The Corpus is the construction body of the theory.

The Construction Spine gives the ten-step public build order.

The Monograph Corpus shows how the seven-book monograph series realizes that build order across books, parts, and chapters.

The Registry exposes atomic objects. TauLib exposes formal proof surfaces where available. The Corpus Graph exposes dependencies. Results shows what follows. Verify shows how the build can be inspected. Publications holds citable release artifacts.

For the implementation view of how Corpus, Results, Verify, Publications, and Engage are connected as public surfaces, see [Building a Public Research Observatory for High-Scope Open Research]({{ '/publications/white-papers/building-a-public-research-observatory/' | relative_url }}).

<p class="eyebrow">The build-order at a glance</p>

## The Construction Spine

{% include scientific-plate.html id="plate-04-construction-spine" class="scientific-plate--construction-spine" loading="lazy" %}

The Construction Spine is the primary human-readable route into the Corpus. It shows the build-order narrative from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure. The spine's [End-to-end construction view]({{ '/corpus/construction-spine/#end-to-end-construction-view' | relative_url }}) shows how the ten steps form a single construction chain, with each step inheriting what earlier steps have earned and handing forward what later steps need.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/construction-spine/' | relative_url }}">Open the Construction Spine</a>
  <a class="btn-ghost" href="{{ '/corpus/registry/' | relative_url }}">Explore the Registry</a>
  <a class="btn-ghost" href="{{ '/verify/taulib/' | relative_url }}">Inspect TauLib</a>
  <a class="btn-ghost" href="{{ '/verify/construction-spine-verification/' | relative_url }}">Verify the Construction Spine</a>
</div>

## Corpus Artifact Projections

<!--
  v5 next-wave W7b · IA §3.2 cross-link block.
  Source: atlas/website/v5/panta-rhei-ia-doctrine-v5.md §3.2 Corpus lane.
  Publications-class artifacts that carry or update the Corpus —
  these are not new Corpus primitives, they are projections of the
  active publication stream into the Corpus reading view.
-->

The Corpus is updated by — and connected to — the active publication stream. Publications-class artifacts that touch the Corpus appear in five projections:

<ul class="v2-grid v2-card-list">
  <li><article><a class="v2-tile" href="{{ '/publications/research-papers/' | relative_url }}"><h3>Research Papers</h3><p>Standalone scholarly papers carrying primary technical contributions — the Hinge series.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/research-notes/' | relative_url }}"><h3>Research Notes</h3><p>Shorter scholarly artifacts from the ongoing research stream — frontier responses, comparative readings.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/research-dossiers/' | relative_url }}"><h3>Research Dossiers</h3><p>Framework dossiers and translation artifacts — including <em>The Construction Spine</em> itself as a Dossier-class artifact.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/release-artifacts/' | relative_url }}"><h3>Release Artifacts</h3><p>Version, provenance, correction, manifest — the release-governance surface for Corpus snapshots.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/research-log/' | relative_url }}"><h3>Research Log</h3><p>The dated public ledger of research-stream events touching the Corpus.</p></a></article></li>
</ul>

## The τ-Kernel

{% include scientific-plate.html id="plate-10-tau-kernel" variant="thumb" class="scientific-plate--compact scientific-plate--tau-kernel" loading="lazy" %}

The τ-Kernel is the formal starting point of the construction. It is not a hidden physical substrate; it is the constrained formal core from which the Corpus begins.

## The Bi-Square Motif

{% capture bi_square_plate_caption %}The Bi-Square Motif shows the repeated categorical shape that carries the kernel through its main lifts: tower coherence on the left, spectral naturality on the right, and a pasted constraint that becomes richer at each layer.{% endcapture %}
{% include scientific-plate.html id="plate-15-bi-square-spine" variant="thumb" class="scientific-plate--compact scientific-plate--bi-square-spine" caption=bi_square_plate_caption loading="lazy" %}

The [Bi-Square Motif]({{ '/corpus/bi-square/' | relative_url }}) is the Corpus route for the repeated proof-organizing diagram behind the kernel buildup. The Construction Spine gives the build order; the bi-square gives a stable categorical shape that reappears as algebraic, geometric, enriched, and computational structure. It is a construction motif, not a second construction spine.

## Construction Steps 1-3 review packet

The first three construction steps have a dedicated reviewer packet route: eight foundational research papers plus a bundle memo, surfaced through Corpus-native gateway pages. These pages explain how the kernel is built, how core mathematics is recovered, and how self-enrichment begins. They are an orientation and stress-test packet, not a standalone Corpus collection.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/foundational-hinges/' | relative_url }}" data-umami-event="cta.review-packet" data-umami-event-location="section" data-umami-event-type="internal">Open the Review Packet</a>
  <a class="btn-ghost" href="{{ '/publications/research-papers/' | relative_url }}">Research Papers</a>
  <a class="btn-ghost" href="{{ '/verify/how-to-verify-by-role/mathematician/' | relative_url }}">Mathematician Audit Route</a>
</div>

## Corpus projections

The same construction body appears through several public projections:

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
        <h3>Construction Spine</h3>
        <p>Ten-step build order from kernel definition through ontic closure.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/monograph-corpus/' | relative_url }}">
        <h3>Monograph Corpus</h3>
        <p>Seven-book narrative projection: Book → Part → Chapter summaries with registry anchors, TauLib links, and construction-step tags.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
        <h3>Registry</h3>
        <p>Atomic object map: definitions, lemmas, propositions, theorems, remarks, axioms, constructions, corollaries.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/taulib/' | relative_url }}">
        <h3>TauLib projection</h3>
        <p>Lean&nbsp;4 formalization browser, module / declaration view, and pinned source link.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/graph/' | relative_url }}">
        <h3>Corpus Graph</h3>
        <p>Dependency and relation graph across objects, monograph exposition, results, and verification routes.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/verify/filter-rules/' | relative_url }}">
        <h3>Versioning · Filter Rules</h3>
        <p>How counts, dashboards, snapshots, and release surfaces should be read.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/results/' | relative_url }}">
        <h3>Results · Verify · Publications</h3>
        <p>Results as answer surfaces, Verify as inspection routes, Publications as the citable artifact shelf.</p>
      </a>
    </article>
  </li>
</ul>

## Orientation routes

These routes are preserved because they are useful for review, but Wave 3 treats them as construction metadata rather than top-level Corpus peers.

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/bi-square/' | relative_url }}">
        <h3>Bi-Square Motif</h3>
        <p>The repeated proof-organizing diagram shape across algebraic, geometric, enriched, and computational layers.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/foundational-hinges/' | relative_url }}">
        <h3>Construction Review Packet</h3>
        <p>The reviewer stress-test route for the first mathematical construction packet (Steps 1-3).</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/publications/research-notes/thirty-open-problems-tau-readout-surfaces/' | relative_url }}">
        <h3>Thirty Open Problems Probe</h3>
        <p>An external expressiveness probe: familiar open-problem surfaces read through the existing construction grammar as answer-shapes, not solved results.</p>
      </a>
    </article>
  </li>
</ul>

## Current state

The current registry is the public atomic projection of the corpus. The primary human-readable route into the Corpus is the [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}): the build-order narrative from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
        <h3>{% if wave3_counts.construction_steps %}{{ wave3_counts.construction_steps }}{% else %}10{% endif %} construction steps</h3>
        <p>The public build narrative that aligns Agenda obligations, Corpus construction, and Results status.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/foundational-hinges/' | relative_url }}">
        <h3>{% if wave3_counts.review_packets %}{{ wave3_counts.review_packets }}{% else %}1{% endif %} review packet</h3>
        <p>The reviewer-facing stress-test route for the mathematical packet behind Steps 1-3.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
        <h3>{% if wave3_counts.registry_public_objects %}{{ wave3_counts.registry_public_objects }}{% else %}{{ registry_objects | size }}{% endif %} public registry objects</h3>
        <p>The current public spine across all seven books.</p>
      </a>
    </article>
  </li>
  {% for group in type_groups %}
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/types/' | relative_url }}#{{ group.name | slugify }}">
        <h3>{{ group.size }} {{ group.name | capitalize }}</h3>
        <p>Registry objects currently typed as {{ group.name }}.</p>
      </a>
    </article>
  </li>
  {% endfor %}
</ul>

## What the Corpus is not

- not a claim list; see [Results]({{ '/results/' | relative_url }});
- not the citable artifact shelf; see [Publications]({{ '/publications/' | relative_url }});
- not the proof assistant itself; see [TauLib]({{ '/verify/taulib/' | relative_url }}) and [Verify]({{ '/verify/' | relative_url }});
- not a frozen release; citable snapshots and release artifacts live in [Publications]({{ '/publications/' | relative_url }});
- not a replacement for verification; see [Verify]({{ '/verify/' | relative_url }}).

## Structure

<div class="v2-system-strip" aria-label="Corpus structure">
  <a href="{{ '/corpus/construction-spine/' | relative_url }}">Construction step</a>
  <span>-></span>
  <a href="{{ '/corpus/monograph-corpus/' | relative_url }}">Monograph part/chapter</a>
  <span>-></span>
  <a href="{{ '/corpus/registry/' | relative_url }}">Registry object</a>
  <span>-></span>
  <a href="{{ '/corpus/graph/' | relative_url }}">Dependency relation</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Result surface</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verify route</a>
  <span>-></span>
  <a href="{{ '/publications/' | relative_url }}">Publication artifact</a>
</div>

The Corpus lane is the place to ask: what has actually been built, how does one item depend on another, and where does a public result touch the underlying research body?

## Frequently asked

A focused subset of FAQ entries on what the Corpus actually is, how to cite it, what's in the Registry vs TauLib, and why count drift matters.

{% include faqs/faq-list.html ids="FAQ-OR-003,FAQ-TC-015,FAQ-TC-014,FAQ-JD-008" %}

<p class="muted-note"><a href="{{ '/faq/' | relative_url }}">All 73 FAQ entries →</a></p>
