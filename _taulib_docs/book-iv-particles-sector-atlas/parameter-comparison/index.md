---
{
  "projection_kind": "taulib_declaration",
  "title": "ParameterComparison",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/parameter-comparison/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::ParameterComparison",
  "declaration_slug": "parameter-comparison",
  "kind": "structure",
  "name": "ParameterComparison",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 243,
  "source_line_end": 252,
  "registry_ids": [
    "IV.R109"
  ],
  "related_registry_items": [
    {
      "id": "IV.R109",
      "title": "SM parameter count comparison",
      "url": "/registry/object/IV.R109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L243-L252",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SectorAtlas",
        "url": "/verify/taulib/docs/book-iv-particles-sector-atlas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L243-L252",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L243-L252)
- Source range: L243-L252
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R109` — SM parameter count comparison

## Immediate Comment / Docstring

```lean
/-- [IV.R109] Parameter count comparison:
    - Standard Model: ~19 free parameters
    - Category τ: 9 canonical generators, of which only 1 (ι_τ) is
      a numerical constant; the remaining 8 are structural objects
      uniquely determined by the boundary algebra.

    Reduction: 19 free parameters → 1 master constant. -/
```

## Source Excerpt

```lean
structure ParameterComparison where
  /-- SM free parameters. -/
  sm_params : Nat := 19
  /-- τ canonical generators. -/
  tau_generators : Nat := 9
  /-- Of which numerical constants. -/
  tau_numerical : Nat := 1
  /-- Of which structural (determined by algebra). -/
  tau_structural : Nat := 8
  deriving Repr
```
