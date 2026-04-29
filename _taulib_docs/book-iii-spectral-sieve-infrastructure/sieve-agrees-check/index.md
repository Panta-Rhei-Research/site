---
{
  "projection_kind": "taulib_declaration",
  "title": "sieve_agrees_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-agrees-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::sieve_agrees_check",
  "declaration_slug": "sieve-agrees-check",
  "kind": "def",
  "name": "sieve_agrees_check",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 162,
  "source_line_end": 170,
  "registry_ids": [
    "III.T66"
  ],
  "related_registry_items": [
    {
      "id": "III.T66",
      "title": "Sieve Correctness",
      "url": "/registry/object/III.T66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L162-L170",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L162-L170",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L162-L170)
- Source range: L162-L170
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T66` — Sieve Correctness

## Immediate Comment / Docstring

```lean
/-- [III.T66] Sieve agrees with trial division: for all n in [0..bound],
    eratosthenes_sieve n = is_prime_nat n. -/
```

## Source Excerpt

```lean
def sieve_agrees_check (bound : Nat) : Bool :=
  go 0 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      (eratosthenes_sieve n == is_prime_sieve n) && go (n + 1) (fuel - 1)
  termination_by fuel
```
