---
layout: program-doc
title: "Corpus Graph"
lane: corpus
v2_lane: corpus
permalink: /corpus/graph/
type: "Corpus Guide"
status: "Draft"
summary_short: "A conceptual map of how registry objects, dependencies, results, publications, and verification surfaces relate."
summary_cards:
  - title: "Graph, not list"
    body: "The registry is most useful when read as dependencies and projections, not as a flat catalog."
  - title: "Bidirectional"
    body: "Each object can be read backward through prerequisites and forward through uses."
  - title: "Projection-aware"
    body: "Results, publications, and TauLib are public projections of the same corpus spine."
right_rail:
  related:
    - title: "Registry"
      url: /corpus/registry/
    - title: "How to Read"
      url: /corpus/how-to-read/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Corpus Guide"
    status: "Draft"
    updated: "April 2026"
---

## Conceptual graph

{% assign graph_index = site.data.corpus.graph_index.graph_index %}

<div class="v2-system-strip" aria-label="Corpus graph model">
  <a href="{{ '/corpus/registry/' | relative_url }}">Registry object</a>
  <span>-></span>
  <a href="{{ '/corpus/graph/' | relative_url }}">Dependencies</a>
  <span>-></span>
  <a href="{{ '/results/' | relative_url }}">Results</a>
  <span>-></span>
  <a href="{{ '/publications/' | relative_url }}">Publications</a>
  <span>-></span>
  <a href="{{ '/verify/' | relative_url }}">Verification</a>
</div>

## What the graph should answer

The graph exists to answer practical review questions:

- Which definitions does this theorem depend on?
- Which later results use this object?
- Which public result is anchored by this registry item?
- Which publication states the argument narratively?
- Which Lean module, if any, formalizes the relevant layer?
- Which version or release manifest fixes the current public state?

## Current data-backed projection

The current page remains a conceptual surface, but Wave 3 now publishes the underlying graph projection data from Corpus.

{% if graph_index %}
- Object inventory: `{{ graph_index.objects }}`
- Dependency adjacency: `{{ graph_index.adjacency }}`
- Reverse dependency adjacency: `{{ graph_index.reverse_adjacency }}`
- Dependency nodes: `{{ graph_index.dependency_nodes }}`
- Reverse dependency nodes: `{{ graph_index.reverse_dependency_nodes }}`
{% else %}
A later implementation can render an interactive dependency explorer from `_data/registry/adjacency.json`, `_data/registry/reverse-adjacency.json`, and `_data/registry/objects.json`.
{% endif %}

This sprint does not turn the graph into a full interactive UI. It makes the data contract explicit so later visual or query surfaces have a stable Corpus-owned source.

## Corpus v3 — live graph stats

{% assign cidx = site.data.corpus_v3.cid-index %}
{% assign aidx = site.data.corpus_v3.alias-index %}
{% assign tridx = site.data.corpus_v3.transition %}

{% if cidx %}
The next-generation Corpus v3 graph projects every Corpus Item to a permanent `/id/cid######/` URL with relation panels, identifier box, and JSON-LD metadata. This is a parallel surface to the v2 Registry above — both remain live during the v3 cutover phase.

<div class="prior-art-totals" aria-label="Corpus v3 live totals">
  <span class="prior-art-totals-chip"><strong>{{ cidx.total_cids }}</strong> Corpus Items</span>
  {% if aidx %}<span class="prior-art-totals-chip"><strong>{{ aidx.total_aliases }}</strong> aliases tracked</span>{% endif %}
  {% if tridx %}<span class="prior-art-totals-chip"><strong>{{ tridx.total_v2_transitions }}</strong> v2→v3 transitions</span>{% endif %}
</div>

### Type distribution

{% assign type_counts = "" | split: "" %}
{% for cid_entry in cidx.cids %}
  {% assign t = cid_entry[1].type %}
  {% if t and t != "" %}{% assign type_counts = type_counts | push: t %}{% endif %}
{% endfor %}

{% assign type_uniq = type_counts | uniq | sort %}
<ul style="columns: 2; column-gap: 24px; list-style: none; padding-left: 0; margin: 16px 0;">
  {% for t in type_uniq %}
    {% assign count = 0 %}
    {% for tc in type_counts %}{% if tc == t %}{% assign count = count | plus: 1 %}{% endif %}{% endfor %}
    <li style="margin: 4px 0;">
      <code>{{ t | replace: "_", " " }}</code> &nbsp;<strong>{{ count }}</strong>
    </li>
  {% endfor %}
</ul>

### Sample item pages

A handful of representative Corpus v3 surfaces to explore:

- [Master Constant Calibration (THM0001)](/id/cid000010/) — the running-example theorem with its full prose proof at [PRF0001](/id/cid000022/) and its Lean formalization at [FTH0001](/id/cid000020/)
- [Construction Spine (DOS0001)](/id/cid000003/) — the 121-step construction dossier
- [Book II — The τ-Kernel (BOK0001)](/id/cid000001/) — monograph artifact item
- [Categorical AI (PAP0001)](/id/cid000004/) — research paper artifact
- [No Independent Dark-Sector Particle (RSL0001)](/id/cid000021/) — Result item with inspection route
- [Lean-Formalized Proof of FTA on τ-Idx (PRF0005)](/id/cid006108/) — lean_formalized proof item

Every public typed alias also short-routes — e.g., [`/thm0001/`](/thm0001/), [`/def0001/`](/def0001/), [`/pap0001/`](/pap0001/), [`/dos0001/`](/dos0001/) — for citation continuity. v2 legacy IDs (II.T25, S024, RN-001, WP-RC-CS-E0-E3, etc.) are preserved as `aliases[]` on each item and discoverable via search.

### Discipline

Per the [Corpus v3 Charter](https://github.com/Panta-Rhei-Research/corpus-v3/blob/main/CHARTER.md):

- CIDs are permanent (never reused after public release)
- Typed aliases are typed-short-ID aliases of the canonical CID
- Atoms contain. Artifacts point. Projections render.
- `prrp://` makes prose proofs corpus-addressed (Wave 6)
- Public-closure CI keeps the public graph closed (Wave 8 activates strict enforcement)

The v3 graph is bidirectionally formalization-aware (prose ↔ Lean), machine-readable as JSON-LD on every item page, and exposes its full dependency closure for downstream audit tools.

{% endif %}
