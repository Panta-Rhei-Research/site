---
{
  "projection_kind": "taulib_declaration",
  "title": "holend_axioms_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/holend-axioms-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::holend_axioms_check",
  "declaration_slug": "holend-axioms-check",
  "kind": "def",
  "name": "holend_axioms_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 322,
  "source_line_end": 327,
  "registry_ids": [
    "II.D41"
  ],
  "related_registry_items": [
    {
      "id": "II.D41",
      "title": "Holomorphic Endomorphism Category",
      "url": "/registry/object/II.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L322-L327",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/verify/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L322-L327",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L322-L327)
- Source range: L322-L327
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D41` — Holomorphic Endomorphism Category

## Immediate Comment / Docstring

```lean
/-- [II.D41] Full category axiom check for HolEnd_tau:
    1. Associativity (II.T29)
    2. Left unit law
    3. Right unit law
    4. Tower coherence preservation under composition -/
```

## Source Excerpt

```lean
def holend_axioms_check (cat : HolEndCat) : Bool :=
  hol_assoc_check cat.max_val cat.max_stage &&
  hol_assoc_triple_check cat.max_val cat.max_stage &&
  left_unit_check cat.max_val cat.max_stage &&
  right_unit_check cat.max_val cat.max_stage &&
  tower_coherent_comp_check cat.max_val cat.max_stage
```
