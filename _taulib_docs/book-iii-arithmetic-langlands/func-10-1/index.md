---
{
  "projection_kind": "taulib_declaration",
  "title": "func_10_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/func-10-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::func_10_1",
  "declaration_slug": "func-10-1",
  "kind": "theorem",
  "name": "func_10_1",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 227,
  "source_line_end": 228,
  "registry_ids": [
    "III.T36"
  ],
  "related_registry_items": [
    {
      "id": "III.T36",
      "title": "Functoriality Theorem",
      "url": "/registry/object/III.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L227-L228",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.Langlands",
        "url": "/verify/taulib/docs/book-iii-arithmetic-langlands/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L227-L228",
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

- Module: [TauLib.BookIII.Arithmetic.Langlands](/verify/taulib/docs/book-iii-arithmetic-langlands/)
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L227-L228)
- Source range: L227-L228
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T36` — Functoriality Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T36] Structural: functoriality at depth 1. -/
```

## Source Excerpt

```lean
theorem func_10_1 :
    functoriality_check 10 1 = true := by native_decide
```
