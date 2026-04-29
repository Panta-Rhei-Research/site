---
{
  "projection_kind": "taulib_declaration",
  "title": "hol_comp",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/hol-comp/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::hol_comp",
  "declaration_slug": "hol-comp",
  "kind": "def",
  "name": "hol_comp",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 59,
  "source_line_end": 61,
  "registry_ids": [
    "II.D39"
  ],
  "related_registry_items": [
    {
      "id": "II.D39",
      "title": "Composition of Holomorphic Maps",
      "url": "/registry/object/II.D39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L59-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L59-L61",
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
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L59-L61)
- Source range: L59-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D39` — Composition of Holomorphic Maps

## Immediate Comment / Docstring

```lean
/-- [II.D39] Holomorphic composition at the TauIdx level.
    Given two tower-coherent endomorphisms f, g on the primorial tower,
    their composition applies g first, then f, at each stage k.

    (f . g)(n, k) = f(g(n, k), k)

    This is the pointwise composition of stage-k maps, which preserves
    tower coherence because both f and g are reduce-compatible. -/
```

## Source Excerpt

```lean
def hol_comp (f g : TauIdx -> TauIdx -> TauIdx)
    (n k : TauIdx) : TauIdx :=
  f (g n k) k
```
