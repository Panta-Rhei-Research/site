---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_code_roundtrip",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-code-roundtrip/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_code_roundtrip",
  "declaration_slug": "decode-code-roundtrip",
  "kind": "theorem",
  "name": "decode_code_roundtrip",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 497,
  "source_line_end": 504,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L497-L504",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L497-L504",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L497-L504)
- Source range: L497-L504
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Formal proof: Code . Decode = id for any table.
    This follows from reduce(reduce(a, k), k) = reduce(a, k). -/
```

## Source Excerpt

```lean
theorem decode_code_roundtrip (table : TauIdx → Int) (a k : TauIdx) :
    code_extract (fun x => decode_reconstruct table k x) k a =
    decode_reconstruct table k a := by
  simp only [code_extract, decode_reconstruct, reduce]
  congr 1
  exact Nat.mod_mod_of_dvd a (dvd_refl (primorial k))

end Tau.BookII.Regularity
```
