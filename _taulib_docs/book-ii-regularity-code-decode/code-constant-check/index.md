---
{
  "projection_kind": "taulib_declaration",
  "title": "code_constant_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-constant-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_constant_check",
  "declaration_slug": "code-constant-check",
  "kind": "def",
  "name": "code_constant_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 113,
  "source_line_end": 129,
  "registry_ids": [
    "II.D51"
  ],
  "related_registry_items": [
    {
      "id": "II.D51",
      "title": "Code Map",
      "url": "/registry/object/II.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L113-L129",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L113-L129",
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
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L113-L129)
- Source range: L113-L129
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D51` — Code Map

## Immediate Comment / Docstring

```lean
/-- [II.D51] Spectral coefficient check for the constant function:
    code_spectral(1, k, pi, v) = P_k / p for each residue class v. -/
```

## Source Excerpt

```lean
def code_constant_check (k_max : TauIdx) : Bool :=
  go 1 1 0 (k_max * 20 + 1)
where
  go (k pi_idx v fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if pi_idx > k then go (k + 1) 1 0 (fuel - 1)
    else
      let p := nth_prime pi_idx
      if p == 0 then go k (pi_idx + 1) 0 (fuel - 1)
      else if v >= p then go k (pi_idx + 1) 0 (fuel - 1)
      else
        let const_1 : TauIdx → Int := fun _ => 1
        let coeff := code_spectral const_1 k pi_idx v
        let expected : Int := (primorial k / p : Nat)
        (coeff == expected) && go k pi_idx (v + 1) (fuel - 1)
  termination_by fuel
```
