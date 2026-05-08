---
layout: "program-doc"
lane: "publications"
v2_lane: "publications"
status: "Canonical"
last_updated: 2026-05-08
updated: "May 2026"
title: "Anchor Documents"
permalink: "/publications/anchor-documents/"
type: "Publication Family"
summary_short: "The citable offline canon: one charter essay plus five canonical white papers routing back into the live observatory."
right_rail:
  related:
    -
      title: "C001 Charter Essay"
      url: "/publications/anchor-documents/c001-standing-in-the-inquiry-of-being/"
    -
      title: "Program Charter"
      url: "/program/about/standing-in-the-inquiry-of-being/"
    -
      title: "Latest Publications"
      url: "/publications/latest/"
    -
      title: "Publications"
      url: "/publications/"
    -
      title: "Verify"
      url: "/verify/"
  meta:
    type: "Publication Family"
    status: "Canonical"
    updated: "May 2026"
---

{% assign anchor_docs = site.data.publications.anchor_documents.documents %}

## Start Here

Anchor Documents are the downloadable offline routes into the Panta Rhei
Research Program. The website remains the live canonical superset; the PDFs are
citable release artifacts that route back into Program, Corpus, TauLib,
Publications, Impact, and Verify surfaces.

<div class="notice note">
  <strong>Claim boundary.</strong>
  {{ site.data.publications.anchor_documents.claim_boundary }}
</div>

<ul class="v2-grid v2-card-list">
  {% for doc in anchor_docs %}
  <li>
    <article>
      <a class="v2-tile" href="{{ doc.landing_path | relative_url }}">
        <p class="eyebrow">{{ doc.id | upcase }} · {{ doc.artifact_type }}</p>
        <h3>{{ doc.title }}</h3>
        <p>{{ doc.summary }}</p>
        <p><strong>Status:</strong> {{ doc.status }}</p>
      </a>
    </article>
  </li>
  {% endfor %}
</ul>

## Reading Routes

Use C001 first if you need the program's inquiry stance. Use WP001 as the
whole-program orientation once released. Use WP004 for the inspection
architecture, WP003 for the formalization surface, WP005 for conditional impact,
and WP002 last for the theory construction synopsis.

<table>
  <caption>Anchor Document Canon</caption>
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">Document</th>
      <th scope="col">Status</th>
      <th scope="col">Short route</th>
      <th scope="col">PDF</th>
    </tr>
  </thead>
  <tbody>
    {% for doc in anchor_docs %}
    <tr>
      <th scope="row">{{ doc.id | upcase }}</th>
      <td><a href="{{ doc.landing_path | relative_url }}">{{ doc.title }}</a></td>
      <td>{{ doc.status }}</td>
      <td><code>{{ doc.short_route | remove: 'https://' }}</code></td>
      <td>{% if doc.pdf_path %}<a href="{{ doc.pdf_path | relative_url }}">Download</a>{% else %}Planned{% endif %}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## Download, Cite, Inspect

Released Anchor Documents expose three surfaces: the canonical website route,
the downloadable PDF, and the public artifact manifest with hashes. Checksums
attest to bytes only; they do not certify correctness, peer review, legal
status, DOI registration, or content validity.
