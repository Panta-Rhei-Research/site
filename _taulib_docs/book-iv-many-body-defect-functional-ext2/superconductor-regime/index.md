---
{
  "projection_kind": "taulib_declaration",
  "title": "SuperconductorRegime",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/superconductor-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::SuperconductorRegime",
  "declaration_slug": "superconductor-regime",
  "kind": "structure",
  "name": "SuperconductorRegime",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 231,
  "source_line_end": 240,
  "registry_ids": [
    "IV.D227"
  ],
  "related_registry_items": [
    {
      "id": "IV.D227",
      "title": "Superconductor regime",
      "url": "/registry/object/IV.D227/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L231-L240",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
        "url": "/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L231-L240",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.ManyBody.DefectFunctionalExt2](/corpus/taulib/docs/book-iv-many-body-defect-functional-ext2/)
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L231-L240)
- Source range: L231-L240
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D227` — Superconductor regime

## Immediate Comment / Docstring

```lean
/-- [IV.D227] The superconductor regime: B-sector mobility mu_B = mu_max,
    theta in Z (quantized), and magnetic flux is quantized in units
    of Phi_0 = h/(2e). The Meissner effect (flux expulsion) follows
    from the B-sector superfluid structure. -/
```

## Source Excerpt

```lean
structure SuperconductorRegime where
  /-- B-sector maximal mobility. -/
  b_sector_maximal : Bool := true
  /-- Topological charge quantized. -/
  theta_quantized : Bool := true
  /-- Magnetic flux quantized. -/
  flux_quantized : Bool := true
  /-- Meissner effect from B-sector superfluid. -/
  meissner : Bool := true
  deriving Repr
```
