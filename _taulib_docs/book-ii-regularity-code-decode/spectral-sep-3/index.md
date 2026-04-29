---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_sep_3",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/spectral-sep-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::spectral_sep_3",
  "declaration_slug": "spectral-sep-3",
  "kind": "theorem",
  "name": "spectral_sep_3",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 471,
  "source_line_end": 472,
  "registry_ids": [
    "II.T35"
  ],
  "related_registry_items": [
    {
      "id": "II.T35",
      "title": "Code/Decode Bijection",
      "url": "/registry/object/II.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L471-L472",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L471-L472",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L471-L472)
- Source range: L471-L472
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
-- Spectral separation [II.T35]
```

## Source Excerpt

```lean
theorem spectral_sep_3 :
    code_spectral_separation_check 3 = true := by native_decide
```
