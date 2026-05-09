---
layout: program-doc
title: "Sitemap"
lane: support
shell: home
type: support_page
support_type: sitemap
status: canonical
last_updated: 2026-05-31
updated: "May 2026"
permalink: /sitemap/
summary: "Human-readable map of the Panta Rhei public research observatory."
summary_short: "Human-readable map of the Panta Rhei public research observatory."
right_rail:
  related:
  - title: Discover
    url: /discover/
  - title: Agenda
    url: /agenda/
  - title: XML Sitemap
    url: /sitemap.xml
  meta:
    type: "Support page"
    scope: "Sitemap"
    status: "Canonical"
    updated: "May 2026"
---

{% assign sitemap_data = site.data.sitemap_v4 %}
{% assign total_links = sitemap_data.support.links | size %}
{% for lane in sitemap_data.primary_lanes %}{% assign total_links = total_links | plus: lane.links.size %}{% endfor %}

<section class="sitemap-intro" aria-labelledby="sitemap-directory-heading">
  <h2 id="sitemap-directory-heading">Observatory directory</h2>
  <p>{{ sitemap_data.intro }}</p>
  <p class="sitemap-totals" aria-label="Sitemap totals">
    <span class="sitemap-totals-chip"><strong>{{ sitemap_data.primary_lanes | size }}</strong> primary lanes</span>
    <span class="sitemap-totals-chip"><strong>{{ total_links }}</strong> canonical pages</span>
  </p>
</section>

<div class="sitemap-search" role="search" aria-labelledby="sitemap-search-label">
  <label id="sitemap-search-label" class="sitemap-search-label" for="sitemap-search-input">Filter the directory</label>
  <div class="sitemap-search-row">
    <input
      type="search"
      id="sitemap-search-input"
      class="sitemap-search-input"
      placeholder="Search {{ total_links }} pages — try &quot;tau&quot;, &quot;dark matter&quot;, &quot;verify&quot;…"
      autocomplete="off"
      spellcheck="false"
      aria-controls="sitemap-results-region"
      aria-describedby="sitemap-search-hint"
    >
    <button type="button" class="sitemap-search-clear" id="sitemap-search-clear" aria-label="Clear search" hidden>×</button>
  </div>
  <p id="sitemap-search-hint" class="sitemap-search-hint">
    Press <kbd>/</kbd> to focus search, <kbd>Esc</kbd> to clear. Filter is shareable via <code>?q=…</code>.
  </p>
  <p id="sitemap-search-status" class="sitemap-search-status" aria-live="polite" data-default-text="Showing all {{ total_links }} pages."></p>
</div>

<nav class="sitemap-jump" aria-label="Jump to lane">
  {% for lane in sitemap_data.primary_lanes %}
  <a class="sitemap-jump-pill" href="#lane-{{ lane.title | slugify }}" data-jump-target="lane-{{ lane.title | slugify }}">{{ lane.title }}</a>
  {% endfor %}
  <a class="sitemap-jump-pill sitemap-jump-pill-support" href="#lane-support" data-jump-target="lane-support">Support</a>
</nav>

<div id="sitemap-results-region">

<section class="sitemap-section" aria-labelledby="sitemap-primary-lanes-heading">
  <h2 id="sitemap-primary-lanes-heading">Primary lanes</h2>
  <div class="sitemap-grid sitemap-grid-primary">
    {% for lane in sitemap_data.primary_lanes %}
    <article class="sitemap-card sitemap-card-primary" id="lane-{{ lane.title | slugify }}" data-sitemap-lane="{{ lane.title | slugify }}" data-sitemap-lane-count="{{ lane.links | size }}">
      <div class="sitemap-card-header">
        <p class="sitemap-card-role">{{ lane.role }}</p>
        <h3>{{ lane.title }}</h3>
        <p class="sitemap-card-count" aria-label="{{ lane.title }} entry count"><span>{{ lane.links | size }}</span> entries</p>
        <p>{{ lane.description }}</p>
      </div>
      <ul class="sitemap-link-grid" aria-label="{{ lane.title }} pages">
        {% for link in lane.links %}
        <li class="sitemap-mini-card" data-sitemap-link-title="{{ link.title | downcase }}"><a href="{{ link.url | relative_url }}"><span>{{ link.title }}</span></a></li>
        {% endfor %}
      </ul>
      <a class="sitemap-card-cta" href="{{ lane.root_url | relative_url }}">{{ lane.root_label }}</a>
    </article>
    {% endfor %}
  </div>
</section>

<section class="sitemap-section" aria-labelledby="sitemap-support-heading">
  <h2 id="sitemap-support-heading">Artifacts, media, and infrastructure</h2>
  {% assign support = sitemap_data.support %}
  <article class="sitemap-card sitemap-card-support" id="lane-support" data-sitemap-lane="support" data-sitemap-lane-count="{{ support.links | size }}">
    <div class="sitemap-card-header">
      <p class="sitemap-card-role">{{ support.role }}</p>
      <h3>{{ support.title }}</h3>
      <p class="sitemap-card-count" aria-label="Support entry count"><span>{{ support.links | size }}</span> entries</p>
      <p>{{ support.description }}</p>
    </div>
    <ul class="sitemap-link-grid" aria-label="{{ support.title }} pages">
      {% for link in support.links %}
      <li class="sitemap-mini-card" data-sitemap-link-title="{{ link.title | downcase }}"><a href="{{ link.url | relative_url }}"><span>{{ link.title }}</span></a></li>
      {% endfor %}
    </ul>
    <a class="sitemap-card-cta" href="{{ support.root_url | relative_url }}">{{ support.root_label }}</a>
  </article>
</section>

<p class="sitemap-empty" id="sitemap-empty" hidden>
  No pages match your search. Try <button type="button" class="sitemap-empty-suggestion" data-search-suggestion="results">results</button>, <button type="button" class="sitemap-empty-suggestion" data-search-suggestion="verify">verify</button>, or <button type="button" class="sitemap-empty-suggestion" data-search-suggestion="challenge">challenge</button>.
</p>

</div>

<section class="sitemap-machine" aria-labelledby="sitemap-machine-heading">
  <h2 id="sitemap-machine-heading">Machine-readable sitemap</h2>
  <p>The machine-readable sitemap remains available at <a href="{{ '/sitemap.xml' | relative_url }}">sitemap.xml</a>.</p>
</section>
