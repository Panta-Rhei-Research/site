---
{
  "projection_kind": "taulib_declaration",
  "title": "FluxQuantization",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/flux-quantization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::FluxQuantization",
  "declaration_slug": "flux-quantization",
  "kind": "structure",
  "name": "FluxQuantization",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 253,
  "source_line_end": 260,
  "registry_ids": [
    "IV.P138"
  ],
  "related_registry_items": [
    {
      "id": "IV.P138",
      "title": "Flux quantization",
      "url": "/registry/object/IV.P138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L253-L260",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L253-L260",
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L253-L260)
- Source range: L253-L260
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P138` — Flux quantization

## Immediate Comment / Docstring

```lean
/-- [IV.P138] Flux quantization from topological charge: in the superconductor
    regime, the integrality of theta on T^2 implies magnetic flux through
    any closed surface is quantized: Phi = n * Phi_0, n in Z.

    This is the structural origin of the Abrikosov vortex lattice. -/
```

## Source Excerpt

```lean
structure FluxQuantization where
  /-- Flux = n * Phi_0. -/
  quantized : Bool := true
  /-- Origin: theta integrality on T^2. -/
  origin : String := "theta integrality on T^2"
  /-- Consequence: Abrikosov vortex lattice. -/
  abrikosov : Bool := true
  deriving Repr
```
