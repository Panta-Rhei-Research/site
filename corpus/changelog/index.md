---
layout: program-doc
title: "Corpus Changelog"
lane: corpus
v2_lane: corpus
permalink: /corpus/changelog/
type: "Corpus Guide"
status: "Canonical"
summary_short: "Curated public record of meaningful semantic Corpus corrections, clarifications, status changes, bridge-boundary updates, and publication errata links."
summary_cards:
  - title: "Semantic record"
    body: "This page records meaningful changes to corpus state, not every repository commit or typographic polish."
  - title: "Corpus first"
    body: "Semantic corrections are handled in Corpus and then propagated to website, TauLib, publications, or errata surfaces as needed."
  - title: "Public trace"
    body: "GitHub Issues and Discussions may hold working history; this page is the curated public record."
right_rail:
  related:
    - title: "Corpus Versioning"
      url: /corpus/versioning/
    - title: "Submit Corrections"
      url: /engage/corrections/
    - title: "Publication Errata"
      url: /publications/errata/
    - title: "Technical Changelog"
      url: /changelog/
    - title: "Release Manifest"
      url: /verify/release-manifest/
  meta:
    type: "Corpus Changelog"
    status: "Canonical"
    updated: "May 2026"
tags:
  - corpus
  - changelog
  - corrections
  - change-control
  - public-record
---

{% assign changelog_data = site.data.corpus.governance.corpus_changelog %}
{% assign entries = changelog_data.entries %}

## Purpose

The Corpus Changelog records meaningful updates to the Panta Rhei corpus:
clarifications, corrections, prior-art additions, result-status changes,
bridge-boundary updates, formalization-related changes, and publication errata
that affect the semantic research record.

It does not list every typographic edit, technical deployment, route polish, or
repository-level change. Those belong in the technical [Changelog]({{ '/changelog/' | relative_url }}) when public release history needs to be recorded.

## Current Public Record

{% if entries and entries.size > 0 %}
<div class="v2-stack">
{% for entry in entries %}
  <article class="content-card">
    <p class="eyebrow">{{ entry.date }} · {{ entry.severity_class }} · {{ entry.type | replace: "_", " " | capitalize }}</p>
    <h2>{{ entry.title }}</h2>
    <p>{{ entry.summary }}</p>
    <p><strong>Release:</strong> <code>{{ entry.release }}</code> · <strong>Status:</strong> <code>{{ entry.status }}</code></p>
    {% if entry.related_errata and entry.related_errata.size > 0 %}
    <p><strong>Related errata:</strong> {% for erratum_id in entry.related_errata %}<a href="{{ '/publications/errata/' | relative_url }}"><code>{{ erratum_id }}</code></a>{% unless forloop.last %}, {% endunless %}{% endfor %}</p>
    {% endif %}
  </article>
{% endfor %}
</div>
{% else %}
<div class="content-card">
  <h2>No substantive post-outreach Corpus changes logged yet</h2>
  <p>No released semantic Corpus Changelog entries are currently projected. When public review leads to a meaningful correction, clarification, prior-art addition, result-status change, bridge-boundary update, formalization update, or publication erratum, it will be recorded here.</p>
</div>
{% endif %}

## What Gets Logged Here

- claim-boundary clarifications;
- registry, theorem, proof-dependency, formula, or numerical corrections;
- result-status and challenge-response revisions;
- bridge-boundary changes;
- formalization-related updates that affect public interpretation;
- publication or monograph errata that affect the corpus.

Small copy polish can happen without a Corpus Changelog entry. Meaningful
changes to public interpretation should be traceable.

## How To Submit Corrections

Use [Corrections]({{ '/engage/corrections/' | relative_url }}) for routing guidance. Public questions and critique usually begin in GitHub Discussions; concrete defects use Issues; concrete fixes use Pull Requests; private, sensitive, media, or institutional feedback should use email.
