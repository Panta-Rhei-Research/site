---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-23
updated: "May 2026"
title: "Research Dossiers"
permalink: "/publications/research-dossiers/"
type: "Publication Category"
summary_short: "Framework dossiers, reading guides, translation artifacts, and public-good briefings — the fourth primary publication class."
summary: "Research Dossiers are the program's framework dossiers, reading guides, translation artifacts, and conditional public-good briefings. They organise existing Results, assumptions, and verification status for a specific reader without re-deriving the underlying claims."
right_rail:
  related:
    -
      title: "Publications"
      url: "/publications/"
    -
      title: "The Construction Spine"
      url: "/corpus/construction-spine/"
    -
      title: "Standing in the Inquiry of Being"
      url: "/program/about/standing-in-the-inquiry-of-being/"
    -
      title: "Public-Good Briefings"
      url: "/publications/research-briefings/public-good/"
    -
      title: "Research Graph"
      url: "/research-graph/"
  meta:
    type: "Publication Category"
    scope: "Framework dossiers + translation artifacts + public-good briefings"
    status: "Canonical"
    updated: "May 2026"
---

<!--
  Research Dossiers — v5 next-wave W7a · new visible category.
  Source: atlas/website/v5/panta-rhei-publication-taxonomy-v5-supplement.md §3.4.

  This page is the canonical index for the Research Dossier class —
  the fourth primary publication class introduced in the v5
  taxonomy migration. It folds in three previously-separate visible
  categories:

    Research Briefings  → Research Dossier (Briefing subtype)
    White Papers        → Research Dossier (White Paper subtype where
                          appropriate, otherwise reclassify as Paper)
    Framework dossiers  → Research Dossier (Framework subtype) — eg
                          The Construction Spine

  Existing URLs for the deprecated categories still resolve; W7b
  adds visible "folded into Research Dossiers" pointers on the
  deprecated index pages.
-->

## What this class records

**Research Dossiers** are framework dossiers, reading guides, translation artifacts, and conditional public-good briefings. They organise existing Results, assumptions, and verification status for a specific reader — a domain expert, an institution, a journalist, a public-good context, an applied audience — without re-deriving the underlying claims.

A Dossier is the right answer when an artifact:

- assembles existing Results into a coherent route for a named reader,
- translates the program's stance on a topic for a public-good or applied context,
- provides a reading guide across multiple Papers, Notes, or Monograph chapters,
- documents the construction or charter of the program at a level above any individual artifact.

A Dossier is the wrong answer when the artifact carries an original technical contribution (that is a [Research Paper]({{ '/publications/research-papers/' | relative_url }})), a focused short response or comparison (that is a [Research Note]({{ '/publications/research-notes/' | relative_url }})), or a release-governance surface (that is a Release Artifact).

## Current dossiers

<ul class="v2-grid v2-card-list">
  <li><article><a class="v2-tile" href="{{ '/corpus/construction-spine/' | relative_url }}"><h3>The Panta Rhei Construction Spine</h3><p>Framework dossier · OSF + live observatory route. The flagship reading guide assembling the program's construction in step-order from kernel to readout, with the 100-step routing ledger.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/program/about/standing-in-the-inquiry-of-being/' | relative_url }}"><h3>Standing in the Inquiry of Being</h3><p>Charter essay · the dossier that grounds the program's stance and methodology — the charter that the Construction Spine refers to as canonical context.</p></a></article></li>
  <li><article><a class="v2-tile" href="{{ '/publications/research-briefings/public-good/' | relative_url }}"><h3>Public-Good Briefings</h3><p>Conditional scenario dossiers — a family of dossiers focused on what becomes possible under specific Results, framed as conditional public-good consequences rather than validation claims or deployment commitments.</p></a></article></li>
</ul>

## Dossier subtypes

The Research Dossier class covers three working subtypes:

| Subtype | Reader | Role |
|---|---|---|
| **Framework dossier** | Reviewer / structural reader | Assembles existing Results + Corpus into a step-ordered reading guide across the construction. *(Example: The Construction Spine.)* |
| **Charter dossier** | First-contact reader / institutional reviewer | Records the program's stance, methodology, and standing in the wider inquiry. *(Example: Standing in the Inquiry of Being.)* |
| **Public-Good Briefing** | Public-good audience / policy-adjacent reviewer | Translates a Result or cluster of Results into a conditional public-good scenario. Not a validation claim, not a deployment proposal — a conditional scenario dossier. |

A future "Translation Dossier" subtype is reserved for domain-facing reading guides that translate Corpus content for specialist audiences (mathematical physicists, formal-methods researchers, philosophers of science) without re-deriving the underlying claims.

## Distinction from Research Papers and Research Notes

| Class | Carries | Best read for |
|---|---|---|
| Research Paper | Original technical contribution | Reviewing the program's standalone claims |
| Research Note | Focused short response, comparison, pre-registration, or stance clarification | Reading recent scholarly responses to frontier work |
| **Research Dossier** | Existing Results assembled or translated for a named reader | Choosing a reading route, understanding the program's posture |

A Dossier never carries an original claim that has not already been published elsewhere in the program. If it would, the artifact should be re-classed as a Paper or Note and the Dossier should cite that artifact.

## Previously visible categories that fold into this class

Per the [Publication Taxonomy v5 Supplement](https://github.com/Panta-Rhei-Research/atlas/blob/main/website/v5/panta-rhei-publication-taxonomy-v5-supplement.md) §3.4, two previously-separate visible categories fold into the Research Dossier class:

- **Research Briefings** — the old visible category becomes the Public-Good Briefing subtype of Research Dossier. The existing [`/publications/research-briefings/`]({{ '/publications/research-briefings/' | relative_url }}) URL continues to resolve and now carries a pointer to this class index.
- **White Papers** — the older "white paper" framing becomes either Research Dossier (framework / translation subtype) or, where the artifact carries an original claim, Research Paper. The existing [`/publications/white-papers/`]({{ '/publications/white-papers/' | relative_url }}) URL continues to resolve as an archived index.

## Identifiers

Every Research Dossier carries an entry in the [Research Graph]({{ '/research-graph/' | relative_url }}) with its persistent identifiers (DOI on Zenodo or OSF, author ORCIDs, repository where applicable, Wikidata Q-item where minted). The right-rail identifier box on each dossier page lists the same identifiers inline, so the reader can cite the dossier without leaving the page.
