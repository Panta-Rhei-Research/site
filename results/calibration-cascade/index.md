---
layout: program-doc
title: "Calibration Cascade"
permalink: /results/calibration-cascade/
lane: results
v2_lane: results
type: "Results Overlay"
status: "Review-Facing"
summary_short: "Constants, couplings, mass ratios, and SI readouts from iota-tau and one dimensional anchor."
tags:
  - calibration-cascade
  - numerical-predictions
  - constants-ledger
  - verification
right_rail:
  related:
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
{% assign dependency_edges = edges | where: "edge_type", "dependency" %}
{% assign couplings = site.data.corpus.calibration.coupling_ledger.couplings %}
{% assign mass_links = site.data.corpus.calibration.mass_ratio_chain.mass_ratio_links %}
{% assign constants = site.data.corpus.calibration.constants_ledger.constants %}
{% assign constant_pages = site.data.corpus.calibration.constant_pages.constant_pages %}
{% assign bridge = site.data.corpus.calibration.g_alpha_bridge.g_alpha_bridge %}
{% assign comparisons = site.data.corpus.calibration.verification_comparisons.verification_comparisons %}
{% assign datasets = site.data.corpus.calibration.comparison_datasets.comparison_datasets %}
{% assign unit_contexts = site.data.corpus.calibration.unit_contexts.unit_contexts %}
{% assign source_chapters = site.data.corpus.calibration.source_chapters.source_chapters %}
{% assign index = site.data.corpus.calibration.index.calibration %}
{% assign established_constants = constants | where: "scope_label", "Established" %}
{% assign tau_constants = constants | where: "scope_label", "Tau-effective" %}
{% assign conjectural_constants = constants | where: "scope_label", "Conjectural" %}
{% assign structural_constants = constants | where: "scope_label", "Metaphorical / structural reading" %}

<div class="calibration-badge-row" aria-label="Calibration Cascade status">
  <span class="chip">Results Overlay</span>
  <span class="chip">Physics</span>
  <span class="chip">E1</span>
  <span class="chip">Directed Acyclic Cascade</span>
  <span class="chip">Registry-backed</span>
  <span class="chip">TauLib-linked</span>
  <span class="chip">External review required</span>
</div>

<div class="notice note">
  <strong>Boundary.</strong>
  The Calibration Cascade is the Results-side overlay that shows how the Panta Rhei physics layer organizes constants.
  It starts with the algebraic master constant <code>ι_τ = 2/(π+e)</code> and one dimensional calibration anchor,
  the neutron mass <code>m_n</code>.
</div>

<p>{{ cascade.summary }}</p>

<div class="notice note">
  <strong>Directed structure.</strong>
  The Calibration Cascade is intentionally represented as a directed acyclic dependency structure rather than a generic graph explorer.
  Dependencies flow from algebraic inputs through dimensionless readouts, dimensional anchoring, SI realization, and verification comparison.
</div>

<div class="notice note">
  <strong>Metrology note.</strong>
  The modern SI is defined through exact numerical values of seven defining constants. This page therefore distinguishes
  τ-internal readouts, dimensional anchoring, SI expression, and external comparison datasets rather than treating SI-defining
  constants as ordinary measured predictions. The Book IV/V source chapters use CODATA 2018 as their comparison baseline;
  current CODATA 2022 / NIST and BIPM links are retained as guardrails, not recalculated Corpus claims.
</div>

<div class="calibration-two-column">
  <article class="calibration-card">
    <h3>This Page Is</h3>
    <ul>
      <li>a dependency cascade;</li>
      <li>a public inspection overlay;</li>
      <li>a map from <code>ι_τ</code> and <code>m_n</code> to readout layers;</li>
      <li>a bridge between source chapters and prediction/falsification pages;</li>
      <li>a Registry, TauLib, and source-chapter provenance surface.</li>
    </ul>
  </article>
  <article class="calibration-card">
    <h3>This Page Is Not</h3>
    <ul>
      <li>a generic graph explorer;</li>
      <li>the old Physics Ledger ontology;</li>
      <li>a new lane or final physical ontology;</li>
      <li>a substitute for expert physics or metrology review;</li>
      <li>a claim that SI-defining constants are ordinary measured predictions;</li>
      <li>a process-level Standard Model scattering calculation.</li>
    </ul>
  </article>
</div>

