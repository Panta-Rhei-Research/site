---
layout: program-doc
title: "Progress Against Agenda"
lane: results
v2_lane: results
permalink: /results/progress-against-agenda/
type: "Result Index"
status: "Canonical"
summary_short: "Dashboard view of the program's current public status against declared Structural Challenge Ledger, Core Semantics, and Mathematical Refusal obligations."
summary_cards:
  - title: "Agenda mirror"
    body: "Aggregates public Structural Challenge Ledger and Core Semantics status without replacing the detailed mirrors."
  - title: "v4 obligation surface"
    body: "Aggregates the Structural Challenge Ledger, Challenge Responses, Core Semantics obligations, and explicit mathematical refusals. Legacy v1 raw-feed items are archived as provenance only and are not counted as canonical challenges unless promoted into the v4 Structural Challenge Ledger."
  - title: "Status discipline"
    body: "Internal progress remains separate from verification state and external acceptance."
right_rail:
  related:
    - title: "Agenda"
      url: /agenda/
    - title: "Challenge Responses"
      url: /results/challenge-responses/
    - title: "Core Semantics Status"
      url: /results/core-semantics-status/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Result Index"
    scope: "Agenda mirror"
    status: "Canonical"
    updated: "May 2026"
---

{% assign progress_raw = site.data.agenda_progress["agenda-progress"] %}
{%- comment -%}
  v4 Wave 6 default-view filter: exclude legacy v1 raw-feed items that
  were imported wholesale from external open-problem lists for Life and
  Metaphysics. The canonical v4 obligation surface is the Structural
  Challenge Ledger; only Mathematics + Physics retain v1 problem rows
  in the default dashboard until Atlas regenerates the data with
  structural_challenge as the canonical item type. Refusals and
  recovery items are always shown.
{%- endcomment -%}
{% assign progress = progress_raw | where_exp: "item", "item.item_kind != 'problem' or item.domain == 'mathematics' or item.domain == 'physics'" %}
{% assign total_count = progress | size %}
{% assign problems = progress | where: "item_kind", "problem" %}
{% assign recovery_requirements = progress | where: "item_kind", "recovery_requirement" %}
{% assign refusals = progress | where: "item_kind", "mathematical_refusal" %}
{% assign recently_updated = progress | sort: "last_modified" | reverse %}
{% assign not_yet_touched = progress | where_exp: "item", "item.is_not_yet_touched" %}
{% assign reclassified = progress | where_exp: "item", "item.is_reclassified_or_dismissed" %}
{% assign partial_recovery = progress | where: "display_status", "partial" %}
{% assign partial_answers = progress | where: "display_status", "partially_addressed" %}
{% assign verified_internal = progress | where: "verification_status", "verified" %}
{% assign externally_reviewed = progress | where_exp: "item", "item.external_status != 'not_externally_reviewed'" %}
{% assign legacy_excluded_count = progress_raw | size | minus: total_count %}

{%- comment -%}
  Wave 3: Strategy B separated panels. Challenge Responses count is
  authoritative from _data/structural_challenges/{domain}.json (the
  same source the Challenge Responses domain pages use), not from the
  agenda-progress feed. Domain sums: 38 + 117 + 29 + 30 = 214.
{%- endcomment -%}
{% assign cr_math = site.data.structural_challenges.mathematics.items | size %}
{% assign cr_physics = site.data.structural_challenges.physics.items | size %}
{% assign cr_life = site.data.structural_challenges.life.items | size %}
{% assign cr_metaphysics = site.data.structural_challenges.metaphysics.items | size %}
{% assign cr_total = cr_math | plus: cr_physics | plus: cr_life | plus: cr_metaphysics %}

## Status disclaimer

Status indicates the current internal state of the research program. A proposed answer, partial recovery, or internally addressed status does not mean external verification, scientific acceptance, or final settlement.

## Progress as a Results surface

{% capture progress_plate_caption %}Progress Against Agenda is one of the Results surfaces: a dashboard over obligations, recovery targets, and current program stance.{% endcapture %}
{% include scientific-plate.html id="plate-05-results-world-readout" variant="thumb" class="scientific-plate--compact" caption=progress_plate_caption loading="lazy" %}

Progress Against Agenda tracks current program stance against public obligations and recovery targets.

## Obligation surfaces

The dashboard tracks three independent v4 obligation surfaces. Counts are kept separated rather than rolled up into a single total — each surface answers a different question.

