---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_id",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/hol-id/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::hol_id",
  "declaration_slug": "hol-id",
  "kind": "def",
  "name": "hol_id",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 79,
  "source_line_end": 80,
  "registry_ids": [
    "II.D40"
  ],
  "related_registry_items": [
    {
      "id": "II.D40",
      "title": "Identity Map",
      "url": "/registry/object/II.D40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L79-L80",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L79-L80",
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
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L79-L80)
- Source range: L79-L80
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D40` — Identity Map

## Immediate Comment / Docstring

```lean
/-- [II.D40] The identity holomorphic endomorphism.
    id(n, k) = reduce(n, k): the canonical projection to Z/M_k Z.

    This is the identity morphism in HolEnd_tau. It is tower-coherent
    by reduction_compat: reduce(reduce(n, l), k) = reduce(n, k). -/
```

## Source Excerpt

```lean
def hol_id (n k : TauIdx) : TauIdx :=
  reduce n k
```
