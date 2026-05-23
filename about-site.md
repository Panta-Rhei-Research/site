---
layout: program-doc
title: "About this Site"
subtitle: "How to use the Panta Rhei Research Observatory"
lane: support
shell: home
type: support_page
support_type: about_site
status: canonical
last_updated: 2026-05-23
updated: "May 2026"
permalink: /about-site/
summary: "A short operational guide for reviewers, journalists, and new readers — how to navigate the Observatory, choose a route, search, inspect a claim, cite the program, and report corrections."
summary_short: "A short operational guide to navigating, searching, inspecting, citing, and contacting the Observatory."
right_rail:
  related:
  - title: Colophon
    url: /colophon/
  - title: Research Graph
    url: /research-graph/
  - title: Cite
    url: /cite/
  - title: Credits
    url: /credits/
  - title: Contact
    url: /engage/contact/
  meta:
    type: "Support page"
    scope: "About this site"
    status: "Canonical"
    updated: "May 2026"
---

<!--
  About this Site — v5 next-wave W4a (IA Doctrine v5 §8).

  Source: atlas/website/v5/panta-rhei-ia-doctrine-v5.md §8.
  Roadmap: atlas/website/briefings/v5/v5-next-wave-roadmap-2026-05-23/
           README.md (W4 · About this Site + Colophon).

  Tone (IA §8.4): no manual tone — short guide for reviewers,
  journalists, and new readers. Operational, not philosophical.

  Forward links: /colophon/ resolves in W4b; /research-log/ resolves
  in W5; /research-graph/ resolves in W6.
-->

## What this site is

The Panta Rhei Research Program is an independent open research program publishing a coherent theory of reality alongside the formal machinery used to check it. This site is the program's public observatory — every monograph, paper, note, prediction, formalization, and dataset is reachable here, with the reasoning visible.

It is **not** a marketing page, not a closed peer-review repository, and not a wiki. It is an inspectable record of an active research program. The standard you should hold it to is the standard you hold a published research artifact to.

## The eight lanes

Top-level navigation is organised into eight epistemic lanes. Each lane answers a different reader question:

- **[Discover]({{ '/discover/' | relative_url }})** — first orientation. Where is this program, what is it claiming, where do I start?
- **[Program]({{ '/program/' | relative_url }})** — what kind of research program this is, how it is governed, who runs it.
- **[Agenda]({{ '/agenda/' | relative_url }})** — what we are actively working on, what we have publicly committed to.
- **[Corpus]({{ '/corpus/' | relative_url }})** — the construction itself. Mathematical structures, derivations, conceptual scaffolding.
- **[Results]({{ '/results/' | relative_url }})** — discharged predictions and named results, with provenance.
- **[Verify]({{ '/verify/' | relative_url }})** — how each result is checked. Lean proofs, falsification packs, audit posture.
- **[Impact]({{ '/impact/' | relative_url }})** — where the program's predictions touch the wider scientific landscape.
- **[Engage]({{ '/engage/' | relative_url }})** — how to read with us, write to us, or work with us. Includes the contact route.

Lanes are stable. URLs are stable. A link to a lane page is a citable surface.

## How to choose a route

Pick the lane that matches *what you are trying to do*:

- **"I want to understand what this program claims."** → start at [Discover]({{ '/discover/' | relative_url }}), then [Corpus]({{ '/corpus/' | relative_url }}).
- **"I want to check whether a specific prediction holds."** → start at [Results]({{ '/results/' | relative_url }}), follow the link to the matching entry in [Verify]({{ '/verify/' | relative_url }}).
- **"I am writing about this program and need verifiable facts."** → start at [Media Kit]({{ '/media/' | relative_url }}) → [Journalist FAQ]({{ '/media/journalist-faq/' | relative_url }}).
- **"I want to read the books."** → start at [Publications]({{ '/publications/' | relative_url }}) → individual book pages carry the Zenodo DOI + PDF.
- **"I want to inspect the formal machinery."** → start at [Verify]({{ '/verify/' | relative_url }}) → the [TauLib]({{ '/verify/taulib/' | relative_url }}) section.

If none of those match, use Search (next section).

## Search and quick access

