---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_independence_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-crt/prime-independence-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.CRT`.",
  "declaration_id": "TauLib.BookIII.Spectral.CRT::prime_independence_check",
  "declaration_slug": "prime-independence-check",
  "kind": "def",
  "name": "prime_independence_check",
  "module_name": "TauLib.BookIII.Spectral.CRT",
  "module_url": "/verify/taulib/docs/book-iii-spectral-crt/",
  "source_line_start": 169,
  "source_line_end": 195,
  "registry_ids": [
    "III.P05"
  ],
  "related_registry_items": [
    {
      "id": "III.P05",
      "title": "Independence of Prime-Level Actions",
      "url": "/registry/object/III.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L169-L195",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.CRT",
        "url": "/verify/taulib/docs/book-iii-spectral-crt/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L169-L195",
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

- Module: [TauLib.BookIII.Spectral.CRT](/verify/taulib/docs/book-iii-spectral-crt/)
- Source path: [`TauLib/BookIII/Spectral/CRT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/CRT.lean#L169-L195)
- Source range: L169-L195
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P05` — Independence of Prime-Level Actions

## Immediate Comment / Docstring

```lean
/-- [III.P05] Prime-level independence: modifying one residue does not
    affect others. The CRT structure guarantees orthogonality. -/
```

## Source Excerpt

```lean
def prime_independence_check (bound db : TauIdx) : Bool :=
  go 0 1 0 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x k i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 0 (fuel - 1)
    else if i >= k then go x (k + 1) 0 (fuel - 1)
    else
      -- CRT basis element e_i: 1 at position i, 0 elsewhere
      let basis := crt_basis k i
      let residues := crt_decompose basis k
      -- Check: residue at i is 1 (mod p_{i+1}), all others are 0
      let p_i := nth_prime (i + 1)
      let diag_ok := if p_i > 0 then residues.getD i 0 % p_i == 1 % p_i
                     else true
      let off_diag_ok := check_off_diag residues i 0 k
      diag_ok && off_diag_ok && go x k (i + 1) (fuel - 1)
  termination_by fuel
  check_off_diag (residues : List TauIdx) (i j k : Nat) : Bool :=
    if j >= k then true
    else if j == i then check_off_diag residues i (j + 1) k
    else
      let p_j := nth_prime (j + 1)
      let ok := if p_j > 0 then residues.getD j 0 % p_j == 0
                else true
      ok && check_off_diag residues i (j + 1) k
```
