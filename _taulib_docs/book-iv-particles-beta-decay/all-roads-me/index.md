---
{
  "projection_kind": "taulib_declaration",
  "title": "AllRoadsME",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/all-roads-me/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::AllRoadsME",
  "declaration_slug": "all-roads-me",
  "kind": "structure",
  "name": "AllRoadsME",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 319,
  "source_line_end": 326,
  "registry_ids": [
    "IV.R127"
  ],
  "related_registry_items": [
    {
      "id": "IV.R127",
      "title": "All roads lead through m_e",
      "url": "/registry/object/IV.R127/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L319-L326",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L319-L326",
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
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L319-L326)
- Source range: L319-L326
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R127` — All roads lead through m_e

## Immediate Comment / Docstring

```lean
/-- [IV.R127] Every atomic-scale prediction factors through
    m_e = m_n/R(ι_τ):
    - a₀ ∝ 1/m_e
    - E₁ ∝ m_e
    - R_∞ ∝ m_e
    - λ ∝ 1/m_e

    The 0.025 ppm precision of m_e is the ceiling for all atomic
    predictions. -/
```

## Source Excerpt

```lean
structure AllRoadsME where
  /-- Number of atomic quantities depending on m_e. -/
  dependent_quantities : Nat := 4
  /-- Precision ceiling (ppm ×1000). -/
  ceiling_ppm_x1000 : Nat := 25
  /-- Improvable by Level 2 correction or better m_n measurement. -/
  improvable : Bool := true
  deriving Repr
```
