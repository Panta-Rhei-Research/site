---
{
  "projection_kind": "taulib_declaration",
  "title": "MembraneAssembly",
  "permalink": "/verify/taulib/docs/book-vi-agency-metabolic-energy/membrane-assembly/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.MetabolicEnergy`.",
  "declaration_id": "TauLib.BookVI.Agency.MetabolicEnergy::MembraneAssembly",
  "declaration_slug": "membrane-assembly",
  "kind": "structure",
  "name": "MembraneAssembly",
  "module_name": "TauLib.BookVI.Agency.MetabolicEnergy",
  "module_url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/",
  "source_line_start": 162,
  "source_line_end": 169,
  "registry_ids": [
    "VI.P12"
  ],
  "related_registry_items": [
    {
      "id": "VI.P12",
      "title": "Self-Assembly as Boundary-Induced Distinction",
      "url": "/registry/object/VI.P12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L162-L169",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.MetabolicEnergy",
        "url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L162-L169",
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

- Module: [TauLib.BookVI.Agency.MetabolicEnergy](/verify/taulib/docs/book-vi-agency-metabolic-energy/)
- Source path: [`TauLib/BookVI/Agency/MetabolicEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L162-L169)
- Source range: L162-L169
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P12` — Self-Assembly as Boundary-Induced Distinction

## Immediate Comment / Docstring

```lean
/-- [VI.P12] Self-Assembly as Boundary-Induced Distinction.
    Amphiphilic self-assembly produces L = S¹ ∨ S¹ boundary
    without requiring a template or external information.
    The lemniscate topology is the ONLY self-assembling 2_τ boundary. -/
```

## Source Excerpt

```lean
structure MembraneAssembly where
  /-- Self-assembles (no template needed). -/
  no_template : Bool := true
  /-- Produces L topology. -/
  produces_lemniscate : Bool := true
  /-- Unique self-assembling boundary. -/
  unique : Bool := true
  deriving Repr
```
