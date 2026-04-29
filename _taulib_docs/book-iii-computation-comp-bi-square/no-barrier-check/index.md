---
{
  "projection_kind": "taulib_declaration",
  "title": "no_barrier_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/no-barrier-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::no_barrier_check",
  "declaration_slug": "no-barrier-check",
  "kind": "def",
  "name": "no_barrier_check",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 142,
  "source_line_end": 146,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L142-L146",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L142-L146",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L142-L146)
- Source range: L142-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T34` — No Barrier Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T34] No Barrier: no encoding gap between external/internal
    computation. Verified by: (1) TTM τ-nativity (code = data),
    (2) operational closure (no meta-level), (3) interface width
    principle (finite determination). -/
```

## Source Excerpt

```lean
def no_barrier_check (bound db : TauIdx) : Bool :=
  let nativity := ttm_nativity_check bound db
  let closure := operational_closure_check bound db
  let width := width_principle_check bound db
  nativity && closure && width
```
