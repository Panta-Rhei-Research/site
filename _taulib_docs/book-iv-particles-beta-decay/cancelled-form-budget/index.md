---
{
  "projection_kind": "taulib_declaration",
  "title": "CancelledFormBudget",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/cancelled-form-budget/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::CancelledFormBudget",
  "declaration_slug": "cancelled-form-budget",
  "kind": "structure",
  "name": "CancelledFormBudget",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 416,
  "source_line_end": 429,
  "registry_ids": [
    "IV.P224"
  ],
  "related_registry_items": [
    {
      "id": "IV.P224",
      "title": "Cancelled-Form Error Budget (77 ppm RSS)",
      "url": "/registry/object/IV.P224/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L416-L429",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L416-L429",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L416-L429)
- Source range: L416-L429
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P224` — Cancelled-Form Error Budget (77 ppm RSS)

## Immediate Comment / Docstring

```lean
/-- [IV.P224] Cancelled-form error budget: RSS = 77 ppm.
    78× improvement over naive Fermi (6030 ppm).
    Theory-limited: RSS (77 ppm) < experimental (570 ppm). -/
```

## Source Excerpt

```lean
structure CancelledFormBudget where
  /-- R⁹ contribution (ppm). -/
  r9_ppm : Nat := 70
  /-- |V_ud|² contribution (ppm). -/
  vud2_ppm : Nat := 33
  /-- f(1+3g_A²) contribution (ppm). -/
  fga_ppm : Nat := 9
  /-- RSS total (ppm). -/
  rss_ppm : Nat := 77
  /-- Naive Fermi (ppm). -/
  naive_ppm : Nat := 6030
  /-- Improvement factor. -/
  improvement : Nat := 78
  deriving Repr
```
