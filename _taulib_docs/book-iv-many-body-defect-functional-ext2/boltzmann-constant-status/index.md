---
{
  "projection_kind": "taulib_declaration",
  "title": "BoltzmannConstantStatus",
  "permalink": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/boltzmann-constant-status/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.DefectFunctionalExt2`.",
  "declaration_id": "TauLib.BookIV.ManyBody.DefectFunctionalExt2::BoltzmannConstantStatus",
  "declaration_slug": "boltzmann-constant-status",
  "kind": "structure",
  "name": "BoltzmannConstantStatus",
  "module_name": "TauLib.BookIV.ManyBody.DefectFunctionalExt2",
  "module_url": "/verify/taulib/docs/book-iv-many-body-defect-functional-ext2/",
  "source_line_start": 302,
  "source_line_end": 309,
  "registry_ids": [
    "IV.P139"
  ],
  "related_registry_items": [
    {
      "id": "IV.P139",
      "title": "Status of Boltzmann constant",
      "url": "/registry/object/IV.P139/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L302-L309",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L302-L309",
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
- Source path: [`TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/DefectFunctionalExt2.lean#L302-L309)
- Source range: L302-L309
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P139` — Status of Boltzmann constant

## Immediate Comment / Docstring

```lean
/-- [IV.P139] The Boltzmann constant k_B is an SI conversion factor,
    not an ontic tau-constant. It converts dimensionless tau-temperature
    to kelvin. In the tau-framework temperature is already dimensionless. -/
```

## Source Excerpt

```lean
structure BoltzmannConstantStatus where
  /-- k_B is a conversion factor. -/
  is_conversion_factor : Bool := true
  /-- Not an ontic constant. -/
  not_ontic : Bool := true
  /-- tau-temperature is dimensionless. -/
  tau_temp_dimensionless : Bool := true
  deriving Repr
```
