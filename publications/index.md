---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-23
updated: "May 2026"
title: "Publications"
permalink: "/publications/"
type: "Lane Root"
summary_short: "The stable public artifact shelf — four primary publication classes (Monographs · Papers · Notes · Dossiers) plus the reference and provenance surfaces (Latest · Archived · Release Artifacts · Bibliography · Errata · Cite)."
og_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
twitter_image: "/assets/images/plates/plate-07-stable-artifact-layer-og.jpg"
og_image_alt: "Scientific plate showing the Publications lane as the stable artifact layer with the four primary publication classes (Monographs, Papers, Notes, Dossiers) and the reference and provenance surfaces."
right_rail:
  related:
    -
      title: "Latest Publications"
      url: "/publications/latest/"
    -
      title: "Research Monographs"
      url: "/publications/research-monographs/"
    -
      title: "Research Papers"
      url: "/publications/research-papers/"
    -
      title: "Research Notes"
      url: "/publications/research-notes/"
    -
      title: "Research Dossiers"
      url: "/publications/research-dossiers/"
    -
      title: "Research Graph"
      url: "/research-graph/"
    -
      title: "Verify"
      url: "/verify/"
  meta:
    type: "Lane Root"
    scope: "Released artifacts · 4-class taxonomy"
    status: "Canonical"
    updated: "May 2026"
---

<!--
  Publications landing — v5 next-wave W7a refresh.
  Source: atlas/website/v5/panta-rhei-publication-taxonomy-v5-supplement.md
          (canonical taxonomy doctrine — supersedes IA Doctrine §3.3 in
          favour of a four-class primary taxonomy).
  Doctrine pinned in _data/publication_classes.yml (shipped W1).

  Four primary classes (W1 + this PR):
    1. Research Monographs    — book-length corpus artifacts
    2. Research Papers        — standalone scholarly papers
    3. Research Notes         — short scholarly artifacts
    4. Research Dossiers      — framework dossiers + translation artifacts

  Deprecated visible categories (URLs stay live for back-compat;
  W7b adds deprecation framing to the per-class index pages):
    × Anchor Documents          → reclassify per artifact (Monograph /
                                  Dossier / Paper)
    × Monograph Supplements     → fold into Corpus / Notes / Errata
    × Research Briefings        → fold into Research Dossiers
    × White Papers              → fold into Research Dossiers
-->

## What Belongs Here

The Publications lane is the stable artifact layer of the Panta Rhei Research Program.

It contains released objects that can be read, cited, downloaded, compared across editions, or used as orientation artifacts.

Publications are not the whole research system. The [Corpus]({{ '/corpus/' | relative_url }}) carries the structured research body, [Results]({{ '/results/' | relative_url }}) reports current program stances, [Verify]({{ '/verify/' | relative_url }}) exposes inspection routes, and [Impact]({{ '/impact/' | relative_url }}) maps conditional consequences. Publications provides the stable released artifacts connected to those lanes.

The deep Book → Part → Chapter reading projection now lives in [Monograph Corpus]({{ '/corpus/monograph-corpus/' | relative_url }}). The Publications lane keeps the citable monograph artifacts: DOI metadata, release status, covers, formats, and artifact classification.

For the dated public ledger of research-stream events — new artifacts, registry additions, result-status changes, formalization milestones, errata, and release packets — see the [Research Progress Log]({{ '/research-log/' | relative_url }}). Publications is the artifact shelf; the Research Log is the moving ledger. The [Research Graph]({{ '/research-graph/' | relative_url }}) exposes the persistent identifiers (DOI · ORCID · OSF · GitHub) for every entity here.

<p class="eyebrow">The four primary publication classes</p>

## The Stable Artifact Layer

{% include scientific-plate.html id="plate-07-stable-artifact-layer" class="scientific-plate--stable-artifact-layer" loading="lazy" %}

Publications classifies artifacts by **scholarly function** — what kind of thing the reader is looking at and how it should be cited. Four primary classes cover everything new the program publishes:

> **Books. Papers. Notes. Dossiers.**

A fifth adjacent layer, [Research Code]({{ '/verify/taulib/' | relative_url }}) (TauLib), is a software and formalization-publication surface treated separately under [Verify]({{ '/verify/' | relative_url }}). Artifact class is not claim status — a Research Paper can be active or superseded, a Monograph can be in its first or third edition.

