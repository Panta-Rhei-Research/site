---
{
  "projection_kind": "taulib_declaration",
  "title": "no_barrier_10_1",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/no-barrier-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::no_barrier_10_1",
  "declaration_slug": "no-barrier-10-1",
  "kind": "theorem",
  "name": "no_barrier_10_1",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 192,
  "source_line_end": 195,
  "registry_ids": [
    "III.T34"
  ],
  "related_registry_items": [
    {
      "id": "III.T34",
      "title": "No Barrier Theorem",
      "url": "/registry/object/III.T34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L192-L195",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L192-L195",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L192-L195)
- Source range: L192-L195
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T34` — No Barrier Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T34] Structural: no-barrier at depth 1. -/
```

## Source Excerpt

```lean
theorem no_barrier_10_1 :
    no_barrier_check 10 1 = true := by native_decide

end Tau.BookIII.Computation
```
