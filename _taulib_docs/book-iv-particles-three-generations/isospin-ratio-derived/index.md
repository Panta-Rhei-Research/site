---
{
  "projection_kind": "taulib_declaration",
  "title": "IsospinRatioDerived",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/isospin-ratio-derived/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::IsospinRatioDerived",
  "declaration_slug": "isospin-ratio-derived",
  "kind": "structure",
  "name": "IsospinRatioDerived",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2760,
  "source_line_end": 2769,
  "registry_ids": [
    "IV.P222"
  ],
  "related_registry_items": [
    {
      "id": "IV.P222",
      "title": "m_u/m_d Isospin Ratio from Winding Algebra at +82 ppm",
      "url": "/registry/object/IV.P222/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2760-L2769",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2760-L2769",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2760-L2769)
- Source range: L2760-L2769
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P222` — m_u/m_d Isospin Ratio from Winding Algebra at +82 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.P222] m_u/m_d isospin ratio from winding algebra.
    m_u(direct)/m_d(chain) = 0.4600 at +82 ppm. -/
```

## Source Excerpt

```lean
structure IsospinRatioDerived where
  /-- Ratio (×10000). -/
  ratio_x10000 : Nat := 4600
  /-- PDG ratio (×10000). -/
  pdg_ratio_x10000 : Nat := 4596
  /-- Deviation ppm. -/
  deviation_ppm : Int := 82
  /-- Consistent with NLO scan (+29 ppm). -/
  consistent_nlo : Bool := true
  deriving Repr
```
