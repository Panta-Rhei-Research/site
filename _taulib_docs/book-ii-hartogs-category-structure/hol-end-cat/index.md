---
{
  "projection_kind": "taulib_declaration",
  "title": "HolEndCat",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/hol-end-cat/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::HolEndCat",
  "declaration_slug": "hol-end-cat",
  "kind": "structure",
  "name": "HolEndCat",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 304,
  "source_line_end": 309,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L304-L309",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L304-L309",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L304-L309)
- Source range: L304-L309
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D41` — Holomorphic Endomorphism Category

## Immediate Comment / Docstring

```lean
/-- [II.D41] The endomorphism category HolEnd_tau.
    Encapsulates: objects (stages), morphisms (tower-coherent maps),
    composition, identity, and the category axioms.

    In the Lean representation, we store:
    - max_stage: the number of stages considered
    - A verification that the axioms hold up to given bounds. -/
```

## Source Excerpt

```lean
structure HolEndCat where
  /-- Maximum stage depth. -/
  max_stage : TauIdx
  /-- Maximum input value for verification. -/
  max_val : TauIdx
  deriving Repr
```
