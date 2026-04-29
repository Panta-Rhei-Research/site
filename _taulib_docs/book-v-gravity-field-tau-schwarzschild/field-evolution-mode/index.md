---
{
  "projection_kind": "taulib_declaration",
  "title": "FieldEvolutionMode",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/field-evolution-mode/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::FieldEvolutionMode",
  "declaration_slug": "field-evolution-mode",
  "kind": "inductive",
  "name": "FieldEvolutionMode",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 154,
  "source_line_end": 161,
  "registry_ids": [
    "V.D65"
  ],
  "related_registry_items": [
    {
      "id": "V.D65",
      "title": "BH evolution modes --- V.D09",
      "url": "/registry/object/V.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L154-L161",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L154-L161",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L154-L161)
- Source range: L154-L161
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D65` — BH evolution modes --- V.D09

## Immediate Comment / Docstring

```lean
/-- [V.D65] The BH evolution modes in the gravitational field context.

    Extends `BHEvolutionMode` with two pre-maturity phases:
    GeometricRelax and TopologicalRelax. -/
```

## Source Excerpt

```lean
inductive FieldEvolutionMode where
  /-- Geometric relaxation phase (pre-maturity). -/
  | GeometricRelax
  /-- Topological relaxation (topology change). -/
  | TopologicalRelax
  /-- Mature evolution (one of three BH modes). -/
  | MatureEvolution (mode : BHEvolutionMode)
  deriving Repr
```
