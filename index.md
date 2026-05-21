---
layout: homepage
shell: home
title: "Panta Rhei Research Program"
lane: discover
v2_lane: discover
type: "Homepage"
status: "Canonical"
summary_short: "An open research program for a coherent theory of reality."
# HF-01 · Frontispiece hero (v5 audit AUD-2026-05-19).
# The H1 is now a thesis sentence, not the program name. The program name
# demotes to a mono ident line above H1. Two CTAs only (AUD-07). Other
# lane CTAs migrate to the numbered lane index (Wave 3 · HF-05).
hero_ident: "Panta Rhei Research Program · v4 release"
hero_thesis: "A coherent theory of reality, built in public — inspectable before it is believed."
hero_line: ""
hero_body: "An independent open research program, published as an inspectable public observatory. The work spans foundational mathematics, physics, the categorical structure of life processes, and the philosophy of mind — developed as one unified construction. Read carefully. Challenge weak links."
hero_ctas:
  - label: "Verify it yourself"
    url: /verify/
    primary: true
  - label: "Start with Discover"
    url: /discover/
# AUD-11 · The posture-seal include replaces hero_supporting_line as the
# canonical home for "Engagement without endorsement." Lands beneath the
# hero τ-seal, gold-hairlined, once per page only.
posture_seal: true
posture_seal_kicker: "Audit posture"
posture_seal_body: "Engagement without endorsement.<br/>Read carefully, challenge weak links, find errors."
og_image: /assets/images/plates/plate-20-panta-rhei-at-a-glance-og.jpg
twitter_image: /assets/images/plates/plate-20-panta-rhei-at-a-glance-og.jpg
og_image_alt: "Scientific plate mapping the Panta Rhei Research Program at a glance as an inspectable research engine with Discover, Program, Corpus, Results, Verify, Publications, Impact, and Engage."
---

<section class="content-card homepage-section">
  <p class="v2-kicker">What the formal layer currently exposes</p>
  <h2>The formalization is real, public, and auditable</h2>
  {%- comment -%}
    HF-03 · TauLib data marquee. Counts come from _data/release/current.yml
    (taulib.modules, taulib.theorems_lemmas, taulib.sorry, taulib.custom_axioms).
    Replaces the v4 prose paragraph that hand-listed the same four numbers —
    the marquee is now the single source of truth for those counts on the
    homepage (AUD-16 deletes the inline repeat from §6 below).
  {%- endcomment -%}
  {% include taulib-data-marquee.html %}
  <p class="marquee-frame">Formal checking is not empirical truth. The bridge to observation, measurement, and domain testing remains the empirical-accountability question — and is treated as such across the site. But the formal layer itself is real, public, and auditable today.</p>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/verify/' | relative_url }}">Verify it yourself</a>
    <a class="btn-ghost" href="{{ '/corpus/taulib/' | relative_url }}">Browse TauLib</a>
    <a class="btn-ghost" href="{{ '/verify/release-manifest/' | relative_url }}">Read the Release Manifest</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">The research observatory at a glance</p>
  <h2>Panta Rhei at a glance</h2>
  {% include scientific-plate.html id="plate-20-panta-rhei-at-a-glance" class="scientific-plate--hero scientific-plate--at-a-glance" loading="eager" %}
  {%- comment -%}
    AUD-09 · The four CTAs that lived here were a duplicate of the hero
    stack within 1500 px of the same page. Hero now carries the two
    canonical CTAs (Verify · Discover); the other lane entries migrate to
    the numbered lane index in §4 below ("Choose your entry"). The plate
    + caption are the at-a-glance signal — no second CTA stack required.
    AUD-10 decision (fill this section with a manifest snapshot) lands in
    Wave 3.
  {%- endcomment -%}
</section>

