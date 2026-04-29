---
{
  "projection_kind": "taulib_declaration",
  "title": "sieve_primes",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-primes/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::sieve_primes",
  "declaration_slug": "sieve-primes",
  "kind": "def",
  "name": "sieve_primes",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 78,
  "source_line_end": 87,
  "registry_ids": [
    "III.D99"
  ],
  "related_registry_items": [
    {
      "id": "III.D99",
      "title": "Eratosthenes Sieve",
      "url": "/registry/object/III.D99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L78-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L78-L87",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L78-L87)
- Source range: L78-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D99` — Eratosthenes Sieve

## Immediate Comment / Docstring

```lean
/-- [III.D99] Collect all primes up to bound via sieve. -/
```

## Source Excerpt

```lean
def sieve_primes (bound : Nat) : List Nat :=
  go 2 [] (bound + 1)
where
  go (k : Nat) (acc : List Nat) (fuel : Nat) : List Nat :=
    if fuel = 0 then acc
    else if k > bound then acc
    else
      let acc' := if eratosthenes_sieve k then acc ++ [k] else acc
      go (k + 1) acc' (fuel - 1)
  termination_by fuel
```