<div class="btn-group section-ctas">
  <a class="btn" href="{{ '/publications/latest/' | relative_url }}">Latest Publications</a>
  <a class="btn" href="{{ '/publications/research-monographs/' | relative_url }}">Browse Research Monographs</a>
  <a class="btn" href="{{ '/publications/research-papers/' | relative_url }}">Read Research Papers</a>
  <a class="btn" href="{{ '/publications/research-notes/' | relative_url }}">Read Research Notes</a>
  <a class="btn" href="{{ '/publications/research-dossiers/' | relative_url }}">Open Research Dossiers</a>
</div>

## Primary publication classes

<ul class="v2-grid v2-card-list">
  <li><article><a class="v2-tile" href="{{ '/publications/research-monographs/' | relative_url }}"><h3>Research Monographs</h3><p>Book-length corpus artifacts. The long-form narrative backbone of the program, including the Seven Books and the associated full-length book <em>Out of Context</em>.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/research-papers/' | relative_url }}"><h3>Research Papers</h3><p>Standalone scholarly papers carrying primary technical research contributions. Each paper stands on its own claim, with its own DOI and proof or argument structure.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/research-notes/' | relative_url }}"><h3>Research Notes</h3><p>Shorter scholarly artifacts from the ongoing research stream — frontier-paper responses, comparative readings, pre-registration notes, and current-stance clarifications.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/research-dossiers/' | relative_url }}"><h3>Research Dossiers</h3><p>Framework dossiers, reading guides, translation artifacts, and public-good briefings. The class that holds <em>The Construction Spine</em> and the Public-Good Briefing series.</p></a></article></li>
</ul>

## Reference and provenance

<ul class="v2-grid v2-card-list">
  <li><article><a class="v2-tile" href="{{ '/publications/latest/' | relative_url }}"><h3>Latest Publications</h3><p>Corpus-backed stream of released, superseded, and archived publication artifacts across all four classes.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/release-artifacts/' | relative_url }}"><h3>Release Artifacts</h3><p>Version, provenance, correction, manifest, changelog, and archive surfaces — the release-governance layer.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/archived/' | relative_url }}"><h3>Archived Releases</h3><p>Superseded releases, edition records, and retired pre-canon white papers preserved for provenance.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/bibliography/' | relative_url }}"><h3>Bibliography</h3><p>The cross-cutting references used by the program — classical and modern sources linked to canonical publisher, DOI, or arXiv record.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/cite/' | relative_url }}"><h3>Cite</h3><p>How to cite the program — individual monographs by Zenodo DOI, the program by canonical URL, TauLib by repository plus theorem name.</p></a></article></li>
</ul>

## Glossary

### Research Monographs

Research Monographs are book-length corpus artifacts and official editions of the Panta Rhei monograph series. They are the long-form narrative backbone of the program — full sustained construction, not introductory primers. Their open reading projection lives at [Monograph Corpus]({{ '/corpus/monograph-corpus/' | relative_url }}); the citable per-book artifact pages live here under [Research Monographs]({{ '/publications/research-monographs/' | relative_url }}). Each Monograph carries a Zenodo DOI on its right-rail identifier box.

### Research Papers

Research Papers are standalone scholarly papers carrying primary technical research contributions. Each paper states, proves, derives, or argues for original research claims in a paper-like scholarly format and is intended to be peer-reviewed on its own. The current paper bundle is the Hinge series (nine standalone papers, all DOI-minted).

### Research Notes

Research Notes are shorter scholarly artifacts from the ongoing research stream. They may respond to frontier papers, compare external theories with Category τ, pre-register falsification commitments, place predictions against observations, or clarify a current program stance. Notes are typically shorter than Papers and faster to publish.

### Research Dossiers

Research Dossiers are framework dossiers, reading guides, translation artifacts, and conditional public-good briefings. They organise existing Results, assumptions, and verification status for a domain, institution, public-good context, or applied audience without re-deriving the underlying claims. The current canonical dossier is *[The Panta Rhei Construction Spine]({{ '/corpus/construction-spine/' | relative_url }})*; the charter dossier is *[Standing in the Inquiry of Being]({{ '/program/about/standing-in-the-inquiry-of-being/' | relative_url }})*.

### Reference and provenance surfaces

The auxiliary surfaces — Latest Publications, Release Artifacts, Archived Releases, Bibliography, Errata, Cite — are reference and provenance layers across the four primary classes, not parallel publication classes themselves.

### Notes on retired visible categories

