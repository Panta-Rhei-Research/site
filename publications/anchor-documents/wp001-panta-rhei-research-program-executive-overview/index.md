---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-10
updated: "May 2026"
title: "WP001 — Panta Rhei Research Program Executive Overview"
title_plain: "Panta Rhei Research Program Executive Overview"
subtitle: "A public research observatory for a coherent theory of reality"
permalink: "/publications/anchor-documents/wp001-panta-rhei-research-program-executive-overview/"
type: "White Paper"
summary_short: "Canonical v1.0 whole-program overview white paper: the program is structured enough to inspect."
right_rail:
  related:
    -
      title: "Download PDF"
      url: "/assets/pdfs/anchor-documents/wp001-panta-rhei-research-program-executive-overview.pdf"
    -
      title: "Anchor Documents"
      url: "/publications/anchor-documents/"
    -
      title: "Program"
      url: "/program/"
    -
      title: "Verify"
      url: "/verify/"
    -
      title: "Engage"
      url: "/engage/"
  meta:
    type: "White Paper"
    status: "Canonical v1.0"
    updated: "May 2026"
---

{% assign doc = site.data.publications.anchor_documents.documents | where: "id", "wp001" | first %}

## Canonical Artifact

*Panta Rhei Research Program Executive Overview* is the first canonical white
paper in the Anchor Document Canon. Its core thesis is that the program is
structured enough to inspect: the public site separates Program, Agenda,
Corpus, Results, Verify, Publications, Impact, and Engage so readers can follow
claims without being asked for premature belief.

<div class="btn-group section-ctas">
  <a class="btn" href="{{ doc.pdf_path | relative_url }}">Download PDF</a>
  <a class="btn" href="/program/">Read Program Lane</a>
  <a class="btn" href="https://github.com/Panta-Rhei-Research/publications/tree/main/anchor-documents/wp001-panta-rhei-research-program-executive-overview">Inspect Artifact Record</a>
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

## Claim Boundary

WP001 is an executive overview and offline guide into the public observatory.
It is not a primary research result, not a proof of T Theory, not a substitute
for expert review, and not a claim of external acceptance for any mathematical,
physical, biological, or metaphysical claim.

Hashes attest to the PDF bytes only; they do not certify correctness, peer
review, empirical adequacy, legal status, DOI registration, or content
validity.

## Citation

Fuchs, Thorsten and Anna-Sophie Fuchs. "Panta Rhei Research Program Executive
Overview." White Paper wp001, Panta Rhei Research Program, canonical v1.0
release, May 2026.
