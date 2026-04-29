---
{
  "projection_kind": "taulib_declaration",
  "title": "arith_preserves_6_3",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/arith-preserves-6-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::arith_preserves_6_3",
  "declaration_slug": "arith-preserves-6-3",
  "kind": "theorem",
  "name": "arith_preserves_6_3",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 233,
  "source_line_end": 234,
  "registry_ids": [
    "III.P36"
  ],
  "related_registry_items": [
    {
      "id": "III.P36",
      "title": "Arithmetic Preserves Operations",
      "url": "/registry/object/III.P36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L233-L234",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L233-L234",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L233-L234)
- Source range: L233-L234
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P36` — Arithmetic Preserves Operations

## Immediate Comment / Docstring

```lean
/-- [III.P36] Operation preservation at bound 6, depth 3. -/
```

## Source Excerpt

```lean
theorem arith_preserves_6_3 :
    arith_preserves_ops_check 6 3 = true := by native_decide
```