<nav class="calibration-inspection-nav" aria-label="Follow the cascade">
  <span>Follow the cascade:</span>
  <a href="#inputs">1. Inputs</a>
  <a href="#coupling-ledger">2. Couplings</a>
  <a href="#mass-ratio-chain">3. Mass-Ratio Chain</a>
  <a href="#g-alpha-bridge">4. G-alpha Bridge</a>
  <a href="#constants-ledger">5. Constants Ledger</a>
  <a href="#verification-comparisons">6. Verification Comparisons</a>
</nav>

## Inputs {#inputs}

<div class="calibration-input-grid">
  {% for input in cascade.inputs %}
  {% assign node = nodes | where: "id", input.id | first %}
  <article class="calibration-card" id="node-{{ input.id }}">
    <p class="eyebrow">{{ node.layer | default: "Input" }}</p>
    <h3>{{ input.label }}</h3>
    <p><strong>Formula / role:</strong> <code>{{ input.symbol }}</code> · {{ input.formula }}</p>
    <p><strong>Status:</strong> {{ node.scope_label }}</p>
    <p><strong>Boundary:</strong>
      {% if input.id == "neutron-mass-anchor" %}
      scale-setting anchor, not absolute mass prediction.
      {% else %}
      algebraic master constant feeding dimensionless readouts.
      {% endif %}
    </p>
    <p><strong>Source:</strong> <code>{{ input.source.chapter_id }}</code> · <code>{{ input.source.label }}</code></p>
  </article>
  {% endfor %}
</div>

## Layers

<div class="calibration-layer-grid">
  {% for layer in layers %}
  <article class="calibration-card" id="layer-{{ layer.id | downcase }}">
    <p class="eyebrow">{{ layer.id }}</p>
    <h3>{{ layer.title }}</h3>
    <p>{{ layer.summary }}</p>
    <p><strong>Representative nodes:</strong> {{ layer.primary_outputs | join: ", " }}</p>
    <p><strong>Scope note:</strong> <code>{{ layer.verification_mode }}</code></p>
  </article>
  {% endfor %}
</div>

## Cascade overview

<p>The schematic below is intentionally compact. It shows the finite dependency order, not every node in the constants table. The detailed machine-readable edge list remains available immediately below it.</p>

<section class="calibration-compact-schematic" aria-label="Compact Calibration Cascade schematic">
  <article class="calibration-schematic-stage">
    <p class="eyebrow">Inputs</p>
    <h3><code>ι_τ</code> + <code>m_n</code></h3>
    <p>Algebraic master constant plus neutron-mass anchor.</p>
  </article>
  <article class="calibration-schematic-stage">
    <p class="eyebrow">L0-L1</p>
    <h3>Couplings</h3>
    <p>Dimensionless readouts and coupling ledger entries.</p>
  </article>
  <article class="calibration-schematic-stage">
    <p class="eyebrow">L2</p>
    <h3>Mass-ratio chain</h3>
    <p>Ten-link route to the electron-mass readout.</p>
  </article>
  <article class="calibration-schematic-stage">
    <p class="eyebrow">L3</p>
    <h3>G-alpha bridge</h3>
    <p>Unit-context-aware SI readout / unit realization.</p>
  </article>
  <article class="calibration-schematic-stage">
    <p class="eyebrow">L4</p>
    <h3>Verification</h3>
    <p>CODATA 2018 comparison rows and falsification surfaces.</p>
  </article>
  <p class="calibration-text-equivalent">
    <strong>Text equivalent.</strong>
    <code>ι_τ</code> feeds the coupling ledger, alpha, and the mass-ratio chain. The mass-ratio chain and the neutron-mass
    anchor feed the electron-mass readout. Alpha feeds the G-alpha bridge, which combines with the neutron-mass anchor
    in the G readout route. Electron-mass and G readouts feed SI readout / unit realization, which feeds CODATA 2018
    verification comparisons. Prediction and falsification pages are related review surfaces, not additional dependency edges.
  </p>
</section>

<div class="calibration-chip-row" aria-label="Scope label legend">
  <span class="chip">Established</span>
  <span class="chip">τ-effective</span>
  <span class="chip">Conjectural</span>
  <span class="chip">Metaphorical / structural</span>
  <span class="chip">Pending unit-context review</span>
</div>

<div class="notice note">
  <strong>Scope label.</strong> Tau-effective means τ-effective. Metadata keeps the stable value <code>tau_effective</code>; public pages render the visible label as <strong>τ-effective</strong>.
</div>

<span id="key-nodes"></span>

## Key constant cascades

