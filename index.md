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
    AUD-10 · The section was structurally vestigial in v4 (a duplicate
    4-CTA stack — removed in Wave 2 as AUD-09). Founders' decision in
    Wave 3: Option A — fill with a real glance. The snapshot below
    carries five manifest-driven cells (release ID, last manifest
    update, manifest hash, Lean toolchain, sorry budget). Single
    source of truth is _data/release/current.yml.
  {%- endcomment -%}
  {% include manifest-snapshot.html %}
</section>

<section class="content-card homepage-section homepage-faq-strip">
  {%- comment -%}
    HF-04 · First-Contact FAQ collapse — questions only.
    Replaces the v4 inline accordion (which dumped ~2,000 words of FAQ
    body onto the homepage) with a 5-question list. Each row links into
    the canonical /faq/first-contact/ page at the entry's stable anchor.
    Provenance blocks (Read next / Where this answer comes from) stay
    on the FAQ canonicals; the homepage carries questions only.
  {%- endcomment -%}
  {% include first-contact-questions.html %}
</section>

<section class="content-card homepage-section">
  {%- comment -%}
    HF-05 · Numbered lane index (00 – 07). Replaces the v4 2×4 generic
    v2-grid with a numbered typographic index — reads as a monograph
    table of contents. Source of truth for lane sequence + roles is
    _data/lanes.yml. Lane numerals are typographic, not visual lane-
    color codes (doctrine: "The observatory is not lane-color-coded").
  {%- endcomment -%}
  {% include lane-index.html %}
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
  {%- comment -%}
    HF-06 · World readout — τ-spectrum + layer-tinted cards. The page's
    single most distinctive moment. A continuous τ-spectrum rule above
    four cards, each tinted with --layer-wash and bordered with
    --layer-accent (both driven by the .lane-eN utility class from W1).

    Doctrine: "τ-totality spectral rule reserved for whole-system /
    corpus-totality moments. World-readout layers carry ontological /
    stratum semantics with five steps each (dark / anchor / accent /
    pale / wash)."

    Visible E3 label is "Reflection" per the audit; URL stays at
    /results/world-readout/metaphysics/ for backwards-compatibility.
  {%- endcomment -%}
  {% include world-readout.html %}
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
