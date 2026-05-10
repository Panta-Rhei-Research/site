---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-10
updated: "May 2026"
title: "WP003 — TauLib Technical Overview"
title_plain: "TauLib Technical Overview"
subtitle: "Lean 4 formalization layer, release manifest, and trust budget"
permalink: "/publications/anchor-documents/wp003-taulib-technical-overview/"
type: "White Paper"
summary_short: "Canonical v1.0 technical overview of TauLib as the Lean 4 formalization layer and Verify/TauLib inspection route."
right_rail:
  related:
    -
      title: "Download PDF"
      url: "/assets/pdfs/anchor-documents/wp003-taulib-technical-overview.pdf"
    -
      title: "Anchor Documents"
      url: "/publications/anchor-documents/"
    -
      title: "TauLib"
      url: "/corpus/taulib/"
    -
      title: "Verify TauLib"
      url: "/verify/taulib/"
    -
      title: "Release Manifest"
      url: "/verify/release-manifest/"
    -
      title: "Generated Docs"
      url: "https://taulib.panta-rhei.site/"
  meta:
    type: "White Paper"
    status: "Canonical v1.0"
    updated: "May 2026"
---

{% assign doc = site.data.publications.anchor_documents.documents | where: "id", "wp003" | first %}

## Canonical Artifact

*TauLib Technical Overview* (WP003) is the canonical technical white paper for
the TauLib Lean 4 formalization layer. It explains what TauLib is, how its
architecture is inspected, what the current Release Manifest pins, and how the
Verify lane exposes the trust budget around the release.

The Technical Overview is deliberately narrower than the *τ-Theory Executive
Synopsis* (WP002). It does not restate the whole theory construction. It
routes technically minded readers into the formalization surface: repository,
generated docs, release manifest, no-sorry check, custom axiom inventory, TCB
disclosure, Registry correspondence, and review workflow.

<div class="btn-group section-ctas">
  <a class="btn" href="{{ doc.pdf_path | relative_url }}">Download PDF</a>
  <a class="btn" href="/verify/taulib/">Open Verify/TauLib</a>
  <a class="btn" href="https://github.com/Panta-Rhei-Research/taulib">Inspect TauLib Repository</a>
  <a class="btn" href="https://taulib.panta-rhei.site/">Generated Docs</a>
</div>

## Release Metadata

<table>
  <tbody>
    <tr>
      <th scope="row">ID</th>
      <td><code>{{ doc.id }}</code></td>
    </tr>
    <tr>
      <th scope="row">Status</th>
      <td>{{ doc.status }}</td>
    </tr>
    <tr>
      <th scope="row">Release date</th>
      <td>{{ doc.release_date }}</td>
    </tr>
    <tr>
      <th scope="row">Short route</th>
      <td><code>{{ doc.short_route }}</code></td>
    </tr>
    <tr>
      <th scope="row">Mnemonic route</th>
      <td><code>{{ doc.mnemonic_route }}</code></td>
    </tr>
    <tr>
      <th scope="row">Canonical route</th>
      <td><a href="{{ doc.canonical_route | relative_url }}">{{ doc.canonical_route }}</a></td>
    </tr>
    <tr>
      <th scope="row">PDF</th>
      <td><a href="{{ doc.pdf_path | relative_url }}">{{ doc.pdf_path }}</a></td>
    </tr>
    <tr>
      <th scope="row">Pages</th>
      <td>{{ doc.page_count }}</td>
    </tr>
    <tr>
      <th scope="row">Size</th>
      <td>{{ doc.file_size }}</td>
    </tr>
    <tr>
      <th scope="row">SHA-256</th>
      <td><code>{{ doc.checksum_sha256 }}</code></td>
    </tr>
    <tr>
      <th scope="row">License</th>
      <td>{{ doc.license }}</td>
    </tr>
  </tbody>
</table>

## Current Release Snapshot

The May 2026 release snapshot summarized in the Technical Overview is pinned
by the TauLib Release Manifest:

<table>
  <tbody>
    <tr>
      <th scope="row">Lean toolchain</th>
      <td><code>v4.28.0-rc1</code></td>
    </tr>
    <tr>
      <th scope="row">Mathlib snapshot</th>
      <td><code>85028a6</code></td>
    </tr>
    <tr>
      <th scope="row">TauLib snapshot</th>
      <td><code>cb5e830</code></td>
    </tr>
    <tr>
      <th scope="row">Modules/files</th>
      <td>512</td>
    </tr>
    <tr>
      <th scope="row">Lean source lines</th>
      <td>142,406</td>
    </tr>
    <tr>
      <th scope="row">Theorem/lemma records</th>
      <td>4,863</td>
    </tr>
    <tr>
      <th scope="row">Declarations and eval records</th>
      <td>14,601</td>
    </tr>
    <tr>
      <th scope="row">Custom axioms</th>
      <td>3</td>
    </tr>
    <tr>
      <th scope="row">Sorry count</th>
      <td>0</td>
    </tr>
  </tbody>
</table>

## Claim Boundary

The Technical Overview documents the represented formalization release and
its inspection routes. It does not claim empirical validation, semantic
adequacy, complete formal coverage of the research program, peer-review
completion, external acceptance, deployment readiness, product availability,
policy adoption, or achieved impact.

Hashes attest to the PDF bytes only; they do not certify correctness, peer
review, empirical adequacy, legal status, DOI registration, or content
validity.

## Inspection Routes

- Formalization overview: [TauLib](/corpus/taulib/)
- Audit surface: [Verify/TauLib](/verify/taulib/)
- Pinned release facts: [Release Manifest](/verify/release-manifest/)
- Trust-budget disclosure: [Custom Axioms](/verify/custom-axioms/) and [TCB](/verify/tcb/)
- Source repository: [Panta-Rhei-Research/taulib](https://github.com/Panta-Rhei-Research/taulib)
- Generated documentation: [taulib.panta-rhei.site](https://taulib.panta-rhei.site/)

## Citation

Fuchs, Thorsten and Anna-Sophie Fuchs. "TauLib Technical Overview." White Paper
wp003, Panta Rhei Research Program, canonical v1.0 release, May 2026.
