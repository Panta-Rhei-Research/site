---
{
  "projection_kind": "taulib_declaration",
  "title": "code_decode_delta_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-decode-delta-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_decode_delta_check",
  "declaration_slug": "code-decode-delta-check",
  "kind": "def",
  "name": "code_decode_delta_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 306,
  "source_line_end": 331,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L306-L331",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L306-L331",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L306-L331)
- Source range: L306-L331
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T35` — Code/Decode Bijection

## Immediate Comment / Docstring

```lean
/-- [II.T35] Delta function round-trip:
    decode(code(delta_a)) = delta_a for all a in [0, P_k). -/
```

## Source Excerpt

```lean
def code_decode_delta_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 200 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      let pk := primorial k
      let ok := check_deltas k 0 pk (fuel - 1)
      ok && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_deltas (k a fuel : Nat) (pk : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else
      let delta_a : TauIdx → Int := fun x => if x == a then 1 else 0
      let coded : TauIdx → Int := fun x => code_extract delta_a k x
      let val_at_a := decode_reconstruct coded k a
      let other := if a + 1 < pk then a + 1 else if a > 0 then a - 1 else 0
      let val_at_other := if pk > 1
        then decode_reconstruct coded k other
        else 0
      let ok := val_at_a == 1 &&
        (pk ≤ 1 || other == a || val_at_other == 0)
      ok && check_deltas k (a + 1) (fuel - 1) pk
  termination_by fuel
```
