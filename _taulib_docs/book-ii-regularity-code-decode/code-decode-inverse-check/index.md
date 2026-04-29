---
{
  "projection_kind": "taulib_declaration",
  "title": "code_decode_inverse_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-decode-inverse-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_decode_inverse_check",
  "declaration_slug": "code-decode-inverse-check",
  "kind": "def",
  "name": "code_decode_inverse_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 199,
  "source_line_end": 222,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L199-L222",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L199-L222",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L199-L222)
- Source range: L199-L222
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Code/Decode round-trip (direction 1): Decode . Code = id.
    For a function f on Z/P_kZ:
      decode(code(f), k, x) = code(f)(reduce(x, k))
      = f(reduce(reduce(x,k), k)) = f(reduce(x,k))

    For x < P_k, reduce(x, k) = x, so this gives f(x). -/
```

## Source Excerpt

```lean
def code_decode_inverse_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 200 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let pk := primorial k
      let delta_0 : TauIdx → Int := fun x => if x == 0 then 1 else 0
      let ok1 := check_roundtrip delta_0 k 0 pk (fuel - 1)
      let const_1 : TauIdx → Int := fun _ => 1
      let ok2 := check_roundtrip const_1 k 0 pk (fuel - 1)
      let id_fn : TauIdx → Int := fun x => (x : Int)
      let ok3 := check_roundtrip id_fn k 0 pk (fuel - 1)
      ok1 && ok2 && ok3 && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_roundtrip (f : TauIdx → Int) (k x fuel : Nat) (pk : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      let coded : TauIdx → Int := fun a => code_extract f k a
      let reconstructed := decode_reconstruct coded k x
      (reconstructed == f x) && check_roundtrip f k (x + 1) (fuel - 1) pk
  termination_by fuel
```