<section class="content-card homepage-section homepage-faq-strip">
  <p class="v2-kicker">First-contact questions</p>
  <h2>What is this, and what is it claiming?</h2>
  <p class="muted-note">A first-contact credibility filter before you choose where to read. Each card links to its full answer with related routes and source pages — see the <a href="{{ '/faq/first-contact/' | relative_url }}">First Contact FAQ</a> for the complete layer.</p>
  {% include faqs/faq-list.html ids="FAQ-FC-001,FAQ-FC-002,FAQ-FC-003,FAQ-FC-004,FAQ-FC-005" style="accordion" %}
  <p class="muted-note" style="margin-top: 12px;"><a href="{{ '/faq/' | relative_url }}">All 73 FAQ entries →</a></p>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Choose your entry</p>
  <h2>Different readers should not have to start in the same place</h2>
  <div class="v2-grid">
    <a class="v2-tile" href="{{ '/discover/' | relative_url }}">
      <h3>Discover</h3>
      <p>A guided first route for readers who want orientation before depth.</p>
    </a>
    <a class="v2-tile" href="{{ '/program/' | relative_url }}">
      <h3>Program</h3>
      <p>Identity, doctrine, scope, status, founders, scrutiny posture, and why the program is built as an inspection observatory.</p>
    </a>
    <a class="v2-tile" href="{{ '/agenda/' | relative_url }}">
      <h3>Agenda</h3>
      <p>Obligations: what must be asked, recovered, built, refused, answered, and left open.</p>
    </a>
    <a class="v2-tile" href="{{ '/corpus/' | relative_url }}">
      <h3>Corpus</h3>
      <p>The construction body of the theory: Construction Spine, Monograph Corpus, Registry, TauLib projection, and dependency graph.</p>
    </a>
    <a class="v2-tile" href="{{ '/results/' | relative_url }}">
      <h3>Results</h3>
      <p>Consequences: Landmark Results, World Readouts, Challenge Responses, Core Semantics Status, and Progress Against Agenda.</p>
    </a>
    <a class="v2-tile" href="{{ '/verify/' | relative_url }}">
      <h3>Verify</h3>
      <p>Inspection routes: formalization, bridge checks, predictions, falsification, audits, and external challenge paths.</p>
    </a>
    <a class="v2-tile" href="{{ '/impact/' | relative_url }}">
      <h3>Impact</h3>
      <p>Conditional relevance: what could matter if relevant Results remain supported through review, translation, and domain uptake.</p>
    </a>
    <a class="v2-tile" href="{{ '/engage/' | relative_url }}">
      <h3>Engage</h3>
      <p>Open scrutiny, public questions, correction routes, review, communication, and contribution without endorsement.</p>
    </a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Flagship results</p>
  <h2>Concrete claims before broad interpretation</h2>
  {%- comment -%}
    HF-02 · Master constant ιτ display block. Display-set the constant
    as a centred, gold-hairlined ceremonial block — the rare ceremonial
    moment gold is sanctioned for. The accompanying paragraph is the
    publishing-route lead-in; the symbolic + numeric forms are now
    carried by the block, not inline prose.
  {%- endcomment -%}
  {% include flagship-constant.html %}
  <p>The quantitative physics surface is organised around this master constant. The current public release treats it as a review target, not a rhetorical shortcut: the constant has a dedicated research paper, a Corpus foundational-hinge page (H3), a scalar-readout route through Construction Spine Step&nbsp;2, Registry anchors, and TauLib evidence. Downstream physics claims remain bridge and empirical-accountability claims, but the master-constant question now has a direct public review path.</p>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/corpus/foundational-hinges/master-constant-iota-tau/' | relative_url }}">Review the Master Constant</a>
    <a class="btn-ghost" href="{{ '/publications/research-papers/master-constant-iota-tau/' | relative_url }}">Read the paper</a>
    <a class="btn-ghost" href="{{ '/results/predictions/timing/' | relative_url }}">See prediction timing</a>
  </div>
  <p>The program presents {% include release-metric.html id="results.records" %} typed result pages, {% include release-metric.html id="predictions.records" %} quantitative predictions, and {% include release-metric.html id="falsifications.records" %} named falsification tests — with <a href="{{ '/results/predictions/timing/' | relative_url }}">full pre-registration accounting</a> distinguishing post-dictions, tension-side commitments, and forward forbiddances. These are not all equivalent in status; the site makes status, verification route, and external-acceptance boundaries visible at the page level.</p>
  <div class="v2-grid">
    <a class="v2-tile" href="{{ '/results/problem/hubble-tension-resolved-h-formula/' | relative_url }}">
      <h3>Hubble tension</h3>
      <p>A zero-continuous-parameter readout for the Hubble constant.</p>
      <div class="v2-badge-row"><span class="v2-badge">Physics</span><span class="v2-badge">Prediction</span></div>
    </a>
    <a class="v2-tile" href="{{ '/results/problem/no-dark-matter-particle/' | relative_url }}">
      <h3>No dark matter particle</h3>
      <p>A structural exhaustion claim rather than a new-particle hypothesis.</p>
      <div class="v2-badge-row"><span class="v2-badge">World Readout</span><span class="v2-badge">Falsifiable</span></div>
    </a>
    <a class="v2-tile" href="{{ '/results/problem/homochirality-universality-12-step-derivation/' | relative_url }}">
      <h3>Homochirality</h3>
      <p>A life-sector derivation path tied back to the formal corpus.</p>
      <div class="v2-badge-row"><span class="v2-badge">Life</span><span class="v2-badge">Corpus-linked</span></div>
    </a>
  </div>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/results/' | relative_url }}">Results Lane</a>
    <a class="btn-ghost" href="{{ '/results/predictions/browse/' | relative_url }}">Browse Predictions</a>
    <a class="btn-ghost" href="{{ '/results/falsifications/browse/' | relative_url }}">Browse Falsification Tests</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">How the system works</p>
  <h2>One research program, several public surfaces</h2>
  <p>Agenda states the burden: Core Semantics, Structural Challenge Ledger, answer-shape discipline, refusals, and Construction Roadmap. Corpus carries the construction: Construction Spine, Monograph Corpus, Registry, TauLib projection, and dependency graph. Results presents current consequence surfaces: Landmark Results, World Readouts, Challenge Responses, Core Semantics Status, and Progress Against Agenda. Verify exposes formal, empirical, bridge, falsification, and assessment routes. Publications preserve the stable artifact and release shelf.</p>
  <div class="v2-system-strip">
    <div class="v2-system-node"><strong>Agenda</strong>Core Semantics, Structural Challenge Ledger, answer-shape discipline, refusals, and Construction Roadmap.</div>
    <div class="v2-system-node"><strong>Kernel</strong>Five generators, one progression operator, and the K0&ndash;K6 structural commitments, with the foundational-hinge route.</div>
    <div class="v2-system-node"><strong>Corpus</strong>Construction Spine, Monograph Corpus, Registry, foundational hinges, TauLib projection, and dependency graph.</div>
    <div class="v2-system-node"><strong>TauLib</strong>Pinned Lean&nbsp;4 formalization with a sharp axiom and sorry budget in Book&nbsp;III bridge territory — <a href="#formal-marquee-title">see the TauLib marquee above</a> for the current release counts.</div>
    <div class="v2-system-node"><strong>Results</strong>Landmark Results, World Readouts, Challenge Responses, Core Semantics Status, and Progress Against Agenda.</div>
    <div class="v2-system-node"><strong>Verify</strong>Release Manifest, inspection routes, prediction timing, falsification pack, and TCB disclosure.</div>
    <div class="v2-system-node"><strong>Publications</strong>research monographs, research papers, supplements, notes, briefings, white papers, release artifacts, and errata.</div>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Public inspectability</p>
  <h2>The site asks to be checked, not simply believed</h2>
  <ul>
    <li><strong>TauLib</strong>: public Lean 4 formalization with a sharp axiom and sorry budget.</li>
    <li><strong>Registry</strong>: object-level IDs, dependencies, and status metadata.</li>
    <li><strong>Predictions</strong>: explicit values, observed comparators, and precision tiers.</li>
    <li><strong>Falsification pack</strong>: named experiments and timelines where the framework can fail.</li>
    <li><strong>Errata</strong>: public corrections with stable IDs and current status.</li>
  </ul>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/verify/' | relative_url }}">Verify</a>
    <a class="btn-ghost" href="{{ '/corpus/registry/' | relative_url }}">Registry</a>
    <a class="btn-ghost" href="{{ '/publications/errata/' | relative_url }}">Errata</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">World readout</p>
  <h2>What the theory currently says follows, domain by domain</h2>
  <div class="v2-grid">
    <a class="v2-tile v2-tile-layer v2-tile-mathematics" href="{{ '/results/world-readout/mathematics/' | relative_url }}"><h3>Mathematics</h3><p>Foundations, holomorphy, spectral structure, and problem surfaces.</p></a>
    <a class="v2-tile v2-tile-layer v2-tile-physics" href="{{ '/results/world-readout/physics/' | relative_url }}"><h3>Physics</h3><p>Microcosm, macrocosm, constants, predictions, and falsification seams.</p></a>
    <a class="v2-tile v2-tile-layer v2-tile-life" href="{{ '/results/world-readout/life/' | relative_url }}"><h3>Life</h3><p>Self-decoding distinctions, biological structure, agency, and persistence.</p></a>
    <a class="v2-tile v2-tile-layer v2-tile-metaphysics" href="{{ '/results/world-readout/metaphysics/' | relative_url }}"><h3>Metaphysics</h3><p>Ontology, ethics, consciousness, and the final enrichment layer.</p></a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Artifacts and continuation</p>
  <h2>Artifacts & Releases</h2>
  <p>The public release surface is not only the research monographs. It includes Anchor Documents, Research Monographs, Monograph Supplements, Research Papers, Research Notes, Research Briefings, TauLib, assessment protocols, Release Artifacts, and errata. The site makes those surfaces easier to find without turning the homepage into a catalogue.</p>
  <div class="btn-group section-ctas">
    <a class="btn-secondary" href="{{ '/publications/' | relative_url }}">Publications</a>
    <a class="btn-secondary" href="{{ '/publications/anchor-documents/' | relative_url }}">Anchor Documents</a>
    <a class="btn-secondary" href="{{ '/publications/research-monographs/' | relative_url }}">Research Monographs</a>
    <a class="btn-ghost" href="{{ '/publications/research-papers/' | relative_url }}">Research Papers</a>
    <a class="btn-ghost" href="{{ '/publications/research-notes/' | relative_url }}">Research Notes</a>
    <a class="btn-ghost" href="{{ '/publications/release-artifacts/' | relative_url }}">Release Artifacts</a>
    <a class="btn-ghost" href="{{ '/publications/errata/' | relative_url }}">Errata</a>
    <a class="btn-ghost" href="{{ '/cite/' | relative_url }}">Cite</a>
  </div>
</section>

<section class="content-card homepage-section">
  <p class="v2-kicker">Stay in inspection range</p>
  {% include buttondown-subscribe.html tag="homepage" heading="Receive publication notifications" body="Get new Panta Rhei publication releases by email when dated artifacts are added — research notes, monograph supplements, white papers, and release manifests. Notifications are sent irregularly and only when there is something substantial to record." %}
</section>
