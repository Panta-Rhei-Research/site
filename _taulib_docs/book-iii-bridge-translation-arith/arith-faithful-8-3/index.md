---
{
  "projection_kind": "taulib_declaration",
  "title": "arith_faithful_8_3",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/arith-faithful-8-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::arith_faithful_8_3",
  "declaration_slug": "arith-faithful-8-3",
  "kind": "theorem",
  "name": "arith_faithful_8_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 229,
  "source_line_end": 230,
  "registry_ids": [
    "III.T59"
  ],
  "related_registry_items": [
    {
      "id": "III.T59",
      "title": "Arithmetic Faithfulness",
      "url": "/registry/object/III.T59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L229-L230",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationArith",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L229-L230",
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

- Module: [TauLib.BookIII.Bridge.TranslationArith](/verify/taulib/docs/book-iii-bridge-translation-arith/)
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L229-L230)
- Source range: L229-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T59` — Arithmetic Faithfulness

## Immediate Comment / Docstring

```lean
/-- [III.T59] Arithmetic faithfulness at bound 8, depth 3. -/
```

## Source Excerpt

```lean
theorem arith_faithful_8_3 :
    arith_faithful_check 8 3 = true := by native_decide
```
