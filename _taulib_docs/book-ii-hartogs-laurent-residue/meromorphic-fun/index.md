---
{
  "projection_kind": "taulib_declaration",
  "title": "MeromorphicFun",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/meromorphic-fun/",
  "summary_short": "`structure` declaration in `TauLib.BookII.Hartogs.LaurentResidue`.",
  "declaration_id": "TauLib.BookII.Hartogs.LaurentResidue::MeromorphicFun",
  "declaration_slug": "meromorphic-fun",
  "kind": "structure",
  "name": "MeromorphicFun",
  "module_name": "TauLib.BookII.Hartogs.LaurentResidue",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/",
  "source_line_start": 278,
  "source_line_end": 282,
  "registry_ids": [
    "II.D44"
  ],
  "related_registry_items": [
    {
      "id": "II.D44",
      "title": "Meromorphic Function",
      "url": "/registry/object/II.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L278-L282",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.LaurentResidue",
        "url": "/verify/taulib/docs/book-ii-hartogs-laurent-residue/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L278-L282",
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

- Module: [TauLib.BookII.Hartogs.LaurentResidue](/verify/taulib/docs/book-ii-hartogs-laurent-residue/)
- Source path: [`TauLib/BookII/Hartogs/LaurentResidue.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/LaurentResidue.lean#L278-L282)
- Source range: L278-L282
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `II.D44` — Meromorphic Function

## Immediate Comment / Docstring

```lean
/-- [II.D44] A meromorphic function in the tau-setting:
    a tower-coherent map that is well-defined (holomorphic) at all but
    finitely many exceptional stages.

    In the finite cyclic primorial world, every tower-coherent function
    is automatically meromorphic (there are no essential singularities).
    The "exceptional stages" are stages where the function has special
    behavior (e.g., the output is 0, or the function is not injective).

    We model this as a function f together with a list of exceptional stages. -/
```

## Source Excerpt

```lean
structure MeromorphicFun where
  /-- The underlying function: (input, stage) -> output. -/
  f : TauIdx -> TauIdx -> TauIdx
  /-- Exceptional stages (poles). -/
  poles : List TauIdx
```
