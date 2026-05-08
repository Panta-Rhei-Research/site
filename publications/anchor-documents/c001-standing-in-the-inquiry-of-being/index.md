---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-08
updated: "May 2026"
title: "C001 — Standing in the Inquiry of Being"
title_plain: "Standing in the Inquiry of Being"
subtitle: "Lineages of Categorical Ontology"
permalink: "/publications/anchor-documents/c001-standing-in-the-inquiry-of-being/"
type: "Charter Essay"
summary_short: "The canonical v1.0 Charter Essay PDF and artifact record for Standing in the Inquiry of Being."
right_rail:
  related:
    -
      title: "Download PDF"
      url: "/assets/pdfs/anchor-documents/c001-standing-in-the-inquiry-of-being.pdf"
    -
      title: "Canonical Program Page"
      url: "/program/about/standing-in-the-inquiry-of-being/"
    -
      title: "Anchor Documents"
      url: "/publications/anchor-documents/"
    -
      title: "Publications"
      url: "/publications/"
    -
      title: "Program"
      url: "/program/"
  meta:
    type: "Charter Essay"
    status: "Canonical v1.0"
    updated: "May 2026"
---

{% assign doc = site.data.publications.anchor_documents.documents | where: "id", "c001" | first %}

## Canonical Artifact

*Standing in the Inquiry of Being* is the first Anchor Document in the canon and
the program's constitutive Charter Essay. It records the inquiry stance behind
the Program lane by situating categorical ontology in a chosen lineage from
ancient formal intelligibility through modern structural thought.

<div class="btn-group section-ctas">
  <a class="btn" href="{{ doc.pdf_path | relative_url }}">Download PDF</a>
  <a class="btn" href="{{ doc.canonical_route | relative_url }}">Read Canonical Program Page</a>
  <a class="btn" href="https://github.com/Panta-Rhei-Research/publications/tree/main/anchor-documents/c001-standing-in-the-inquiry-of-being">Inspect Artifact Record</a>
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

This Charter Essay is an orientation artifact. It does not prove or validate
`\tau`-Theory, does not claim final-theory status, and does not turn a
historical lineage into evidence of truth.

Hashes and timestamps attest to the PDF bytes only; they do not certify
correctness, peer review, legal status, DOI registration, or content validity.

## Citation

Fuchs, Thorsten and Anna-Sophie Fuchs. "Standing in the Inquiry of Being:
Lineages of Categorical Ontology." Charter Essay c001, Panta Rhei Research
Program, canonical v1.0 release, May 2026.