<div class="calibration-key-node-grid">
  {% for item in constant_pages %}
  <a class="calibration-key-node-card" href="{{ item.route | relative_url }}" id="key-node-{{ item.slug }}">
    <span class="eyebrow">{{ item.layer }} · {{ item.scope_label }}</span>
    <strong>{{ item.title }}</strong>
    <code>{{ item.formula_display }}</code>
    <span>{{ item.public_boundary }}</span>
    {% if item.dependency_labels.size > 0 %}
    <small>Depends on: {{ item.dependency_labels | join: ", " }}</small>
    {% else %}
    <small>Privileged input</small>
    {% endif %}
  </a>
  {% endfor %}
</div>

<p><a class="button" href="{{ '/results/calibration-cascade/constants/' | relative_url }}">Open all seeded constant pages</a></p>

## Dependency edge table {#dependency-edge-table}

<p>This machine-readable dependency view preserves the edge list behind the overview. Acyclicity checks apply to dependency edges only; related prediction and falsification surfaces remain outside the dependency DAG.</p>

<div class="calibration-table-wrap">
  <table>
    <thead>
      <tr>
        <th scope="col">From</th>
        <th scope="col">Relation</th>
        <th scope="col">To</th>
        <th scope="col">Edge type</th>
      </tr>
    </thead>
    <tbody>
      {% for edge in edges %}
      {% assign source_node = nodes | where: "id", edge.source | first %}
      {% assign target_node = nodes | where: "id", edge.target | first %}
      <tr>
        <th scope="row"><a href="#node-{{ edge.source }}">{{ source_node.display.short_label | default: edge.source }}</a></th>
        <td><code>{{ edge.relation }}</code></td>
        <td><a href="#node-{{ edge.target }}">{{ target_node.display.short_label | default: edge.target }}</a></td>
        <td>{{ edge.edge_type | replace: "_", " " }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

## Mass-Ratio Chain

<p>The mass-ratio chain is the clearest finite derivation path in the cascade. It shows how the neutron-to-electron mass ratio is built through a ten-link route from the τ³ fibration, torus spectral data, lemniscate capacity, and holonomy correction.</p>

<ol class="calibration-card-list">
  {% for item in mass_links %}
  <li>
    <details class="calibration-inspector-card" id="node-mass-ratio-{{ item.id | downcase }}">
      <summary>
        <span class="calibration-summary-main">
          <strong>{{ item.sequence }}. {{ item.title }}</strong>
          <code>{{ item.formula }}</code>
        </span>
        <span class="calibration-summary-meta">
          <span class="chip">{{ item.layer }}</span>
          <span class="chip">{{ item.mapping_status | replace: "_", " " }}</span>
        </span>
      </summary>
      <div class="calibration-detail-body">
        <p>{{ item.title }} is retained as a finite source-mapped link in the ten-step chain.</p>
        <div class="calibration-detail-grid">
          <div><strong>Source</strong><br><code>{{ item.source.chapter_id }}</code><br><code>{{ item.source.label | default: "pending label review" }}</code></div>
          <div><strong>Registry</strong><br>{% if item.registry_refs.size > 0 %}{% for ref in item.registry_refs %}<code>{{ ref }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}{% else %}Pending review{% endif %}</div>
          <div><strong>TauLib</strong><br>{% if item.taulib_modules.size > 0 %}{% for module in item.taulib_modules %}<code>{{ module }}</code>{% unless forloop.last %}<br>{% endunless %}{% endfor %}{% else %}Pending review{% endif %}</div>
        </div>
      </div>
    </details>
  </li>
  {% endfor %}
</ol>

## Coupling Ledger

<p>The coupling ledger is one dimensionless dependency table inside the cascade. It is not a separate ontology.</p>

<ol class="calibration-card-list">
  {% for item in couplings %}
  <li>
    <details class="calibration-inspector-card" id="node-coupling-{{ item.id | downcase }}">
      <summary>
        <span class="calibration-summary-main">
          <strong><code>{{ item.symbol }}</code> · {{ item.meaning }}</strong>
          <code>{{ item.formula }}</code>
        </span>
        <span class="calibration-summary-meta">
          <span class="chip">{{ item.kind }}</span>
          <span class="chip">{{ item.layer }}</span>
        </span>
      </summary>
      <div class="calibration-detail-body">
        <div class="calibration-detail-grid">
          <div><strong>Value</strong><br>{{ item.display_value }}</div>
          <div><strong>Source</strong><br><code>{{ item.source.chapter_id }}</code><br><code>{{ item.source.label }}</code></div>
          <div><strong>Registry</strong><br>{% for ref in item.registry_refs %}<code>{{ ref }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}</div>
          <div><strong>TauLib</strong><br>{% for module in item.taulib_modules %}<code>{{ module }}</code>{% unless forloop.last %}<br>{% endunless %}{% endfor %}</div>
        </div>
      </div>
    </details>
  </li>
  {% endfor %}
</ol>

## G-Alpha Bridge

<div class="calibration-card-list" id="g-alpha-bridge-cards">
<details class="calibration-inspector-card" id="node-g-alpha-identity" open>
  <summary>
    <span class="calibration-summary-main">
      <strong>Dimensionless identity</strong>
      <code>{{ bridge.dimensionless_identity }}</code>
    </span>
    <span class="calibration-summary-meta">
      <span class="chip">{{ bridge.status | replace: "_", " " }}</span>
      <span class="chip">dimensionless identity</span>
    </span>
  </summary>
  <div class="calibration-detail-body">
    <p>{{ bridge.title }} keeps the dimensionless identity separate from the SI readout formula.</p>
  </div>
</details>
<details class="calibration-inspector-card" id="node-g-alpha-si-readout" open>
  <summary>
    <span class="calibration-summary-main">
      <strong>SI readout formula</strong>
      <code>{{ bridge.g_readout_formula }}</code>
    </span>
    <span class="calibration-summary-meta">
      <span class="chip">{{ bridge.unit_context | replace: "_", " " }}</span>
    </span>
  </summary>
  <div class="calibration-detail-body">
    <p><strong>Dimensionless identity ≠ SI readout formula.</strong> The readout formula is rendered only with the explicit unit context shown here.</p>
  </div>
</details>
<details class="calibration-inspector-card" id="node-g-alpha-bridge" open>
  <summary>
    <span class="calibration-summary-main">
      <strong>Unit context and pending alternatives</strong>
      <code>{{ bridge.unit_context }}</code>
    </span>
    <span class="calibration-summary-meta">
      <span class="chip">review boundary</span>
    </span>
  </summary>
  <div class="calibration-detail-body">
    <ul>
      {% for limitation in bridge.limitations %}
      <li>{{ limitation }}</li>
      {% endfor %}
    </ul>
  </div>
</details>
</div>

## Constants Ledger

<p>The constants ledger is a table of cascade outputs. Its rows should be read with their scope labels, unit context, and source vintage. The table does not by itself establish external acceptance.</p>

<p>Notation guardrail: the Bohr radius is rendered as <code>a_B</code> with the alias <code>a_0^{Bohr}</code> where needed, so it is not confused with acceleration-scale notation elsewhere in the physics pages.</p>

<div class="calibration-scope-groups" aria-label="Constants Ledger by scope">
  {% assign scope_sets = "Established|Tau-effective|Conjectural|Metaphorical / structural reading" | split: "|" %}
  {% for scope_name in scope_sets %}
  {% assign scoped_constants = constants | where: "scope_label", scope_name %}
  {% assign scope_display = scope_name | replace: "Tau-effective", "τ-effective" | replace: "Metaphorical / structural reading", "Metaphorical / structural" %}
  <details class="calibration-inspector-card" id="constant-scope-{{ scope_name | slugify }}" {% if forloop.first %}open{% endif %}>
    <summary>
      <span class="calibration-summary-main">
        <strong>{{ scope_display }}</strong>
        <span>{{ scoped_constants | size }} constants-ledger entries</span>
      </span>
      <span class="calibration-summary-meta">
        <span class="chip">scope group</span>
      </span>
    </summary>
    <div class="calibration-detail-body">
      <ol class="calibration-card-list calibration-card-list--compact">
        {% for item in scoped_constants %}
        {% assign unit_context = unit_contexts | where: "id", item.unit_context | first %}
        <li>
          <a class="calibration-compact-row" href="#node-constant-{{ item.id | downcase }}">
            <strong>{{ item.sequence }}. <code>{{ item.symbol }}</code> · {{ item.quantity }}</strong>
            <span><code>{{ item.formula }}</code></span>
            <small>{{ unit_context.label | default: item.unit_context }} · {{ item.deviation }}</small>
          </a>
        </li>
        {% endfor %}
      </ol>
    </div>
  </details>
  {% endfor %}
</div>

<ol class="calibration-card-list" aria-label="Constants Ledger detail cards">
  {% for item in constants %}
  {% assign unit_context = unit_contexts | where: "id", item.unit_context | first %}
  <li>
    <details class="calibration-inspector-card" id="node-constant-{{ item.id | downcase }}">
      {% assign item_scope_display = item.scope_label | replace: "Tau-effective", "τ-effective" | replace: "Metaphorical / structural reading", "Metaphorical / structural" %}
      <summary>
        <span class="calibration-summary-main">
          <strong>{{ item.sequence }}. <code>{{ item.symbol }}</code> · {{ item.quantity }}</strong>
          <code>{{ item.formula }}</code>
        </span>
        <span class="calibration-summary-meta">
          <span class="chip">{{ item_scope_display }}</span>
          <span class="chip">{{ unit_context.label | default: item.unit_context }}</span>
        </span>
      </summary>
      <div class="calibration-detail-body">
        <div class="calibration-detail-grid">
          <div><strong>Deviation</strong><br>{{ item.deviation }}</div>
          <div><strong>Layer</strong><br>{{ item.layer }}</div>
          <div><strong>Source</strong><br><code>{{ item.source.chapter_id }}</code><br><code>{{ item.source.label }}</code></div>
          <div><strong>Mapping status</strong><br>{{ item.mapping_status | replace: "_", " " }}</div>
        </div>
      </div>
    </details>
  </li>
  {% endfor %}
</ol>

<div class="calibration-table-wrap">
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
      {% assign item_scope_display = item.scope_label | replace: "Tau-effective", "τ-effective" | replace: "Metaphorical / structural reading", "Metaphorical / structural" %}
      <tr>
        <th scope="row">{{ item.sequence }}</th>
        <td><code>{{ item.symbol }}</code> · {{ item.quantity }}</td>
        <td><code>{{ item.formula }}</code></td>
        <td>{{ item_scope_display }}</td>
        <td>{{ item.deviation }}</td>
        <td><code>{{ item.unit_context }}</code></td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

## Verification Comparisons

<p>These comparison rows preserve the manuscript baseline. Current public reference values may be tracked separately, but they should not be silently mixed with the Book IV/V CODATA 2018 comparisons.</p>

<div class="calibration-table-wrap">
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
</div>

## Dataset Guardrails

<ul>
  {% for dataset in datasets %}
  <li><strong>{{ dataset.title }}</strong> · {{ dataset.role | replace: "_", " " }} · <a href="{{ dataset.url }}">{{ dataset.url }}</a></li>
  {% endfor %}
</ul>

## Source Chapters

<div class="calibration-card-list" aria-label="Source chapter details">
  {% for source in source_chapters %}
  <details class="calibration-inspector-card" id="source-{{ source.id }}">
    <summary>
      <span class="calibration-summary-main">
        <strong><code>{{ source.id }}</code> · {{ source.title }}</strong>
        <span>{{ source.role | replace: "_", " " }}</span>
      </span>
      <span class="calibration-summary-meta">
        <span class="chip">{{ source.labels | size }} labels</span>
        <span class="chip">{{ source.source_status | replace: "_", " " }}</span>
      </span>
    </summary>
    <div class="calibration-detail-body">
      <div class="calibration-detail-grid">
        <div><strong>Source file</strong><br><code>{{ source.source_path }}</code></div>
        <div><strong>Registry range</strong><br>{% if source.registry_comments.size > 0 %}{% for comment in source.registry_comments %}<code>{{ comment }}</code>{% unless forloop.last %}<br>{% endunless %}{% endfor %}{% else %}Pending explicit range review{% endif %}</div>
        <div><strong>Line count</strong><br>{{ source.line_count }}</div>
        <div><strong>SHA-256</strong><br><code>{{ source.sha256 }}</code></div>
      </div>
      <p><strong>Extracted labels:</strong></p>
      <p class="calibration-label-cloud">
        {% for label in source.labels %}
        <code>{{ label }}</code>{% unless forloop.last %} {% endunless %}
        {% endfor %}
      </p>
    </div>
  </details>
  {% endfor %}
</div>

<div class="calibration-table-wrap">
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
</div>

## Limitations

- This is a static, review-facing overlay, not a dynamic graph application.
- The page does not recompute CODATA 2022 values or change the existing numerical prediction artifact.
- Unresolved Registry, TauLib, and source-label mappings remain visible as pending review.
- “SI readout / unit realization” language is used deliberately; the cascade is not presented as an unqualified SI prediction engine.
- The prediction catalogue lists claims; this page shows dependency structure and review boundaries.

## Projection Metadata

- Public export route: `/assets/data/calibration/`
- Layer count: **{{ index.counts.layers }}**
- Dependency edges: **{{ index.counts.dependency_edges }}**
- Coupling entries: **{{ index.counts.couplings }}**
- Mass-ratio links: **{{ index.counts.mass_ratio_links }}**
- Constants-ledger entries: **{{ index.counts.constants }}**