Press <kbd>/</kbd> anywhere on the site (or <kbd>Cmd/Ctrl</kbd>+<kbd>K</kbd>) to open the search modal. The search is powered by [Pagefind](https://pagefind.app), which indexes the full site content at build time and runs entirely in your browser — nothing is sent to a server.

Before you type, the modal shows three short orientation lists:

- **Quick access** — direct chips to FAQ, Latest Publications, Research Log, Publications, Construction Spine, Verify, Cite, and Contact.
- **Common starting points** — four first-contact-shaped questions that route to the right page.
- **Site help** — links to this page and to the [Colophon]({{ '/colophon/' | relative_url }}).

As soon as you start typing, the orientation lists collapse and Pagefind results appear in their place. The result list supports lane filter chips (All / Corpus / Results / Verify / Program) for narrowing.

If Pagefind misses what you are looking for, the modal also offers a one-click "Broader site search with Google" link that runs `site:panta-rhei.site <your query>`.

## Page tools

Most pages carry a small set of page tools, visible either in the right rail (desktop) or in the "page tools" drawer (mobile):

- **Share page** — copy the page's permalink to your clipboard.
- **Copy citation** — copy a pre-formatted citation string for the current page.
- **Reviewer note** — open a pre-filled email to the program with the page URL and a short context block, for sending a reviewer comment.
- **Download PDF dossier** — where available, a print-ready PDF version of the page.
- **Download Markdown dossier** — where available, the page's source content as portable Markdown for offline reading or quoting.
- **Related routes** — a small list of adjacent surfaces (sibling pages, parent lane, cross-linked entries).
- **Right-rail identifiers** — on publication pages, the right rail also carries the publication's DOI, ORCID(s), GitHub repository, and any other persistent identifiers (full pattern shipped in Wave 6).

Page tools are an inspection convenience, not a separate navigation system. Everything they expose is also reachable through the page itself.

## PDF / Markdown dossiers

Every Monograph and most long-form research artifacts ship both as a rendered web page and as a portable dossier:

- **PDF dossier** — typeset for print and archival reading.
- **Markdown dossier** — the page's source content as Markdown with stable headings and embedded math, suitable for offline reading, quoting, or re-rendering.

Dossier links appear in the right rail of pages that have them. If a page does not expose a dossier link, none has been generated for it yet — most non-publication pages do not need one.

## Publications, Research Log, Changelog

Three near-adjacent surfaces, distinct in scope:

| Surface | Records | When to read it |
|---|---|---|
| **[Publications]({{ '/publications/' | relative_url }})** | Finished and citable works — Monographs, Hinge Papers, Research Notes, Dossiers. | When you want to read or cite a finished artifact. |
| **[Research Log]({{ '/research-log/' | relative_url }})** | Dated public ledger of research activity — what was worked on, what landed, what was reframed. | When you want to know what the program has been doing recently. |
| **[Changelog]({{ '/changelog/' | relative_url }})** | Site and release changes — what shipped on the site itself. | When you want to know what changed on this website. |

The Research Log is the public progress journal. The Changelog is the site's release notes. The two intentionally do not overlap.

## How to inspect a claim

Every named result in [Results]({{ '/results/' | relative_url }}) carries a verification panel that links to:

- the **formal proof** (Lean source in TauLib, with the exact theorem name and a permalink to the source line),
- the **falsification pack** describing what observation or measurement would refute the claim,
- the **provenance trail** — which monograph chapter or paper the claim originates from, and which corpus entries it depends on.

The [Verify]({{ '/verify/' | relative_url }}) lane carries the cross-cutting machinery: the proof-assistant stack, the audit posture, the custom axiom inventory, and the release manifest. If you want a single page that explains *how* the program is checked, [Verify · How to verify]({{ '/verify/how-to-verify/' | relative_url }}) is that page.

## How to cite the program

The full citation guidance is on the [Cite]({{ '/cite/' | relative_url }}) page. The short version:

- **Cite an individual Monograph** by its Zenodo DOI (on the book's individual page).
- **Cite the program as a whole** using the canonical URL `https://panta-rhei.site`.
- **Cite a specific result, prediction, or note** by its canonical page URL plus the named result identifier shown on the page.
- **Cite TauLib** by its repository URL plus the theorem name.

The Cite page also has BibTeX templates for each of the above.

## How to contact or report corrections

Use the [Contact]({{ '/engage/contact/' | relative_url }}) page. Three routes:

- **General correspondence** — use the contact form.
- **Reviewer note on a specific page** — use the "Reviewer note" page tool, which pre-fills the page URL and a short context block.
- **Erratum or correction** — email the program directly (address on the Contact page). All errata are recorded openly in the [Changelog]({{ '/changelog/' | relative_url }}) and, where they affect a published artifact, linked from the artifact's page.

We read every message. We do not always reply quickly, but corrections are taken seriously and recorded openly.

## Colophon

The [Colophon]({{ '/colophon/' | relative_url }}) page records *how* the Observatory is built — the static-site stack, the search index, the metadata pipeline, the design system, and the site-facts snapshot from the most recent build.

If you want to understand the construction of this site (not the construction of the underlying program), the Colophon is the page for you.

## Research Graph

The [Research Graph]({{ '/research-graph/' | relative_url }}) page is the program's authority and provenance layer. It records, for every Monograph, Paper, Note, person, repository, and dataset, which persistent identifiers (DOI, ORCID, OSF, GitHub, Wikidata) describe it.

If you want to understand how this program connects to the wider scholarly-identifier graph, or you want machine-readable provenance for citation tooling, the Research Graph is the page for you.
