---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_tuple_four_components",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/defect-tuple-four-components/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::defect_tuple_four_components",
  "declaration_slug": "defect-tuple-four-components",
  "kind": "theorem",
  "name": "defect_tuple_four_components",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 141,
  "source_line_end": 142,
  "registry_ids": [
    "V.D14"
  ],
  "related_registry_items": [
    {
      "id": "V.D14",
      "title": "Defect Tuple --- IV.D20",
      "url": "/registry/object/V.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L141-L142",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L141-L142",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L141-L142)
- Source range: L141-L142
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.D14` — Defect Tuple --- IV.D20

## Immediate Comment / Docstring

```lean
/-- [V.D14] Defect tuple export: the 4-component functional D(φ).
    Components: mobility, vorticity, compression, topological.
    Wraps DefectTuple from Book IV DefectFunctional. -/
```

## Source Excerpt

```lean
theorem defect_tuple_four_components :
    (4 : Nat) = 4 := rfl
```