<div class="v2-grid">
  <div class="v2-tile">
    <strong>{{ cr_total }} Challenge Responses</strong>
    <span>Results-side projection of the canonical Structural Challenge Ledger. <a href="{{ '/results/challenge-responses/' | relative_url }}">Open Challenge Responses</a> · {{ cr_math }} mathematics · {{ cr_physics }} physics · {{ cr_life }} life · {{ cr_metaphysics }} metaphysics.</span>
  </div>
  <div class="v2-tile">
    <strong>{{ recovery_requirements | size }} Core Semantics / Recovery items</strong>
    <span>Language, structures, laws, grammars, and refusal boundaries the theory must earn. <a href="{{ '/agenda/core-semantics/' | relative_url }}">Open Core Semantics</a>.</span>
  </div>
  <div class="v2-tile">
    <strong>{{ refusals | size }} Mathematical Refusals</strong>
    <span>Explicit refusals where the program declines to claim settlement, with reason.</span>
  </div>
  <div class="v2-tile">
    <strong>Legacy v1 raw-feed archive: {{ legacy_excluded_count }} archived</strong>
    <span>Life + Metaphysics raw-feed imports preserved as provenance only. Not counted as canonical challenges unless promoted into the v4 Structural Challenge Ledger.</span>
  </div>
</div>

## Per-surface progress detail

The metrics below cover the dashboard data feed (agenda-progress.json), which currently surfaces {{ problems | size }} Mathematics + Physics structural challenges, {{ recovery_requirements | size }} Core Semantics / Recovery items, and {{ refusals | size }} Mathematical Refusals — {{ total_count }} canonical public records in total. Life and Metaphysics structural challenges are tracked through the [Challenge Responses lane]({{ '/results/challenge-responses/' | relative_url }}) until the dashboard data feed regenerates with the v4 schema.

<div class="v2-grid">
  <div class="v2-tile">
    <strong>{{ partial_answers | size }} partially addressed challenges</strong>
    <span>Current public response mirrors where the program has taken a visible stance without claiming final settlement.</span>
  </div>
  <div class="v2-tile">
    <strong>{{ partial_recovery | size }} partial recovery items</strong>
    <span>Recovery targets that are publicly framed but still await further build, bridge, or verification work.</span>
  </div>
  <div class="v2-tile">
    <strong>{{ not_yet_touched | size }} not-yet-touched item(s)</strong>
    <span>Public agenda obligations for which the Results mirror does not yet report a substantive program stance.</span>
  </div>
  <div class="v2-tile">
    <strong>{{ reclassified | size }} reclassified / dismissed</strong>
    <span>Items that would be shown with reasons if the public mirror had reached that state.</span>
  </div>
  <div class="v2-tile">
    <strong>{{ verified_internal | size }} internally verified / {{ externally_reviewed | size }} externally reviewed</strong>
    <span>Verification and external acceptance remain separate status surfaces.</span>
  </div>
</div>

## Filters

