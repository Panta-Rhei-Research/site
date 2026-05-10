---
layout: program-doc
title: "Prior-Art Clusters"
permalink: /bibliography/prior-art/
lane: corpus
type: "Prior-Art Cluster Index"
status: "Canonical"
summary: "9 domain clusters of prior-art references that the Panta Rhei Research Program engages, each curated from the central bibliography (1,148 entries) and wired to the program's construction-spine steps and structural-challenge-ledger items."
summary_short: "9 prior-art clusters · 117 representative references · 60 structural-challenge edges. Source: corpus/data/bibliography/prior-art-clusters.yml."
right_rail:
  related:
  - title: "Bibliography (browse)"
    url: /bibliography/browse/
  - title: "Deep Comparison Briefing"
    url: /agenda/kernel-model-reality/related-approaches/deep-comparison/
  - title: "Structural Challenge Ledger"
    url: /agenda/structural-challenge-ledger/
  - title: "Challenge Responses"
    url: /results/challenge-responses/
  meta:
    type: "Prior-Art Cluster Index"
    scope: "All 9 clusters"
    status: "Canonical"
    updated: "May 2026"
---

{% assign clusters_root = site.data.bibliography['prior-art-clusters'] %}
{% assign total_refs = 0 %}
{% assign total_challenges = 0 %}
{% if clusters_root and clusters_root.clusters %}
  {% for c in clusters_root.clusters %}
    {% assign total_refs = total_refs | plus: c.references.size %}
    {% assign total_challenges = total_challenges | plus: c.related_challenges.size %}
  {% endfor %}
{% endif %}

<section class="content-card">
  <p>Prior-art clusters group bibliography references that share a domain pressure the Panta Rhei Research Program engages. Each cluster is curated from the central bibliography ({% include release-metric.html id="bibliography.references" %} entries) and wired to:</p>
  <ul>
    <li>the program's <a href="{{ '/corpus/construction-spine/' | relative_url }}">construction-spine steps</a>,</li>
    <li>the canonical <a href="{{ '/agenda/structural-challenge-ledger/' | relative_url }}">Structural Challenge Ledger</a> items the cluster bears on,</li>
    <li>the corresponding <a href="{{ '/results/challenge-responses/' | relative_url }}">Challenge Responses</a> on the Results lane.</li>
  </ul>
  <p class="muted-note">This index is the <strong>structured-data backbone</strong>; for narrative comparisons against specific approach families (shared pressure, distinguishing claim, remaining burden), see the <a href="{{ '/agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }}">Deep Comparison briefing</a>.</p>
  <p class="prior-art-totals" aria-label="Prior-art totals">
    <span class="prior-art-totals-chip"><strong>{{ clusters_root.clusters.size }}</strong> clusters</span>
    <span class="prior-art-totals-chip"><strong>{{ total_refs }}</strong> representative references</span>
    <span class="prior-art-totals-chip"><strong>{{ total_challenges }}</strong> structural-challenge edges</span>
  </p>
</section>

<section class="content-card">
  <h2>The 9 clusters</h2>
  <ul class="prior-art-cluster-grid" role="list">
    {% for c in clusters_root.clusters %}
    <li class="prior-art-cluster-card">
      <a href="{{ '/bibliography/prior-art/' | append: c.cluster_key | append: '/' | relative_url }}">
        <p class="prior-art-cluster-eyebrow"><code>{{ c.cluster_id }}</code> · {{ c.reference_count }} domain entries</p>
        <h3>{{ c.title }}</h3>
        <p class="prior-art-cluster-counts">
          <span><strong>{{ c.references.size }}</strong> representative references</span>
          <span><strong>{{ c.related_challenges.size }}</strong> SCL challenge edges</span>
          <span><strong>{{ c.related_construction_steps.size }}</strong> construction-spine steps</span>
        </p>
        <span class="prior-art-cluster-cta">Open cluster →</span>
      </a>
    </li>
    {% endfor %}
  </ul>
</section>

## Source-of-truth discipline

> The Corpus owns the prior-art clusters. The website renders prior-art projections.

Cluster data is mirrored from [`corpus/data/bibliography/prior-art-clusters.yml`](https://github.com/Panta-Rhei-Research/corpus/blob/main/data/bibliography/prior-art-clusters.yml) via `scripts/sync_prior_art_clusters_from_corpus.py`. Edits land in the corpus repo first, then sync into this site. Each cluster has a stable ID (`pa<NNNNNN>`) for citation continuity.

## Read next

- [Bibliography browse]({{ '/bibliography/browse/' | relative_url }}) — full filterable catalogue of {% include release-metric.html id="bibliography.references" %} entries
- [Deep Comparison briefing]({{ '/agenda/kernel-model-reality/related-approaches/deep-comparison/' | relative_url }}) — narrative comparisons against 12 approach families
- [Structural Challenge Ledger]({{ '/agenda/structural-challenge-ledger/' | relative_url }}) — the obligation side
- [Challenge Responses]({{ '/results/challenge-responses/' | relative_url }}) — the Results-side projection
