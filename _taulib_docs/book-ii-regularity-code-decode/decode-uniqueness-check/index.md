---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_uniqueness_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_uniqueness_check",
  "declaration_slug": "decode-uniqueness-check",
  "kind": "def",
  "name": "decode_uniqueness_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 172,
  "source_line_end": 187,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L172-L187",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L172-L187",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L172-L187)
- Source range: L172-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D52` — Decode Map

## Immediate Comment / Docstring

```lean
/-- [II.D52] Decode uniqueness check:
    for a != b in [0, P_k), the CRT indicators are different. -/
```

## Source Excerpt

```lean
def decode_uniqueness_check (k_max : TauIdx) : Bool :=
  go 1 0 0 (k_max * 100 + 1)
where
  go (k a b fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let pk := primorial k
      if a >= pk then go (k + 1) 0 0 (fuel - 1)
      else if b >= pk then go k (a + 1) 0 (fuel - 1)
      else if a == b then go k a (b + 1) (fuel - 1)
      else
        let ok := decode_crt_indicator k a a &&
                  !decode_crt_indicator k a b
        ok && go k a (b + 1) (fuel - 1)
  termination_by fuel
```
