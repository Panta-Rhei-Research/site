---
layout: program-doc
title: "Corpus"
lane: corpus
v2_lane: corpus
permalink: /corpus/
type: "Lane Root"
status: "Canonical"
summary_short: "The inspectable construction body of the program: build steps, operational map, Registry graph, and TauLib projection."
og_image: /assets/images/plates/plate-04-construction-spine-og.jpg
twitter_image: /assets/images/plates/plate-04-construction-spine-og.jpg
og_image_alt: "Scientific plate showing the Corpus Construction Spine as a ten-step build sequence from Kernel to Ontic Closure."
summary_cards:
  - title: "Construction Spine"
    body: "Ten build obligations from kernel to ontic closure."
  - title: "Construction Map"
    body: "Seventy-nine monograph parts as the operational build sequence."
  - title: "Registry Graph"
    body: "Atomic objects, dependencies, downstream uses, and projection links."
  - title: "TauLib"
    body: "The compiled Lean projection of the Corpus."
hero_ctas:
  - label: "Follow the Construction Spine"
    url: /corpus/construction-spine/
    primary: true
  - label: "Open the Construction Map"
    url: /corpus/construction-map/
  - label: "Explore the Registry Graph"
    url: /corpus/graph/
  - label: "Open TauLib"
    url: /corpus/taulib/
right_rail:
  related:
    - title: "Construction Spine"
      url: /corpus/construction-spine/
    - title: "Construction Map"
      url: /corpus/construction-map/
    - title: "Foundational Hinges"
      url: /corpus/foundational-hinges/
    - title: "Monograph Drilldown"
      url: /corpus/monographs/
    - title: "Registry Graph"
      url: /corpus/graph/
    - title: "TauLib"
      url: /corpus/taulib/
  meta:
    type: "Lane Root"
    status: "Canonical"
    updated: "April 2026"
---

## What the corpus is

{% assign registry_objects = site.data.registry.objects %}
{% assign construction_map = site.data.construction_map["construction-map"] %}
{% assign taulib_summary = site.data.taulib.summary %}

The Corpus is the construction lane: the public body of what has been built. It is not the full prose of the books, not a list of answer claims, and not the verification argument itself. It is the inspectable research body: build order, operational part sequence, atomic dependencies, and the compiled Lean projection.

The v3.0 Corpus lane has four entry modes.

<ul class="v2-grid v2-card-list corpus-entry-modes">
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/corpus/construction-spine/' | relative_url }}">Construction Spine</a></h3>
      <p>Ten logical build obligations: kernel, mathematics, physics, life, reflection, self-hosting, and ontic closure.</p>
      <p><strong>Use it when:</strong> you want the high-level sequence of what must be built.</p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/corpus/construction-map/' | relative_url }}">Construction Map</a></h3>
      <p>{{ construction_map | size }} monograph parts recast as construction units with summaries, chapter links, Registry anchors, and TauLib links.</p>
      <p><strong>Use it when:</strong> you want the operational build without reading full book prose.</p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/corpus/graph/' | relative_url }}">Registry Graph</a></h3>
      <p>{{ registry_objects | size }} atomic objects, dependency edges, downstream uses, and links into monograph and formalization projections.</p>
      <p><strong>Use it when:</strong> you want to inspect one object and move through its dependency neighborhood.</p>
    </article>
  </li>
  <li>
    <article class="v2-tile">
      <h3><a href="{{ '/corpus/taulib/' | relative_url }}">TauLib</a></h3>
      <p>{{ taulib_summary.module_count | default: "Current" }} Lean modules published as the compiled Lean projection of the Corpus.</p>
      <p><strong>Use it when:</strong> you want the formalization inventory, module docs, and Corpus-to-Lean anchor map.</p>
    </article>
  </li>
</ul>

## Construction Spine

{% include scientific-plate.html id="plate-04-construction-spine" class="scientific-plate--construction-spine" loading="lazy" %}

The Construction Spine is the first read: ten obligations in logical order. It says what the Corpus must build, not when a task happened historically.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/construction-spine/' | relative_url }}">Open the Construction Spine</a>
  <a class="btn-ghost" href="{{ '/verify/construction-spine-verification/' | relative_url }}">Inspect the obligations</a>
</div>

## Construction Map

The Construction Map is the second read: the 79 parts of the seven monographs as a sequential construction route. The books remain the full prose artifacts; the website exposes the stripped construction body: part summaries, chapter navigation, Registry anchors, TauLib links, and previous/next part movement across book boundaries.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/construction-map/' | relative_url }}">Open the 79-part Construction Map</a>
  <a class="btn-ghost" href="{{ '/corpus/monographs/' | relative_url }}">Book/part/chapter drilldown</a>
</div>

## Registry Graph

The Registry is the atomic projection of the Corpus. The graph view lets reviewers start from an object, inspect upstream dependencies and downstream uses, and jump into the monograph part, Construction Map layer, TauLib modules, Results, or Verify surfaces where mappings exist.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/graph/' | relative_url }}">Explore the Registry Graph</a>
  <a class="btn-ghost" href="{{ '/corpus/registry/' | relative_url }}">Registry overview</a>
</div>

## TauLib

TauLib is Corpus-owned: it is the compiled Lean projection of the Corpus. Verify still owns the semantic questions: what the formalization covers, what the formal terms mean, where bridge assumptions hold, and what remains externally assessable.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/taulib/' | relative_url }}">Open Corpus TauLib</a>
  <a class="btn-ghost" href="{{ '/verify/taulib/' | relative_url }}">TauLib inspection bridge</a>
  <a class="btn-ghost" href="{{ '/verify/release-manifest/' | relative_url }}">Release Manifest</a>
</div>

## What the corpus is not

- not the full book prose; see [Research Monographs]({{ '/publications/research-monographs/' | relative_url }})
- not a list of answer claims; see [Results]({{ '/results/' | relative_url }})
- not final verification or external acceptance; see [Verify]({{ '/verify/' | relative_url }})
- not a reduced page count; the Corpus is allowed to be large because it is the research body
