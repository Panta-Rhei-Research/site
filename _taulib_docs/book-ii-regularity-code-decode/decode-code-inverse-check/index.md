---
{
  "projection_kind": "taulib_declaration",
  "title": "decode_code_inverse_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/decode-code-inverse-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::decode_code_inverse_check",
  "declaration_slug": "decode-code-inverse-check",
  "kind": "def",
  "name": "decode_code_inverse_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 230,
  "source_line_end": 249,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L230-L249",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L230-L249",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L230-L249)
- Source range: L230-L249
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Code/Decode round-trip (direction 2): Code . Decode = id.
    For a coefficient table c : Z/P_kZ → Int:
      code(decode(c), k, a) = decode(c)(reduce(a, k))
      = c(reduce(reduce(a,k), k)) = c(reduce(a,k))

    For a < P_k, this gives c(a). -/
```

## Source Excerpt

```lean
def decode_code_inverse_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 200 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let pk := primorial k
      let table : TauIdx → Int := fun a => (a : Int) + 1
      let ok := check_inverse table k 0 pk (fuel - 1)
      ok && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_inverse (table : TauIdx → Int) (k a fuel : Nat) (pk : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else
      let decoded_fn : TauIdx → Int := fun x => decode_reconstruct table k x
      let recoded := code_extract decoded_fn k a
      (recoded == table a) && check_inverse table k (a + 1) (fuel - 1) pk
  termination_by fuel
```
