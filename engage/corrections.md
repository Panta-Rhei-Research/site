---
layout: program-doc
title: "Corrections"
lane: engage
v2_lane: engage
permalink: /engage/corrections/
type: "Engagement Route"
status: "Canonical"
summary_short: "How to submit corrections, prior-art references, claim-boundary concerns, formalization concerns, publication errata, and private review feedback."
summary_cards:
  - title: "Concrete is best"
    body: "Name the page, result, registry object, theorem, module, publication, or route under review."
  - title: "Meaning is traceable"
    body: "Substantive corrections are handled through controlled corpus updates and public changelog entries."
  - title: "Privacy respected"
    body: "Private or sensitive feedback can be summarized publicly without exposing private correspondence."
right_rail:
  related:
    - title: "Corpus Changelog"
      url: /corpus/changelog/
    - title: "Public Discussions"
      url: /engage/discussions/
    - title: "Critique & Challenge"
      url: /engage/critique-challenge/
    - title: "Contact"
      url: /engage/contact/
    - title: "Publication Errata"
      url: /publications/errata/
  artifacts:
    - title: "GitHub Discussions"
      url: https://github.com/orgs/Panta-Rhei-Research/discussions
    - title: "Site Issues"
      url: https://github.com/Panta-Rhei-Research/site/issues
    - title: "TauLib Issues"
      url: https://github.com/Panta-Rhei-Research/taulib/issues
    - title: "Publications Issues"
      url: https://github.com/Panta-Rhei-Research/publications/issues
  meta:
    type: "Engagement Route"
    status: "Canonical"
    updated: "May 2026"
tags:
  - engage
  - corrections
  - corpus-changelog
  - feedback
  - scrutiny
  - errata
---

## Correction posture

Corrections and review are part of the research process. Meaningful changes to
the corpus are logged publicly rather than silently absorbed.

Panta Rhei invites corrections, prior-art references, technical objections,
formalization concerns, and domain-specific review. Public feedback is triaged,
evaluated, and, where accepted, implemented through controlled corpus updates.
Substantive changes are recorded in the [Corpus Changelog]({{ '/corpus/changelog/' | relative_url }}).

## Where To Send What

<table>
  <thead>
    <tr>
      <th scope="col">Concern</th>
      <th scope="col">Best route</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Public question, critique, or prior-art suggestion</td><td><a href="https://github.com/orgs/Panta-Rhei-Research/discussions">GitHub Discussions</a></td></tr>
    <tr><td>Broken link, route, metadata, or reproducible site defect</td><td><a href="https://github.com/Panta-Rhei-Research/site/issues">Site Issues</a></td></tr>
    <tr><td>Formalization concern or Lean-source mismatch</td><td><a href="https://github.com/Panta-Rhei-Research/taulib/issues">TauLib Issues</a></td></tr>
    <tr><td>PDF, checksum, timestamp, DOI, or artifact metadata concern</td><td><a href="https://github.com/Panta-Rhei-Research/publications/issues">Publications Issues</a></td></tr>
    <tr><td>Concrete wording, metadata, documentation, or code fix</td><td>Pull Request to the relevant public repository</td></tr>
    <tr><td>Private review, sensitive concern, institutional context, or media correction</td><td><a href="{{ '/engage/contact/' | relative_url }}">Email via Contact</a></td></tr>
  </tbody>
</table>

## What To Include

- the exact public URL, registry ID, result ID, theorem, TauLib module, PDF, or publication route;
- the correction or concern;
- why it affects meaning, correctness, scope, priority, or interpretation;
- references, reproduction steps, counterexamples, or suggested wording where available;
- whether you are comfortable being named publicly if the correction is logged.

## What Happens Next

Substantive feedback is triaged by domain, severity, affected surfaces, privacy
constraints, and propagation needs. If accepted, the semantic correction is made
in Corpus or the appropriate source repository, propagated outward, verified,
and recorded in the Corpus Changelog when it affects public meaning.

GitHub Issues and Discussions are useful working surfaces. The curated public
history of meaningful semantic changes is the [Corpus Changelog]({{ '/corpus/changelog/' | relative_url }}).

## Publication Errata

If a correction affects a released publication or monograph, the publication
record may also receive an erratum. Publication-specific errata remain under
[Publication Errata]({{ '/publications/errata/' | relative_url }}) and should
link back to the Corpus Changelog when the correction affects the semantic
corpus.
