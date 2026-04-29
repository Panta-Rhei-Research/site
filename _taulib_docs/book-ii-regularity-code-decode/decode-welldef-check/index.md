---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_welldef_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-welldef-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_welldef_check",
  "declaration_slug": "decode-welldef-check",
  "kind": "def",
  "name": "decode_welldef_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 155,
  "source_line_end": 168,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L155-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L155-L168",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L155-L168)
- Source range: L155-L168
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D52` — Decode Map

## Immediate Comment / Docstring

```lean
/-- [II.D52] Decode well-definedness check:
    verify that decode is periodic: decode(table, k, x) = decode(table, k, x + P_k).
    This follows from reduce(x + P_k, k) = reduce(x, k). -/
```

## Source Excerpt

```lean
def decode_welldef_check (k_max bound : TauIdx) : Bool :=
  go 1 0 (k_max * bound + k_max + bound + 1)
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if x >= primorial k then go (k + 1) 0 (fuel - 1)
    else
      let table : TauIdx → Int := fun n => (n : Int)
      let pk := primorial k
      let val1 := decode_reconstruct table k x
      let val2 := decode_reconstruct table k (x + pk)
      (val1 == val2) && go k (x + 1) (fuel - 1)
  termination_by fuel
```
