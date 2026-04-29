---
{
  "projection_kind": "taulib_declaration",
  "title": "sieve_crt_compat_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-crt-compat-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::sieve_crt_compat_check",
  "declaration_slug": "sieve-crt-compat-check",
  "kind": "def",
  "name": "sieve_crt_compat_check",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 247,
  "source_line_end": 259,
  "registry_ids": [
    "III.P42"
  ],
  "related_registry_items": [
    {
      "id": "III.P42",
      "title": "Sieve-CRT Compatibility",
      "url": "/registry/object/III.P42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L247-L259",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.SieveInfrastructure",
        "url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L247-L259",
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

- Module: [TauLib.BookIII.Spectral.SieveInfrastructure](/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/)
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L247-L259)
- Source range: L247-L259
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P42` — Sieve-CRT Compatibility

## Immediate Comment / Docstring

```lean
/-- [III.P42] Sieve-CRT compatibility: n is divisible by p_i (i ≤ k)
    iff the i-th CRT residue (n mod p_i) equals 0. -/
```

## Source Excerpt

```lean
def sieve_crt_compat_check (bound db : Nat) : Bool :=
  go 1 1 ((bound + 1) * (db + 1))
where
  go (n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else if k > db then go (n + 1) 1 (fuel - 1)
    else
      let residues := crt_decompose n k
      let has_zero := residues.any (· == 0)
      let divisible := divisible_by_small_prime n k
      (has_zero == divisible) && go n (k + 1) (fuel - 1)
  termination_by fuel
```