Previously the lane exposed nine visible categories (Anchor Documents, Monograph Supplements, Research Briefings, White Papers, etc.). The v5 taxonomy consolidates these into the four primary classes above. Existing URLs continue to resolve — readers landing on a deprecated category page see a pointer to the new home for those artifacts. See the [Publication Taxonomy v5 Supplement](https://github.com/Panta-Rhei-Research/atlas/blob/main/website/v5/panta-rhei-publication-taxonomy-v5-supplement.md) for the full migration rationale.

## How we classify new artifacts

Every new publication artifact must first answer which of the four primary classes it belongs to.

1. Is it a full book-length canonical exposition? → **Research Monograph**.
2. Does it carry a primary original technical research contribution as a standalone paper? → **Research Paper**.
3. Is it a short scholarly response, comparison, pre-registration, or falsification note? → **Research Note**.
4. Is it a framework dossier, reading guide, translation artifact, or public-good briefing? → **Research Dossier**.

If the artifact is a release-governance surface (version, provenance, correction, manifest, changelog, archive state), it is a **Release Artifact**, not a publication class. If the artifact is a formalization / software module, it is **Research Code** (TauLib), not a prose publication.

If an artifact fits none of these, a new class should only be introduced after an explicit editorial justification per the [Publication Taxonomy v5 Supplement](https://github.com/Panta-Rhei-Research/atlas/blob/main/website/v5/panta-rhei-publication-taxonomy-v5-supplement.md).

## Artifact classification matrix

<table class="artifact-classification-matrix">
  <caption>Publication artifact classification matrix · v5 four-class taxonomy</caption>
  <thead>
    <tr>
      <th scope="col">Artifact</th>
      <th scope="col">Class</th>
      <th scope="col">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Book I – Book VII</th>
      <td>Research Monograph</td>
      <td>The Seven Books · Zenodo DOI per book</td>
    </tr>
    <tr>
      <th scope="row">Out of Context</th>
      <td>Research Monograph</td>
      <td>Associated book · not part of the Seven Books</td>
    </tr>
    <tr>
      <th scope="row">Hinge series (nine papers)</th>
      <td>Research Paper</td>
      <td>Standalone peer-review bundle · DOI per paper</td>
    </tr>
    <tr>
      <th scope="row">Spring 2026 note batch (five)</th>
      <td>Research Note</td>
      <td>Structural-prior readings · Zenodo DOIs</td>
    </tr>
    <tr>
      <th scope="row">May 2026 categorical readings (four)</th>
      <td>Research Note</td>
      <td>τ-readout / categorical-reading notes · OSF nodes</td>
    </tr>
    <tr>
      <th scope="row">The Panta Rhei Construction Spine</th>
      <td>Research Dossier</td>
      <td>Framework dossier · OSF + live observatory route</td>
    </tr>
    <tr>
      <th scope="row">Standing in the Inquiry of Being</th>
      <td>Research Dossier</td>
      <td>Charter essay</td>
    </tr>
    <tr>
      <th scope="row">Public-Good Briefings</th>
      <td>Research Dossier</td>
      <td>Conditional public-good scenario dossiers</td>
    </tr>
    <tr>
      <th scope="row">Numerical Physics Ledger</th>
      <td>Folded into Corpus + Errata</td>
      <td>Former Monograph Supplement · per Supplement §3.1</td>
    </tr>
    <tr>
      <th scope="row">Release Manifest</th>
      <td>Release Artifact</td>
      <td>Cross-cutting governance — not a publication class</td>
    </tr>
    <tr>
      <th scope="row">Errata</th>
      <td>Release Artifact</td>
      <td>Correction stream — not a publication class</td>
    </tr>
  </tbody>
</table>

## Suggested reading order

1. Start with the [Latest Publications]({{ '/publications/latest/' | relative_url }}) stream when you want a chronological view of what has shipped.
2. Use the [Research Monographs]({{ '/publications/research-monographs/' | relative_url }}) for sustained canonical exposition.
3. Use the [Research Papers]({{ '/publications/research-papers/' | relative_url }}) for the standalone peer-review-ready bundle — especially the Hinge series.
4. Use the [Research Notes]({{ '/publications/research-notes/' | relative_url }}) for current scholarly responses, comparisons, and pre-registration notes.
5. Use the [Research Dossiers]({{ '/publications/research-dossiers/' | relative_url }}) for framework reading guides — the Construction Spine and the charter essay.
6. Use [Release Artifacts]({{ '/publications/release-artifacts/' | relative_url }}) to inspect version status, errata, and archived releases.
