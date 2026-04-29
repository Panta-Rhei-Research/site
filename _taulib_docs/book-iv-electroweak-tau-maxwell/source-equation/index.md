---
{
  "projection_kind": "taulib_declaration",
  "title": "SourceEquation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/source-equation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::SourceEquation",
  "declaration_slug": "source-equation",
  "kind": "structure",
  "name": "SourceEquation",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 241,
  "source_line_end": 247,
  "registry_ids": [
    "IV.T43"
  ],
  "related_registry_items": [
    {
      "id": "IV.T43",
      "title": "Inhomogeneous Maxwell Equations",
      "url": "/registry/object/IV.T43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L241-L247",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L241-L247",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L241-L247)
- Source range: L241-L247
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T43` — Inhomogeneous Maxwell Equations

## Immediate Comment / Docstring

```lean
/-- [IV.T43] Source equation d*F = *J: the inhomogeneous Maxwell equations.
    Physical content: Gauss's law (div E = ρ/ε₀) + Ampere-Maxwell. -/
```

## Source Excerpt

```lean
structure SourceEquation where
  /-- d*F = *J holds. -/
  source_eq : Bool := true
  /-- Maxwell equation count from source eq: 2 (Gauss, Ampere). -/
  maxwell_count : Nat
  count_eq : maxwell_count = 2
  deriving Repr
```
