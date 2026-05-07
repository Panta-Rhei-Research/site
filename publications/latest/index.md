---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-08
updated: "May 2026"
title: "Latest Publications"
permalink: "/publications/latest/"
type: "Publication Stream"
summary_short: "Corpus-backed stream of released and archived publication artifacts."
right_rail:
  related:
    -
      title: "Publications"
      url: "/publications/"
    -
      title: "Research Papers"
      url: "/publications/research-papers/"
    -
      title: "Research Notes"
      url: "/publications/research-notes/"
    -
      title: "White Papers"
      url: "/publications/white-papers/"
    -
      title: "Publication Notifications"
      url: "/engage/follow-the-research/"
  meta:
    type: "Publication Stream"
    source: "Corpus metadata"
    status: "Canonical"
    updated: "May 2026"
---

## Corpus-Backed Publication Stream

This page lists the latest released, superseded, and archived publication artifacts currently exposed by the public Publications metadata projection.

<div class="notice note"><strong>Artifact stream, not news.</strong> This route is a citable-publication and provenance stream. It records released artifacts and their metadata; it is not a news feed, activity feed, or claim-status shortcut.</div>

{% assign latest_publications = site.data.corpus.latest_publications.publications %}
{% assign released_count = latest_publications | where: "status", "released" | size %}
{% assign superseded_count = latest_publications | where: "status", "superseded" | size %}
{% assign archived_count = latest_publications | where: "status", "archived" | size %}

<div class="summary-cards">
  <div class="summary-card"><div class="summary-card-title">{{ latest_publications | size }}</div><div class="summary-card-body">public artifact records</div></div>
  <div class="summary-card"><div class="summary-card-title">{{ released_count }}</div><div class="summary-card-body">released</div></div>
  <div class="summary-card"><div class="summary-card-title">{{ superseded_count | plus: archived_count }}</div><div class="summary-card-body">superseded / archived</div></div>
</div>

## Latest Artifacts

<ul class="pub-card-grid">
{% for item in latest_publications %}
  {% assign item_url = item.website_url | default: item.canonical_url %}
  {% assign item_summary = item.summary_short | default: item.abstract %}
  {% if item_summary contains "{%" %}
    {% assign item_summary = item.claim_boundary.claim | default: item.title %}
  {% endif %}
  <li>
    <article class="pub-card">
      <div class="pub-card__body">
        <p class="eyebrow">{{ item.type_label }} · {{ item.release_date }} · {{ item.status | replace: "_", " " | capitalize }}</p>
        <h3 class="pub-card__title">
          {% if item_url and item_url != "" %}
            <a href="{{ item_url }}">{{ item.title }}</a>
          {% else %}
            {{ item.title }}
          {% endif %}
        </h3>
        {% if item.subtitle and item.subtitle != "" %}
          <p class="pub-card__meta"><span>{{ item.subtitle }}</span></p>
        {% endif %}
        <p class="pub-card__summary">{{ item_summary | strip_html | truncate: 280 }}</p>
        <p class="pub-card__meta">
          <span>{{ item.publication_id | upcase }}</span>
          <span>{{ item.artifact_availability | replace: "_", " " }}</span>
          <span>{{ item.route_status | replace: "_", " " }}</span>
        </p>
        <div class="pub-card__actions">
          {% if item_url and item_url != "" %}<a href="{{ item_url }}" class="chip chip-small">Page</a>{% endif %}
          {% if item.files.pdf_url and item.files.pdf_url != "" %}<a href="{{ item.files.pdf_url }}" class="chip chip-small">PDF</a>{% endif %}
          {% if item.identifiers.doi_url and item.identifiers.doi_url != "" %}<a href="{{ item.identifiers.doi_url }}" class="chip chip-small" rel="noopener">DOI</a>{% endif %}
          {% if item.github_path and item.github_path != "" %}<a href="https://github.com/Panta-Rhei-Research/publications/tree/main/{{ item.github_path }}" class="chip chip-small" rel="noopener">GitHub mirror</a>{% endif %}
        </div>
      </div>
    </article>
  </li>
{% endfor %}
</ul>

## Projection Metadata

- Generated from: `corpus/data/publications/publications.yml`
- Projection version: `v0.1`
- Canonical metadata source: `corpus/data`
- Artifact bytes, checksums, and OpenTimestamps receipts remain owned by the public `publications` repository.
