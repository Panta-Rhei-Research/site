---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_welldef_3_15",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-welldef-3-15/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_welldef_3_15",
  "declaration_slug": "decode-welldef-3-15",
  "kind": "theorem",
  "name": "decode_welldef_3_15",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 452,
  "source_line_end": 453,
  "registry_ids": [
    "II.D52"
  ],
  "related_registry_items": [
    {
      "id": "II.D52",
      "title": "Decode Map",
      "url": "/registry/object/II.D52/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L452-L453",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.CodeDecode",
        "url": "/verify/taulib/docs/book-ii-regularity-code-decode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L452-L453",
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

- Module: [TauLib.BookII.Regularity.CodeDecode](/verify/taulib/docs/book-ii-regularity-code-decode/)
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L452-L453)
- Source range: L452-L453
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D52` — Decode Map

## Immediate Comment / Docstring

```lean
-- Decode well-definedness [II.D52]
```

## Source Excerpt

```lean
theorem decode_welldef_3_15 :
    decode_welldef_check 3 15 = true := by native_decide
```