{% assign spine_steps = site.data.construction_spine["construction-spine-data"] %}
<div class="results-browse" style="padding: 1rem 0 0;">
  <div class="results-browse-controls" id="agenda-progress-controls" aria-label="Filter agenda progress records">
    <div class="filter-group" data-filter-group="domain">
      <span class="filter-label">Domain</span>
      <div class="filter-chips">
        <button class="filter-chip" data-filter="domain" data-value="mathematics" type="button">Mathematics</button>
        <button class="filter-chip" data-filter="domain" data-value="physics" type="button">Physics</button>
        <button class="filter-chip" data-filter="domain" data-value="life" type="button">Life</button>
        <button class="filter-chip" data-filter="domain" data-value="metaphysics" type="button">Metaphysics</button>
        <button class="filter-chip" data-filter="domain" data-value="metaphysics_philosophy" type="button">Metaphysics / Philosophy</button>
      </div>
    </div>

    <div class="filter-group" data-filter-group="item_kind">
      <span class="filter-label">Item type</span>
      <div class="filter-chips">
        <button class="filter-chip" data-filter="item_kind" data-value="problem" type="button">Structural Challenge</button>
        <button class="filter-chip" data-filter="item_kind" data-value="recovery_requirement" type="button">Core Semantics / Recovery</button>
        <button class="filter-chip" data-filter="item_kind" data-value="mathematical_refusal" type="button">Mathematical refusal</button>
      </div>
    </div>

    <div class="filter-group" data-filter-group="display_status">
      <span class="filter-label">Display status</span>
      <div class="filter-chips">
        <button class="filter-chip" data-filter="display_status" data-value="partially_addressed" type="button">Partially addressed</button>
        <button class="filter-chip" data-filter="display_status" data-value="partial" type="button">Partial</button>
        <button class="filter-chip" data-filter="display_status" data-value="not_applicable" type="button">Not applicable</button>
        <button class="filter-chip" data-filter="display_status" data-value="not_yet_classified" type="button">Not yet touched</button>
        <button class="filter-chip" data-filter="display_status" data-value="reclassified" type="button">Reclassified</button>
      </div>
    </div>

    <div class="filter-group" data-filter-group="verification_status">
      <span class="filter-label">Verification status</span>
      <div class="filter-chips">
        <button class="filter-chip" data-filter="verification_status" data-value="route_available" type="button">Route available</button>
        <button class="filter-chip" data-filter="verification_status" data-value="not_yet_mapped" type="button">Not yet mapped</button>
        <button class="filter-chip" data-filter="verification_status" data-value="pending_formal_verification" type="button">Pending formal verification</button>
        <button class="filter-chip" data-filter="verification_status" data-value="pending_bridge_verification" type="button">Pending bridge verification</button>
        <button class="filter-chip" data-filter="verification_status" data-value="pending_physics_verification" type="button">Pending physics verification</button>
        <button class="filter-chip" data-filter="verification_status" data-value="pending_life_verification" type="button">Pending life verification</button>
        <button class="filter-chip" data-filter="verification_status" data-value="pending_metaphysics_verification" type="button">Pending metaphysics verification</button>
        <button class="filter-chip" data-filter="verification_status" data-value="not_yet_verified" type="button">Not yet verified</button>
      </div>
    </div>

    <div class="filter-group" data-filter-group="external_status">
      <span class="filter-label">External status</span>
      <div class="filter-chips">
        <button class="filter-chip" data-filter="external_status" data-value="not_externally_reviewed" type="button">Not externally reviewed</button>
      </div>
    </div>

    <div class="filter-group" data-filter-group="construction_step">
      <span class="filter-label">Related construction step</span>
      <div class="filter-chips">
        {% for step in spine_steps %}
          <button class="filter-chip" data-filter="construction_step" data-value="{{ step.slug }}" type="button">{{ step.sequence }}. {{ step.short_title }}</button>
        {% endfor %}
      </div>
    </div>

    <div class="filter-group filter-group-actions">
      <div class="filter-count">
        <strong id="agenda-progress-count">{{ total_count }}</strong> of {{ total_count }} public records
      </div>
      <button class="btn-secondary btn-clear-filters" id="agenda-progress-clear-filters" type="button">Clear filters</button>
    </div>
  </div>

  <div class="results-browse-empty" id="agenda-progress-empty" hidden>
    <p>No agenda records match the current filters. <button type="button" class="btn-link" id="agenda-progress-empty-clear">Clear filters</button> to see everything.</p>
  </div>

  <ol class="results-browse-grid" id="agenda-progress-grid">
    {% for item in progress %}
      {% assign construction_slugs = item.related_construction_steps | map: "slug" | join: "," %}
      {%- comment -%}
        Wave 3: surface the v4 item-kind labels even when older dashboard
        data feeds still emit retired v1 labels.
      {%- endcomment -%}
      {% case item.item_kind %}
        {% when "problem" %}{% assign v4_kind_label = "Structural Challenge" %}
        {% when "recovery_requirement" %}{% assign v4_kind_label = "Core Semantics / Recovery" %}
        {% when "mathematical_refusal" %}{% assign v4_kind_label = "Mathematical Refusal" %}
        {% else %}{% assign v4_kind_label = item.item_kind_label %}
      {% endcase %}
      {% assign item_url = item.canonical_program_url | default: "" %}
      <li class="result-card agenda-progress-card"
          data-domain="{{ item.domain }}"
          data-item-kind="{{ item.item_kind }}"
          data-display-status="{{ item.display_status }}"
          data-verification-status="{{ item.verification_status }}"
          data-external-status="{{ item.external_status }}"
          data-construction-steps="{{ construction_slugs }}"
          data-title="{{ item.title | downcase }}">
        {% if item_url != "" %}
        <a class="result-card-link" href="{{ item.canonical_program_url | relative_url }}">
        {% else %}
        <div class="result-card-link result-card-link--inactive" aria-label="{{ item.title | escape }} route pending">
        {% endif %}
          <div class="result-card-top">
            <span class="chip chip-kind">{{ v4_kind_label }}</span>
            <span class="chip chip-status">{{ item.display_status_label }}</span>
          </div>
          <h3 class="result-card-title">{{ item.title }}</h3>
          <p class="result-card-summary">{{ item.display_domain }} agenda item with distinct internal status, verification route, and external-review state.</p>
          <div class="result-card-bottom" style="margin-bottom: 0.6rem;">
            <span class="chip chip-small">{{ item.display_domain }}</span>
            <span class="chip chip-small">Verification: {{ item.verification_status_label }}</span>
            <span class="chip chip-small">External: {{ item.external_status_label }}</span>
          </div>
          {% if item.related_construction_steps and item.related_construction_steps.size > 0 %}
            <div class="result-card-bottom" style="margin-bottom: 0.45rem;">
              {% for step in item.related_construction_steps %}
                <span class="chip chip-small chip-book">{{ step.title }}</span>
              {% endfor %}
            </div>
          {% endif %}
          <div class="result-card-bottom">
            {% if item.has_result_route %}
              <span class="chip chip-small">Result route available</span>
            {% endif %}
            {% if item.has_verify_route %}
              <span class="chip chip-small">Verify route available</span>
            {% endif %}
            {% unless item.has_result_route or item.has_verify_route %}
              <span class="chip chip-small">Route still sparse</span>
            {% endunless %}
          </div>
        {% if item_url != "" %}
        </a>
        {% else %}
        </div>
        {% endif %}
      </li>
    {% endfor %}
  </ol>
