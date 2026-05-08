---
layout: program-doc
title: "Errata"
lane: publications
permalink: /publications/errata/
summary_short: "Public changelog for substantial corrections to the Panta Rhei 2nd Edition books, verification surfaces, registry entries, and associated publications."
summary_cards:
  - title: "Substantial only"
    body: "Entries here are corrections that affect a registered theorem, definition, registry ID, downstream citation, or public verification surface."
  - title: "Append-only"
    body: "Issued errata are never deleted. Superseded entries remain visible and point to their replacement."
  - title: "Active record"
    body: "Four active errata are currently projected from Corpus Wave 4 governance metadata."
right_rail:
  related:
    - title: "Publications Overview"
      url: /publications/
    - title: "The Seven Books"
      url: /publications/books/
    - title: "The Panta Rhei Conspectus"
      url: /publications/conspectus/
    - title: "Verify"
      url: /verify/
  meta:
    type: "Public Changelog"
    scope: "2nd Edition corpus"
    status: "Active"
    updated: "May 2026"
---

## Purpose

This page records **substantial corrections** to the published 2nd Edition of the *Panta Rhei* monograph series and its public companion surfaces. A correction appears here when it changes a registered theorem, a definition used downstream, a registry object, a citation target, or a public verification claim.

Purely typographical fixes are intentionally excluded from this page. The purpose is not to make ordinary copy-editing visible; it is to keep the public mathematical and verification record citeable.

## Issued Errata

{% assign errata = site.data.corpus.governance.errata.errata | sort: "erratum_id" %}
{% for entry in errata %}
### {{ entry.erratum_id }} — {{ entry.affected }}

| Field | Value |
|---|---|
| Issued | {{ entry.issued }} |
| Status | {{ entry.status }} |
| Severity | {{ entry.severity }} |
| Change class | {{ entry.change_class }} |
{% if entry.registry_ids.size > 0 %}
| Registry anchors | {% for reg_id in entry.registry_ids %}[{{ reg_id }}]({{ '/registry/object/' | append: reg_id | append: '/' | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %} |
{% endif %}

{{ entry.summary }}

**Correction.** {{ entry.correction }}

{% if entry.book_slug and entry.book_slug != "" %}
[Book-specific errata page]({{ '/publications/books/' | append: entry.book_slug | append: '/errata/' | relative_url }})
{% endif %}

{% endfor %}

## Status Convention

- **Active** means the correction is citeable and should be used when reading or quoting the affected material.
- **Superseded** means a later erratum refines or replaces the correction while preserving the historical record.
- **Applied** means the correction has landed in a later print run, registry release, or verification artifact.

## Citation Guidance

When citing affected material, cite the original book location and the relevant erratum ID together. Example: *Book I, Theorem I.T05, as corrected by ERRATUM-001*.

## Projection Source

This page is rendered from Corpus governance metadata. The Publications repository mirrors generated errata snapshots for cloneable artifact provenance, but Corpus owns the semantic errata source.
