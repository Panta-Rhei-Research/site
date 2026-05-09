---
title: "Sitemap L1/L2 sync — 30 new canonical anchors + validation hardening"
date: 2026-05-09
change_type: "site-release"
summary_short: "Added 30 canonical L2/L3 anchors to /sitemap/ (4 SCL domain pages, 11 Public Good subdomains, 4 domain-verification leaves, 5 World Readout pages, 4 TauLib children, 2 most-cited foundational hinges) and extended the sitemap validation script with per-lane coverage floors and a required-key-pages allowlist."
affected_lanes:
  - agenda
  - corpus
  - results
  - verify
  - impact
right_rail:
  toc: false
  related:
    - title: "Sitemap"
      url: /sitemap/
    - title: "Changelog"
      url: /changelog/
    - title: "Discover"
      url: /discover/
  meta:
    type: "Changelog Entry"
    status: "Published"
    updated: "May 2026"
---

## Changes

The `/sitemap/` page is the canonical human-readable directory of the v4 observatory. With the SCL Responses workstream landing 214 Challenge Response pages and several adjacent surfaces (Bi-Square Spine, World Readout clusters, Public Good subdomains) reaching first-class status, the human sitemap needs to surface them all. This wave does the strict L1/L2 sync.

### Added — 30 new canonical anchors

| Lane | Additions |
|---|---|
| **Agenda** (+4) | `SCL — Mathematics`, `SCL — Physics`, `SCL — Life`, `SCL — Metaphysics` (the four canonical-by-domain SCL views) |
| **Corpus** (+6) | `Master Constant ι_τ`, `τ-Kernel Foundational Architecture` (the two most-cited foundational hinges); `TauLib — Modules / Docs / Status / Architecture` (the four canonical TauLib hubs) |
| **Results** (+5) | `World Readout` parent + `World Readout — Mathematics / Physics / Life / Metaphysics` (the four domain readouts) |
| **Verify** (+4) | `Domain Verification — Mathematics / Physics / Life / Metaphysics` (the four domain verification leaves) |
| **Impact** (+11) | All 11 Global Public Good subdomains: Agriculture · Biodiversity Restoration · Climate · Disaster Resilience · Energy · Ocean · One Health · Pollution & Circularity · Solar · Water & WASH · Weather |

### Removed — 1 stale entry

- Removed `/results/fields/` (no parent index page exists; individual field briefings are reached via the World Readout domain pages).

### Per-lane coverage after sync

| Lane | Before | After | Δ |
|---|---|---|---|
| Discover | 11 | 11 | 0 |
| Program | 11 | 11 | 0 |
| Agenda | 14 | 18 | +4 |
| Corpus | 18 | 24 | +6 |
| Results | 29 | 34 | +5 |
| Verify | 23 | 27 | +4 |
| Impact | 9 | 20 | +11 |
| Engage | 14 | 14 | 0 |
| Support | 25 | 25 | 0 |
| **Total** | **154** | **184** | **+30** |

### Validation hardening

`scripts/assert_v4_sitemap.py` now enforces:

- **Per-lane coverage floors** (Discover ≥11, Program ≥11, Agenda ≥18, Corpus ≥24, Results ≥34, Verify ≥27, Impact ≥20, Engage ≥14) — guards against canonical hubs silently disappearing from the sitemap.
- **Total mini-card link floor: ≥180** across primary lanes + support.
- **Required key-pages allowlist** (13 anchor URLs that must always be discoverable from /sitemap/, including the SCL domain pages, World Readout, Public Good, Domain Verification, and the four canonical hub pages).

This means future sitemap edits cannot regress L1/L2 coverage without an explicit deliberate floor adjustment in the validation script — the floors travel with the code.

### Deferred to follow-up wave (PR 2)

A separate "frontier-level UX uplift" PR follows this one. It will add per-lane page counts, a sticky lane jump-nav with scroll-spy, and a client-side instant search box across all 184 anchors — pure UX layer on top of the synced data.
