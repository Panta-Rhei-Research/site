---
{
  "projection_kind": "taulib_declaration",
  "title": "SuperfluidVortexQuantization",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/superfluid-vortex-quantization/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::SuperfluidVortexQuantization",
  "declaration_slug": "superfluid-vortex-quantization",
  "kind": "structure",
  "name": "SuperfluidVortexQuantization",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 206,
  "source_line_end": 213,
  "registry_ids": [
    "IV.P137"
  ],
  "related_registry_items": [
    {
      "id": "IV.P137",
      "title": "Superfluid vortex quantization",
      "url": "/registry/object/IV.P137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L206-L213",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L206-L213",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L206-L213)
- Source range: L206-L213
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P137` — Superfluid vortex quantization

## Immediate Comment / Docstring

```lean
/-- [IV.P137] In the superfluid regime every vortex core carries
    theta_core in Z \ {0}, and the total circulation around any loop
    enclosing k cores is 2*pi*hbar_tau/m times the sum of winding numbers.

    Quantization is structural (from pi_1(T^2) = Z^2), not imposed. -/
```

## Source Excerpt

```lean
structure SuperfluidVortexQuantization where
  /-- Vortex charge is nonzero integer. -/
  charge_nonzero_integer : Bool := true
  /-- Circulation quantized. -/
  circulation_quantized : Bool := true
  /-- Structural origin: pi_1(T^2). -/
  structural_origin : String := "pi_1(T^2) = Z^2"
  deriving Repr
```
