---
{
  "projection_kind": "taulib_declaration",
  "title": "radical_primorial_5",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/radical-primorial-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::radical_primorial_5",
  "declaration_slug": "radical-primorial-5",
  "kind": "theorem",
  "name": "radical_primorial_5",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 204,
  "source_line_end": 205,
  "registry_ids": [
    "III.T78"
  ],
  "related_registry_items": [
    {
      "id": "III.T78",
      "title": "Radical Primorial 5",
      "url": "/registry/object/III.T78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L204-L205",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCDeep",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L204-L205",
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

- Module: [TauLib.BookIII.Arithmetic.ABCDeep](/verify/taulib/docs/book-iii-arithmetic-abcdeep/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L204-L205)
- Source range: L204-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T78` — Radical Primorial 5

## Immediate Comment / Docstring

```lean
/-- [III.T78] Radical-primorial identity at depth 5: rad(M_k) = M_k. -/
```

## Source Excerpt

```lean
theorem radical_primorial_5 :
    radical_primorial_deep_check 5 = true := by native_decide
```
