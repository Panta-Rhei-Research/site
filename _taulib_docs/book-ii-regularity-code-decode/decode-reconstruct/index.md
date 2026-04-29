---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_reconstruct",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-reconstruct/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_reconstruct",
  "declaration_slug": "decode-reconstruct",
  "kind": "def",
  "name": "decode_reconstruct",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 143,
  "source_line_end": 144,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L143-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L143-L144",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L143-L144)
- Source range: L143-L144
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D52` — Decode Map

## Immediate Comment / Docstring

```lean
/-- [II.D52] Decode: reconstruct a function value from its CRT-indexed code.
    Given a table of values indexed by points in Z/P_kZ, decode reads
    the value at the stage-k representative of x.

    decode_reconstruct(table, k, x) = table(reduce(x, k))

    This is the inverse of code_extract: reading back the recorded value
    at the canonical representative. -/
```

## Source Excerpt

```lean
def decode_reconstruct (table : TauIdx → Int) (k x : TauIdx) : Int :=
  table (reduce x k)
```
