---
{
  "projection_kind": "taulib_declaration",
  "title": "ChartReadout",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/chart-readout/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::ChartReadout",
  "declaration_slug": "chart-readout",
  "kind": "structure",
  "name": "ChartReadout",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 222,
  "source_line_end": 237,
  "registry_ids": [
    "IV.D257"
  ],
  "related_registry_items": [
    {
      "id": "IV.D257",
      "title": "Chart readout homomorphism",
      "url": "/registry/object/IV.D257/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L222-L237",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.Tau3Arena",
        "url": "/verify/taulib/docs/book-iv-arena-tau3-arena/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L222-L237",
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

- Module: [TauLib.BookIV.Arena.Tau3Arena](/verify/taulib/docs/book-iv-arena-tau3-arena/)
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L222-L237)
- Source range: L222-L237
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D257` — Chart readout homomorphism

## Immediate Comment / Docstring

```lean
/-- [IV.D257] Chart readout homomorphism: the map R: τ³ → ℝ⁴ that projects
    categorical structure to measurable coordinates.
    Target dimension = 1 (temporal) + 3 (spatial) = 4. -/
```

## Source Excerpt

```lean
structure ChartReadout where
  /-- Source dimension (generators). -/
  source_dim : Nat
  source_eq : source_dim = 5
  /-- Target dimension (physical). -/
  target_dim : Nat
  target_eq : target_dim = 4
  /-- Temporal dimensions in target. -/
  temporal : Nat
  temporal_eq : temporal = 1
  /-- Spatial dimensions in target. -/
  spatial : Nat
  spatial_eq : spatial = 3
  /-- Sum check. -/
  dim_sum : temporal + spatial = target_dim
  deriving Repr
```
