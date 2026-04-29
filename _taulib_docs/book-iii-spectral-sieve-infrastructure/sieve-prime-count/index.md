---
{
  "projection_kind": "taulib_declaration",
  "title": "sieve_prime_count",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-prime-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::sieve_prime_count",
  "declaration_slug": "sieve-prime-count",
  "kind": "def",
  "name": "sieve_prime_count",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 94,
  "source_line_end": 103,
  "registry_ids": [
    "III.D100"
  ],
  "related_registry_items": [
    {
      "id": "III.D100",
      "title": "Sieve Prime Count",
      "url": "/registry/object/III.D100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L94-L103",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L94-L103",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L94-L103)
- Source range: L94-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D100` — Sieve Prime Count

## Immediate Comment / Docstring

```lean
/-- [III.D100] π(n): count of primes ≤ n via sieve. -/
```

## Source Excerpt

```lean
def sieve_prime_count (n : Nat) : Nat :=
  go 2 0 (n + 1)
where
  go (k acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if k > n then acc
    else
      let acc' := if eratosthenes_sieve k then acc + 1 else acc
      go (k + 1) acc' (fuel - 1)
  termination_by fuel
```
