---
{
  "projection_kind": "taulib_declaration",
  "title": "code_decode_id_roundtrip",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-decode-id-roundtrip/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_decode_id_roundtrip",
  "declaration_slug": "code-decode-id-roundtrip",
  "kind": "theorem",
  "name": "code_decode_id_roundtrip",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 488,
  "source_line_end": 493,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L488-L493",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L488-L493",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L488-L493)
- Source range: L488-L493
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Formal proof: Decode . Code = id for the identity function.
    This follows from reduction idempotence: reduce(reduce(x, k), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
theorem code_decode_id_roundtrip (x k : TauIdx) :
    decode_reconstruct (fun a => code_extract (fun n => (n : Int)) k a) k x =
    code_extract (fun n => (n : Int)) k x := by
  simp only [decode_reconstruct, code_extract, reduce]
  congr 1
  exact Nat.mod_mod_of_dvd x (dvd_refl (primorial k))
```
