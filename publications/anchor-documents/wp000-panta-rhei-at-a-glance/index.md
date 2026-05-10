---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-10
updated: "May 2026"
title: "WP000 — Panta Rhei at a Glance"
title_plain: "Panta Rhei at a Glance"
subtitle: "A nontechnical orientation to an inspectable open research program"
permalink: "/publications/anchor-documents/wp000-panta-rhei-at-a-glance/"
type: "White Paper"
summary_short: "Canonical v1.0 four-page first-contact primer for the Panta Rhei Research Program."
right_rail:
  related:
    -
      title: "Download PDF"
      url: "/assets/pdfs/anchor-documents/wp000-panta-rhei-at-a-glance.pdf"
    -
      title: "Anchor Documents"
      url: "/publications/anchor-documents/"
    -
      title: "Discover"
      url: "/discover/"
    -
      title: "Program"
      url: "/program/"
    -
      title: "C001 Charter Essay"
      url: "/publications/anchor-documents/c001-standing-in-the-inquiry-of-being/"
    -
      title: "WP001 Executive Overview"
      url: "/publications/anchor-documents/wp001-panta-rhei-research-program-executive-overview/"
    -
      title: "Verify"
      url: "/verify/"
  meta:
    type: "White Paper"
    status: "Canonical v1.0"
    updated: "May 2026"
---

{% assign doc = site.data.publications.anchor_documents.documents | where: "id", "wp000" | first %}

## Canonical Artifact

*Panta Rhei at a Glance* is the four-page first-contact primer for the Anchor
Document Canon. It gives nontechnical readers the shortest stable orientation
to the program: what it is, how to read it, why it is structured as a public
research observatory, and where to continue.

The at-a-glance primer should be read before the longer anchor documents if
the reader needs a compact entry point. It points onward to *Standing in the
Inquiry of Being* (C001) for the program's inquiry stance, the *Executive
Overview* (WP001) for the whole-program overview, the *τ-Theory Executive
Synopsis* (WP002) for the theory synopsis, the *TauLib Technical Overview*
(WP003) for TauLib, the *Public Research Observatory Blueprint* (WP004) for
the observatory blueprint, and the *Global Public Good Impact Overview*
(WP005) for conditional impact.

<div class="btn-group section-ctas">
  <a class="btn" href="{{ doc.pdf_path | relative_url }}">Download PDF</a>
  <a class="btn" href="/discover/">Start Discover</a>
  <a class="btn" href="/publications/anchor-documents/">Browse Anchor Documents</a>
  <a class="btn" href="https://github.com/Panta-Rhei-Research/publications/tree/main/anchor-documents/wp000-panta-rhei-at-a-glance">Inspect Artifact Record</a>
</div>

## Release Metadata

<table>
  <tbody>
    <tr>
      <th scope="row">ID</th>
      <td><code>{{ doc.id }}</code></td>
    </tr>
    <tr>
      <th scope="row">Role</th>
      <td>{{ doc.role }}</td>
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

## Four-Page Scope

The primer is deliberately short. It is for first-time readers, journalists,
reviewers, and public communicators who need to know how to enter the site
without mistaking an orientation document for a proof, a peer-review record, or
a final theory claim.

The primer covers:

- the program's public category as an inspectable open research program;
- the route grammar from Discover and Program into Agenda, Corpus, Results,
  Verify, Publications, Impact, and Engage;
- the role of the Anchor Document Canon as citable offline entry points;
- the claim boundary that separates orientation, construction, formalization,
  verification routes, and external acceptance.

## Claim Boundary

*Panta Rhei at a Glance* is an orientation primer. It is not a primary research
result, not a proof of T Theory, not a substitute for the charter essay or the
*Executive Overview*, not a peer-review certificate, and not a claim of
empirical validation, external acceptance, deployment readiness, policy
adoption, product availability, or achieved impact.

Hashes attest to the PDF bytes only; they do not certify correctness, peer
review, empirical adequacy, legal status, DOI registration, or content
validity.

## Citation

Fuchs, Thorsten and Anna-Sophie Fuchs. "Panta Rhei at a Glance." White Paper
wp000, Panta Rhei Research Program, canonical v1.0 release, May 2026.
