---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_faithful_42_3",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/crt-faithful-42-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::crt_faithful_42_3",
  "declaration_slug": "crt-faithful-42-3",
  "kind": "theorem",
  "name": "crt_faithful_42_3",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 203,
  "source_line_end": 205,
  "registry_ids": [
    "III.P22"
  ],
  "related_registry_items": [
    {
      "id": "III.P22",
      "title": "CRT Witness Decomposition",
      "url": "/registry/object/III.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L203-L205",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L203-L205",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L203-L205)
- Source range: L203-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P22` — CRT Witness Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.P22] Structural: CRT decomposition at depth 3 is faithful. -/
```

## Source Excerpt

```lean
theorem crt_faithful_42_3 :
    crt_reconstruct (crt_decompose 42 3) 3 = 42 % primorial 3 := by
  native_decide
```
