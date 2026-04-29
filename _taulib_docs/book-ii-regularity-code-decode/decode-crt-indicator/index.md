---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_crt_indicator",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-crt-indicator/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_crt_indicator",
  "declaration_slug": "decode-crt-indicator",
  "kind": "def",
  "name": "decode_crt_indicator",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 149,
  "source_line_end": 150,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L149-L150",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L149-L150",
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

- Module: [TauLib.BookII.Regularity.CodeDecode](/verify/taulib/docs/book-ii-regularity-code-decode/)
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L149-L150)
- Source range: L149-L150
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D52` — Decode Map

## Immediate Comment / Docstring

```lean
/-- [II.D52] CRT product indicator: returns true iff reduce(x, k) == target.
    This is the product basis element
    Phi_{v_1,...,v_k}(x) = prod_i E_{k,i,v_i}(x). -/
```

## Source Excerpt

```lean
def decode_crt_indicator (k x target : TauIdx) : Bool :=
  reduce x k == target
```
