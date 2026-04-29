---
{
  "projection_kind": "taulib_declaration",
  "title": "root_of_unity_one",
  "permalink": "/verify/taulib/docs/book-i-boundary-cyclotomic/root-of-unity-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Cyclotomic`.",
  "declaration_id": "TauLib.BookI.Boundary.Cyclotomic::root_of_unity_one",
  "declaration_slug": "root-of-unity-one",
  "kind": "theorem",
  "name": "root_of_unity_one",
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_url": "/verify/taulib/docs/book-i-boundary-cyclotomic/",
  "source_line_start": 58,
  "source_line_end": 59,
  "registry_ids": [
    "I.T45"
  ],
  "related_registry_items": [
    {
      "id": "I.T45",
      "title": "Roots of Unity CRT Decomposition",
      "url": "/registry/object/I.T45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L58-L59",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Cyclotomic",
        "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L58-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Boundary.Cyclotomic](/verify/taulib/docs/book-i-boundary-cyclotomic/)
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L58-L59)
- Source range: L58-L59
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T45` — Roots of Unity CRT Decomposition

## Immediate Comment / Docstring

```lean
/-- [I.T45] 1 is always an nth root of unity mod any m. -/
```

## Source Excerpt

```lean
theorem root_of_unity_one (n m : TauIdx) : IsRootOfUnity n 1 m := by
  simp only [IsRootOfUnity, one_pow]
```
