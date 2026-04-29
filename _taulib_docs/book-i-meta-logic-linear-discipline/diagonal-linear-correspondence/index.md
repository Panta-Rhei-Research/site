---
{
  "projection_kind": "taulib_declaration",
  "title": "DiagonalLinearCorrespondence",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/diagonal-linear-correspondence/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.LinearDiscipline`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearDiscipline::DiagonalLinearCorrespondence",
  "declaration_slug": "diagonal-linear-correspondence",
  "kind": "structure",
  "name": "DiagonalLinearCorrespondence",
  "module_name": "TauLib.BookI.MetaLogic.LinearDiscipline",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/",
  "source_line_start": 264,
  "source_line_end": 280,
  "registry_ids": [
    "I.T37"
  ],
  "related_registry_items": [
    {
      "id": "I.T37",
      "title": "Diagonal-Linear Correspondence",
      "url": "/registry/object/I.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L264-L280",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearDiscipline",
        "url": "/verify/taulib/docs/book-i-meta-logic-linear-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L264-L280",
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

- Module: [TauLib.BookI.MetaLogic.LinearDiscipline](/verify/taulib/docs/book-i-meta-logic-linear-discipline/)
- Source path: [`TauLib/BookI/MetaLogic/LinearDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearDiscipline.lean#L264-L280)
- Source range: L264-L280
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.T37` — Diagonal-Linear Correspondence

## Immediate Comment / Docstring

```lean
/-- [I.T37] The Diagonal-Linear Correspondence Theorem.

    The correspondence has three components:
    1. Aspect bijection: 3 diagonal aspects ↔ 3 linear aspects
    2. Resource interpretation: 4 Truth4 values ↔ 4 resource states
    3. Structural classification: 2 refused + 1 preserved = 3 rules

    Together, these establish that K5's diagonal discipline IS the
    !-free fragment of linear logic, restricted to τ's finite universe. -/
```

## Source Excerpt

```lean
structure DiagonalLinearCorrespondence where
  /-- The aspect bijection has 3 components -/
  aspect_count : allDiagonalAspects.length = 3
  /-- The resource interpretation has 4 states matching Truth4 -/
  resource_count : allResourceStates.length = 4
  /-- The aspect bijection is a genuine bijection (round-trip) -/
  aspect_roundtrip_diag : ∀ d, linear_to_diag (diag_to_linear d) = d
  /-- The aspect bijection is a genuine bijection (round-trip) -/
  aspect_roundtrip_linear : ∀ l, diag_to_linear (linear_to_diag l) = l
  /-- The resource interpretation is a genuine bijection (round-trip) -/
  resource_roundtrip_t4 : ∀ v, resource_to_truth4 (truth4_to_resource v) = v
  /-- The resource interpretation is a genuine bijection (round-trip) -/
  resource_roundtrip_rs : ∀ r, truth4_to_resource (resource_to_truth4 r) = r
  /-- Structural rules: exactly 2 refused -/
  rules_refused : refusedRules.length = 2
  /-- Structural rules: exactly 1 preserved -/
  rules_preserved : preservedRules.length = 1
```
