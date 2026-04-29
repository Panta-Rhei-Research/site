---
{
  "projection_kind": "taulib_declaration",
  "title": "CPPhaseRemark",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/cpphase-remark/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::CPPhaseRemark",
  "declaration_slug": "cpphase-remark",
  "kind": "structure",
  "name": "CPPhaseRemark",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1180,
  "source_line_end": 1185,
  "registry_ids": [
    "IV.R406"
  ],
  "related_registry_items": [
    {
      "id": "IV.R406",
      "title": "CP Phase delta_CP from A-Sector Rotation: Connects IV.T152 and V.T174",
      "url": "/registry/object/IV.R406/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1180-L1185",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1180-L1185",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1180-L1185)
- Source range: L1180-L1185
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R406` — CP Phase delta_CP from A-Sector Rotation: Connects IV.T152 and V.T174

## Immediate Comment / Docstring

```lean
/-- [IV.R406] CP phase A-sector remark structure (formalized). -/
```

## Source Excerpt

```lean
structure CPPhaseRemark where
  /-- Number of mixing matrices connected (CKM + PMNS). -/
  n_matrices_connected : Nat := 2
  /-- A-sector generator index: π is 2nd of {α,π,γ,η,ω}. -/
  a_sector_generator_index : Nat := 2
  deriving Repr
```
