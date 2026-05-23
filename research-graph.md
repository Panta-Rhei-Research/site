---
layout: research-graph
title: "Research Graph"
subtitle: "Identifiers, authority records, publications, people, software, and provenance routes"
lane: support
shell: home
type: support_page
support_type: research_graph
status: canonical
last_updated: 2026-05-23
updated: "May 2026"
permalink: /research-graph/
section: "Research Graph"
summary: "The Research Graph is the program's authority and provenance layer — every monograph, paper, note, dossier, person, repository, and dataset, with the persistent identifiers (DOI, ORCID, OSF, GitHub, Wikidata) that describe each entity."
summary_short: "The program's authority + provenance layer — local IDs, external identifiers (DOI · ORCID · OSF · GitHub · Wikidata), and a downloadable manifest."
summary_cards:
- title: "Local first, Wikidata where appropriate"
  body: "Every entity carries a stable local prrp: ID. Wikidata Q-items are added once an entity meets Wikidata's notability and sourcing expectations — Wikidata is an authority layer, not a navigation menu."
- title: "Identifiers on every page"
  body: "Publication, person, software, and program pages carry right-rail identifier boxes (DOI, ORCID, OSF, GitHub, Wikidata) — the page-level surface of this graph."
- title: "Machine-readable"
  body: "JSON-LD is emitted page by page (CollectionPage here, ScholarlyArticle on papers, Book on monographs, Person on founders, etc.). A flat manifest projection is downloadable below."
right_rail:
  related:
  - title: About this Site
    url: /about-site/
  - title: Colophon
    url: /colophon/
  - title: Credits
    url: /credits/
  - title: Cite
    url: /cite/
  - title: Publications
    url: /publications/
  meta:
    type: "Support page"
    scope: "Authority and provenance layer"
    status: "Canonical"
    updated: "May 2026"
---

<!--
  Research Graph — v5 next-wave W6a (IA §10).
  Source: atlas/website/v5/panta-rhei-ia-doctrine-v5.md §10.
  Data: _data/research_graph.yml.
  17 recommended sections per IA §10.6 — the data-driven entity tables
  render in the layout (_layouts/research-graph.html); the prose
  sections below (What this graph is · Authority layers used · Local
  IDs · How identifiers appear on pages · JSON-LD · SPARQL examples ·
  Manifest download · Correction policy) live here.

  The data tables are: People, Program/Observatory, Monographs,
  Research Papers, Research Notes, Dossiers, Software/formalization,
  and the Authority layers block (active + deprecated).

  W6b will extend this surface area with per-publication identifier
  right-rail boxes; this PR ships the central /research-graph/ page
  and the manifest backfill.
-->

## What this graph is

The Panta Rhei Research Program publishes alongside the formal machinery used to check it. The **Research Graph** is the layer that connects every monograph, paper, note, dossier, person, repository, and dataset to the persistent identifiers that describe them — DOIs, ORCIDs, OSF nodes, GitHub repositories, and Wikidata Q-items where they exist.

The graph has three public surfaces:

1. **Machine-readable metadata** — JSON-LD on every page, emitted according to the page's type (ScholarlyArticle on Hinge Papers, Book on Monographs, Person on Founders, CollectionPage on this page).
2. **Human-visible identifiers** — right-rail identifier boxes on publication, person, program, and software pages.
3. **This page** — the central overview of every entity in the graph and the authority layers used to describe it.

## Authority layers used

