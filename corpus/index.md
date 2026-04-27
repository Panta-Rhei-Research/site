---
layout: program-doc
title: "Corpus"
lane: corpus
v2_lane: corpus
permalink: /corpus/
type: "Lane Root"
status: "Canonical"
summary_short: "The living, versioned research corpus of the program."
og_image: /assets/images/plates/plate-04-construction-spine-og.jpg
twitter_image: /assets/images/plates/plate-04-construction-spine-og.jpg
og_image_alt: "Scientific plate showing the Corpus Construction Spine as a ten-step build sequence from Kernel to Ontic Closure."
summary_cards:
  - title: "Research body"
    body: "Definitions, lemmas, theorems, structures, and dependency relations."
  - title: "Construction spine"
    body: "The public build-order narrative traces the Corpus through ten canonical construction steps."
  - title: "Public projections"
    body: "Results, publications, verification, and TauLib are projections of the corpus."
hero_ctas:
  - label: "Follow the Construction Spine"
    url: /corpus/construction-spine/
    primary: true
  - label: "Browse the Registry"
    url: /corpus/registry/
  - label: "How to Read"
    url: /corpus/how-to-read/
right_rail:
  related:
    - title: "Construction Spine"
      url: /corpus/construction-spine/
    - title: "Registry"
      url: /corpus/registry/
    - title: "Types"
      url: /corpus/types/
    - title: "How to Read"
      url: /corpus/how-to-read/
    - title: "Corpus Graph"
      url: /corpus/graph/
  meta:
    type: "Lane Root"
    status: "Canonical"
    updated: "April 2026"
---

## What the corpus is

{% assign registry_objects = site.data.registry.objects %}
{% assign type_groups = registry_objects | group_by: "type" | sort: "name" %}

The corpus is the central research artifact of the program.

It is not a summary, not a set of claims, and not a collection of papers. It is the structured body of what has been built: definitions, lemmas, theorems, structures, derivations, and dependency relations.

<p class="eyebrow">The build-order at a glance</p>

## The Construction Spine

{% include scientific-plate.html id="plate-04-construction-spine" class="scientific-plate--construction-spine" loading="lazy" %}

The Construction Spine is the primary human-readable route into the Corpus. It shows the build-order narrative from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

<div class="btn-group section-ctas">
  <a class="btn-secondary" href="{{ '/corpus/construction-spine/' | relative_url }}">Open the Construction Spine</a>
  <a class="btn-ghost" href="{{ '/corpus/registry/' | relative_url }}">Explore the Registry</a>
  <a class="btn-ghost" href="{{ '/verify/taulib/' | relative_url }}">Inspect TauLib</a>
  <a class="btn-ghost" href="{{ '/verify/construction-spine-verification/' | relative_url }}">Verify the Construction Spine</a>
</div>

## Current state

The current registry is the public atomic projection of the corpus. The primary human-readable route into the Corpus is the [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}): the build-order narrative from kernel definition through mathematics, physics, life, reflective structure, self-hosting, and ontic closure.

<ul class="v2-grid v2-card-list">
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}">
        <h3>10 construction steps</h3>
        <p>The public build narrative that aligns Agenda obligations, Corpus construction, and Results status.</p>
      </a>
    </article>
  </li>
  <li>
    <article>
      <a class="v2-tile" href="{{ '/corpus/registry/' | relative_url }}">
        <h3>{{ registry_objects | size }} registry objects</h3>
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

## What the corpus is not

- not a narrative exposition; see [Publications]({{ '/publications/' | relative_url }})
- not a list of answer claims; see [Results]({{ '/results/' | relative_url }})
- not the proof assistant itself; see [Verify]({{ '/verify/' | relative_url }}) and TauLib
- not static

## Corpus projections

The corpus is expressed in multiple public forms:

- [Construction Spine]({{ '/corpus/construction-spine/' | relative_url }}) — human-readable build narrative
- [Registry]({{ '/corpus/registry/' | relative_url }}) — human-readable formal spine
- [Publications]({{ '/publications/' | relative_url }}) — narrative crystallizations
- [Results]({{ '/results/' | relative_url }}) — answer surfaces
- [Verify]({{ '/verify/' | relative_url }}) — formal and empirical inspection paths

## Structure

<div class="v2-system-strip" aria-label="Corpus structure">
  <a href="{{ '/corpus/construction-spine/' | relative_url }}">Construction steps</a>
  <span>-></span>
  <a href="{{ '/corpus/registry/' | relative_url }}">Atomic items</a>
  <span>-></span>
  <a href="{{ '/corpus/graph/' | relative_url }}">Dependencies</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Result projections</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verification</a>
  <span>-></span>
  <a href="{{ '/publications/' | relative_url }}">Release artifacts</a>
</div>

The Corpus lane is the place to ask: what has actually been built, how does one item depend on another, and where does a public result touch the underlying research body?