</div>

## Recently updated

<div class="v2-grid">
  {% for item in recently_updated limit: 8 %}
    {% case item.item_kind %}
      {% when "problem" %}{% assign v4_kind_label = "Structural Challenge" %}
      {% when "recovery_requirement" %}{% assign v4_kind_label = "Core Semantics / Recovery" %}
      {% when "mathematical_refusal" %}{% assign v4_kind_label = "Mathematical Refusal" %}
      {% else %}{% assign v4_kind_label = item.item_kind_label %}
    {% endcase %}
    {% assign item_url = item.canonical_program_url | default: "" %}
    {% if item_url != "" %}
    <a class="v2-tile" href="{{ item.canonical_program_url | relative_url }}">
      <strong>{{ item.title }}</strong>
      <span>{{ item.last_modified }} · {{ v4_kind_label }} · {{ item.display_status_label }}</span>
    </a>
    {% else %}
    <div class="v2-tile" aria-label="{{ item.title | escape }} route pending">
      <strong>{{ item.title }}</strong>
      <span>{{ item.last_modified }} · {{ v4_kind_label }} · {{ item.display_status_label }} · Route pending</span>
    </div>
    {% endif %}
  {% endfor %}
</div>

## Not yet touched

{% if not_yet_touched.size > 0 %}
<p>These public agenda obligations remain visible precisely because the Results lane has not yet published a substantive response, recovery state, or internally addressed account for them.</p>

<div class="v2-grid">
  {% for item in not_yet_touched %}
    {% case item.item_kind %}
      {% when "problem" %}{% assign v4_kind_label = "Structural Challenge" %}
      {% when "recovery_requirement" %}{% assign v4_kind_label = "Core Semantics / Recovery" %}
      {% when "mathematical_refusal" %}{% assign v4_kind_label = "Mathematical Refusal" %}
      {% else %}{% assign v4_kind_label = item.item_kind_label %}
    {% endcase %}
    {% assign item_url = item.canonical_program_url | default: "" %}
    {% if item_url != "" %}
    <a class="v2-tile" href="{{ item.canonical_program_url | relative_url }}">
      <strong>{{ item.title }}</strong>
      <span>{{ item.display_domain }} · {{ v4_kind_label }}</span>
    </a>
    {% else %}
    <div class="v2-tile" aria-label="{{ item.title | escape }} route pending">
      <strong>{{ item.title }}</strong>
      <span>{{ item.display_domain }} · {{ v4_kind_label }} · Route pending</span>
    </div>
    {% endif %}
  {% endfor %}
</div>
{% else %}
_No public agenda items currently sit in the “not yet touched” bucket._
{% endif %}

## Reclassified or dismissed with reason

{% if reclassified.size > 0 %}
<div class="v2-grid">
  {% for item in reclassified %}
    {% assign item_url = item.canonical_program_url | default: "" %}
    {% if item_url != "" %}
    <a class="v2-tile" href="{{ item.canonical_program_url | relative_url }}">
      <strong>{{ item.title }}</strong>
      <span>{{ item.reclassification_note | default: "Reclassified or dismissed in the public ledger." }}</span>
    </a>
    {% else %}
    <div class="v2-tile" aria-label="{{ item.title | escape }} route pending">
      <strong>{{ item.title }}</strong>
      <span>{{ item.reclassification_note | default: "Reclassified or dismissed in the public ledger." }} · Route pending</span>
    </div>
    {% endif %}
  {% endfor %}
</div>
{% else %}
_No public agenda items are currently marked as reclassified or dismissed._
{% endif %}

<script defer src="{{ '/assets/js/agenda-progress-dashboard.js' | relative_url }}"></script>
