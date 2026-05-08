---
layout: program-doc
title: "Corpus Versioning"
lane: corpus
v2_lane: corpus
permalink: /corpus/versioning/
type: "Corpus Guide"
status: "Canonical"
summary_short: "How corpus objects, public releases, errata, and registry snapshots relate over time."
right_rail:
  related:
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Corpus Changelog"
      url: /corpus/changelog/
    - title: "Errata"
      url: /publications/errata/
    - title: "Changelog"
      url: /changelog/
  meta:
    type: "Corpus Guide"
    status: "Draft"
    updated: "May 2026"
---

## Versioning stance

The corpus is living, but public claims must remain citeable. Wave 4 separates living corpus state from released public artifacts, semantic corpus changes, publication errata, and technical website release history.

Corpus Changelog entries, errata, release manifests, edition records, release artifacts, and registry snapshots together define how the public record changes over time.

## Current public surfaces

- [Corpus Changelog]({{ '/corpus/changelog/' | relative_url }}) - semantic corpus evolution.
- [Errata]({{ '/publications/errata/' | relative_url }}) - publication-facing corrections.
- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }})
- [Changelog]({{ '/changelog/' | relative_url }}) - technical/site release history.

## Snapshot model

<div class="v2-system-strip" aria-label="Corpus versioning model">
  <a href="{{ '/publications/research-monographs/' | relative_url }}">Book release</a>
  <span>-></span>
  <a href="{{ '/corpus/registry/' | relative_url }}">Registry state</a>
  <span>-></span>
  <a href="{{ '/verify/release-manifest/' | relative_url }}">Release manifest</a>
  <span>-></span>
  <a href="{{ '/publications/errata/' | relative_url }}">Errata</a>
  <span>-></span>
  <a href="{{ '/corpus/changelog/' | relative_url }}">Corpus changelog</a>
  <span>-></span>
  <a href="{{ '/changelog/' | relative_url }}">Technical changelog</a>
</div>

## Working rule

Books and public release artifacts are citeable snapshots. The registry is the living source of truth for the corpus spine. When a correction changes the interpretation, status, or dependency structure of a corpus object, the public record should expose that change through the Corpus Changelog, publication errata where needed, release notes, and manifest updates. The technical changelog remains for website and repository release history.
