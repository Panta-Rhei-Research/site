---
{
  "projection_kind": "taulib_declaration",
  "title": "full_code_decode_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/full-code-decode-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::full_code_decode_check",
  "declaration_slug": "full-code-decode-check",
  "kind": "def",
  "name": "full_code_decode_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 369,
  "source_line_end": 378,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L369-L378",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L369-L378",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L369-L378)
- Source range: L369-L378
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Full Code/Decode bijection verification:
    - Code extraction (delta, constant checks)
    - Decode well-definedness (periodic)
    - Decode uniqueness (CRT injectivity)
    - Round-trip Decode . Code = id
    - Round-trip Code . Decode = id
    - Delta function round-trip
    - Spectral separation (completeness)
    - Tower compatibility -/
```

## Source Excerpt

```lean
def full_code_decode_check (k_max : TauIdx) : Bool :=
  code_delta_check k_max &&
  code_constant_check k_max &&
  decode_welldef_check k_max 20 &&
  decode_uniqueness_check k_max &&
  code_decode_inverse_check k_max &&
  decode_code_inverse_check k_max &&
  code_decode_delta_check k_max &&
  code_spectral_separation_check k_max &&
  code_decode_tower_check 15 k_max
```
