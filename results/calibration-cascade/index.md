---
layout: program-doc
title: "Calibration Cascade"
permalink: /results/calibration-cascade/
lane: results
v2_lane: results
type: "Results Overlay"
status: "Review-Facing"
summary_short: "Dependency overlay connecting numerical claims, constants, unit contexts, sources, Registry items, and verification surfaces."
tags:
  - calibration-cascade
  - numerical-predictions
  - constants-ledger
  - verification
right_rail:
  - title: "Numerical Prediction Catalogue"
    url: "/results/predictions/"
  - title: "Falsification N-tests"
    url: "/results/falsifications/"
  - title: "Physics Verification"
    url: "/verify/domain-verification/physics/"
  - title: "Numerical Physics Ledger Artifact"
    url: "/publications/monograph-supplements/numerical-physics-ledger/"
---

{% assign cascade = site.data.corpus.calibration.calibration_cascade.calibration_cascade %}
{% assign layers = site.data.corpus.calibration.cascade_layers.layers %}
{% assign nodes = site.data.corpus.calibration.constant_nodes.nodes %}
{% assign edges = site.data.corpus.calibration.cascade_edges.edges %}
{% assign couplings = site.data.corpus.calibration.coupling_ledger.couplings %}
{% assign mass_links = site.data.corpus.calibration.mass_ratio_chain.mass_ratio_links %}
{% assign constants = site.data.corpus.calibration.constants_ledger.constants %}
{% assign bridge = site.data.corpus.calibration.g_alpha_bridge.g_alpha_bridge %}
{% assign comparisons = site.data.corpus.calibration.verification_comparisons.verification_comparisons %}
{% assign datasets = site.data.corpus.calibration.comparison_datasets.comparison_datasets %}
{% assign source_chapters = site.data.corpus.calibration.source_chapters.source_chapters %}
{% assign index = site.data.corpus.calibration.index.calibration %}

<div class="notice note">
  <strong>Boundary.</strong>
  {{ cascade.boundary_statement }}
</div>

<p>{{ cascade.summary }}</p>

<div class="notice note">
  <strong>Metrology note.</strong>
  {{ cascade.metrology_note }}
</div>

## Inputs

<table>
  <thead>
    <tr>
      <th scope="col">Input</th>
      <th scope="col">Formula / role</th>
      <th scope="col">Source</th>
    </tr>
  </thead>
  <tbody>
    {% for input in cascade.inputs %}
    <tr>
      <th scope="row">{{ input.label }}</th>
      <td><code>{{ input.symbol }}</code> · {{ input.formula }}</td>
      <td><code>{{ input.source.chapter_id }}</code> · <code>{{ input.source.label }}</code></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Layer Model

<ol class="v2-grid v2-card-list">
  {% for layer in layers %}
  <li>
    <article class="v2-tile">
      <p class="eyebrow">{{ layer.id }}</p>
      <h3>{{ layer.title }}</h3>
      <p>{{ layer.summary }}</p>
      <p><strong>Inputs:</strong> {{ layer.primary_inputs | join: ", " }}</p>
      <p><strong>Outputs:</strong> {{ layer.primary_outputs | join: ", " }}</p>
      <p><strong>Verification mode:</strong> <code>{{ layer.verification_mode }}</code></p>
    </article>
  </li>
  {% endfor %}
</ol>

## Dependency Graph

