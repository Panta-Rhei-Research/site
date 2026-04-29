---
{
  "projection_kind": "taulib_declaration",
  "title": "operational_closure_8_3",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/operational-closure-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::operational_closure_8_3",
  "declaration_slug": "operational-closure-8-3",
  "kind": "theorem",
  "name": "operational_closure_8_3",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 222,
  "source_line_end": 223,
  "registry_ids": [
    "III.T57"
  ],
  "related_registry_items": [
    {
      "id": "III.T57",
      "title": "Operational Closure Theorem",
      "url": "/registry/object/III.T57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L222-L223",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L222-L223",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L222-L223)
- Source range: L222-L223
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T57` — Operational Closure Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T57] Operational closure at bound 8, depth 3. -/
```

## Source Excerpt

```lean
theorem operational_closure_8_3 :
    operational_closure_full_check 8 3 = true := by native_decide
```