External authority registries used (or deprecated) by the program are listed in the **Authority layers** table below. The doctrine guiding which registries get used is from [IA §10.4](https://github.com/Panta-Rhei-Research/atlas): _Wikidata is an authority layer, not a navigation menu_. The website remains the Observatory layer; the local research graph remains the control layer; Wikidata Q-items are public authority nodes used where they are appropriate, notable, referenced, and stable.

For ordinary website pages — Construction Spine steps, internal registry items, FAQ, About this Site, Colophon, UI surfaces — local IDs are preferred and no external Q-item is sought.

## Local Panta Rhei IDs

Every entity in the graph carries a stable local identifier in the namespace `prrp:` (Panta Rhei Research Program). The pattern, per [IA §10.5](https://github.com/Panta-Rhei-Research/atlas), is:

```text
prrp:program:panta-rhei
prrp:person:thorsten-fuchs
prrp:person:anna-sophie-fuchs
prrp:publication:book-i
prrp:publication:paper-hyperfactorization-theorem
prrp:publication:note-semantic-space-has-a-shape
prrp:publication:dossier-construction-spine
prrp:software:taulib
prrp:website:observatory
prrp:registry:item:...
prrp:page:...
```

Local IDs are stable across renames, redirects, and class migrations (W7 will migrate publication classes; the local IDs stay).

## How identifiers appear on pages

On a publication page (Monograph, Hinge Paper, Research Note, Dossier), the right rail carries an **identifier box** listing every persistent identifier the entity has: DOI, ORCID(s) of the authors, OSF node where applicable, GitHub repository where applicable, Wikidata Q-item where minted. The boxes are uniform — the same box on every publication page, the same order, the same icon set.

W6b is the wave that ships these per-page identifier boxes. This page (W6a) is the central authority layer; W6b makes that layer visible on every entity page.

## JSON-LD and structured metadata

Every page emits JSON-LD structured data per the page-type registry (`_data/page_types.yml`, shipped in W1). The registry maps each page type to a Schema.org type:

| Page type | Schema.org type |
|---|---|
| `lane_overview` | `WebPage` |
| `publication` | `ScholarlyArticle` / `Book` / `CreativeWork` |
| `software` | `SoftwareSourceCode` / `SoftwareApplication` |
| `person` | `Person` |
| `organization` | `ResearchOrganization` |
| `faq` | `FAQPage` |
| `research_log` | `CollectionPage` |
| `research_graph` | `CollectionPage` / `Dataset` *(this page)* |
| `colophon` | `WebPage` |
| `about_site` | `WebPage` |

The JSON-LD pipeline lives in `_includes/seo-jsonld.html`. Author Persons (both founders, both with ORCIDs) and the publisher Organization (the program) are emitted as nested objects on every page that has them.

## SPARQL examples

Once the program's entities have Wikidata Q-items, the graph becomes queryable via SPARQL. A representative query (illustrative — Q-items will be added as they are minted):

```sparql
# Find all publications authored by Thorsten Fuchs that have a DOI
SELECT ?work ?workLabel ?doi WHERE {
  ?work wdt:P50 wd:Qxxxxxxxx ;       # author: Thorsten Fuchs (Q-item pending)
        wdt:P356 ?doi .              # property: DOI
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```

Until Q-items are minted, the same query is answered locally from this graph's manifest (see [Manifest download](#manifest-download) below).

## Manifest download

The full graph is available as a downloadable manifest in two formats:

- **YAML** (canonical, hand-maintained): [`/_data/research_graph.yml`](https://github.com/Panta-Rhei-Research/site/blob/main/_data/research_graph.yml) (GitHub source)
- **JSON** (generated, machine-friendly): [`/assets/research-graph.json`]({{ '/assets/research-graph.json' | relative_url }}) (build-time projection)

The YAML manifest is the source of truth; the JSON projection regenerates on every site build. Both contain the same data — entities + authority_layers — and are licensed under the same CC BY 4.0 terms as the rest of the site content.

## Correction policy for identifiers

If you find an incorrect identifier, an outdated DOI, a mis-attributed ORCID, or a missing reference, please open an issue on the [site repository](https://github.com/Panta-Rhei-Research/site) or use the [Contact]({{ '/engage/contact/' | relative_url }}) page. Identifier corrections are taken seriously — a wrong DOI breaks citation tooling.

When a correction lands, the canonical YAML manifest is updated in the same commit; the JSON projection regenerates on the next build; downstream JSON-LD on every affected page picks up the new value automatically.