<table>
  <thead>
    <tr>
      <th scope="col">From</th>
      <th scope="col">Relation</th>
      <th scope="col">To</th>
    </tr>
  </thead>
  <tbody>
    {% for edge in edges %}
    {% assign from_node = nodes | where: "id", edge.source | first %}
    {% assign to_node = nodes | where: "id", edge.target | first %}
    <tr>
      <th scope="row">{{ from_node.label | default: edge.source }}</th>
      <td><code>{{ edge.relation }}</code></td>
      <td>{{ to_node.label | default: edge.target }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Coupling Ledger

<p>The coupling ledger is not a separate ontology here. It is one dependency table inside the cascade.</p>

<table>
  <thead>
    <tr>
      <th scope="col">Entry</th>
      <th scope="col">Kind</th>
      <th scope="col">Formula</th>
      <th scope="col">Value</th>
      <th scope="col">Registry</th>
    </tr>
  </thead>
  <tbody>
    {% for item in couplings %}
    <tr>
      <th scope="row"><code>{{ item.symbol }}</code></th>
      <td>{{ item.kind }}</td>
      <td><code>{{ item.formula }}</code></td>
      <td>{{ item.display_value }}</td>
      <td>{% if item.registry_refs.size > 0 %}{% for ref in item.registry_refs %}<code>{{ ref }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}{% else %}Pending review{% endif %}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Mass-Ratio Chain

<table>
  <thead>
    <tr>
      <th scope="col">Link</th>
      <th scope="col">Step</th>
      <th scope="col">Formula / output</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    {% for item in mass_links %}
    <tr>
      <th scope="row">{{ item.sequence }}</th>
      <td>{{ item.title }}</td>
      <td><code>{{ item.formula }}</code></td>
      <td>{{ item.mapping_status | replace: "_", " " }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## G-Alpha Bridge

<div class="content-card">
  <p><strong>{{ bridge.title }}</strong></p>
  <p><strong>Dimensionless identity:</strong> <code>{{ bridge.dimensionless_identity }}</code></p>
  <p><strong>G readout formula:</strong> <code>{{ bridge.g_readout_formula }}</code></p>
  <p><strong>Unit context:</strong> <code>{{ bridge.unit_context }}</code></p>
  <p><strong>Status:</strong> {{ bridge.status | replace: "_", " " }}</p>
  <ul>
    {% for limitation in bridge.limitations %}
    <li>{{ limitation }}</li>
    {% endfor %}
  </ul>
</div>

## Constants Ledger

<p>The constants ledger is rendered as a table of outputs. It does not decide, by itself, whether a dependency path is formally verified or externally accepted.</p>

<p>Notation guardrail: the Bohr radius is rendered as <code>a_B</code> with the alias <code>a_0^{Bohr}</code> where needed, so it is not confused with acceleration-scale notation elsewhere in the physics pages.</p>

<table>
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Quantity</th>
      <th scope="col">Formula</th>
      <th scope="col">Scope</th>
      <th scope="col">Deviation</th>
      <th scope="col">Unit context</th>
    </tr>
  </thead>
  <tbody>
    {% for item in constants %}
    <tr>
      <th scope="row">{{ item.sequence }}</th>
      <td><code>{{ item.symbol }}</code> · {{ item.quantity }}</td>
      <td><code>{{ item.formula }}</code></td>
      <td>{{ item.scope_label }}</td>
      <td>{{ item.deviation }}</td>
      <td><code>{{ item.unit_context }}</code></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Verification Comparisons

<p>These rows preserve the manuscript comparison vintage. They are not a CODATA 2022 recalculation.</p>

<table>
  <thead>
    <tr>
      <th scope="col">Quantity</th>
      <th scope="col">Tau value</th>
      <th scope="col">CODATA 2018 value</th>
      <th scope="col">Deviation</th>
    </tr>
  </thead>
  <tbody>
    {% for item in comparisons %}
    <tr>
      <th scope="row">{{ item.quantity }}</th>
      <td>{{ item.tau_value }}</td>
      <td>{{ item.comparison_value }}</td>
      <td>{{ item.deviation }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Dataset Guardrails

<ul>
  {% for dataset in datasets %}
  <li><strong>{{ dataset.title }}</strong> · {{ dataset.role | replace: "_", " " }} · <a href="{{ dataset.url }}">{{ dataset.url }}</a></li>
  {% endfor %}
</ul>

## Source Chapters

<table>
  <thead>
    <tr>
      <th scope="col">Source</th>
      <th scope="col">Role</th>
      <th scope="col">Labels</th>
      <th scope="col">SHA-256</th>
    </tr>
  </thead>
  <tbody>
    {% for source in source_chapters %}
    <tr>
      <th scope="row"><code>{{ source.id }}</code></th>
      <td>{{ source.role | replace: "_", " " }}</td>
      <td>{{ source.labels | size }}</td>
      <td><code>{{ source.sha256 | slice: 0, 12 }}</code></td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Limitations

- This is a static, review-facing overlay, not a dynamic graph application.
- The page does not recompute CODATA 2022 values or change the Numerical Physics Ledger PDF artifact.
- Unresolved Registry, TauLib, and source-label mappings remain visible as pending review.
- “SI readout / unit realization” language is used deliberately; the cascade is not presented as an unqualified SI prediction engine.

## Projection Metadata

- Public export route: `/assets/data/calibration/`
- Layer count: **{{ index.counts.layers }}**
- Coupling entries: **{{ index.counts.couplings }}**
- Mass-ratio links: **{{ index.counts.mass_ratio_links }}**
- Constants-ledger entries: **{{ index.counts.constants }}**
