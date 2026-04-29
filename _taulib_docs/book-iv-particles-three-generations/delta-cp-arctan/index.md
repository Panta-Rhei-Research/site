---
{
  "projection_kind": "taulib_declaration",
  "title": "delta_cp_arctan",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/delta-cp-arctan/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::delta_cp_arctan",
  "declaration_slug": "delta-cp-arctan",
  "kind": "def",
  "name": "delta_cp_arctan",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1925,
  "source_line_end": 1927,
  "registry_ids": [
    "IV.P204"
  ],
  "related_registry_items": [
    {
      "id": "IV.P204",
      "title": "δ_CP = π + arctan(ι_τ) at +9365 ppm",
      "url": "/registry/object/IV.P204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1925-L1927",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1925-L1927",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1925-L1927)
- Source range: L1925-L1927
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P204` — δ_CP = π + arctan(ι_τ) at +9365 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.P204] δ_CP = π + arctan(ι_τ) at +9365 ppm.
    π radians (half-period on L) plus small τ-rotation. PDG 197°. -/
```

## Source Excerpt

```lean
def delta_cp_arctan : String :=
  "δ_CP = π + arctan(ι_τ) = 198.84°, PDG 197°, deviation +9365 ppm. " ++
  "Half-period on L plus master-constant rotation."
```
