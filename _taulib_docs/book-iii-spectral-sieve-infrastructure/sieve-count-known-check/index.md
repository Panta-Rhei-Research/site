---
{
  "projection_kind": "taulib_declaration",
  "title": "sieve_count_known_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/sieve-count-known-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::sieve_count_known_check",
  "declaration_slug": "sieve-count-known-check",
  "kind": "def",
  "name": "sieve_count_known_check",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 173,
  "source_line_end": 178,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L173-L178",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L173-L178",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L173-L178)
- Source range: L173-L178
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T66` — Sieve Correctness

## Immediate Comment / Docstring

```lean
/-- [III.T66] Sieve count matches known values at key points. -/
```

## Source Excerpt

```lean
def sieve_count_known_check : Bool :=
  sieve_prime_count 10 == 4 &&    -- π(10) = 4
  sieve_prime_count 20 == 8 &&    -- π(20) = 8
  sieve_prime_count 30 == 10 &&   -- π(30) = 10
  sieve_prime_count 50 == 15 &&   -- π(50) = 15
  sieve_prime_count 100 == 25     -- π(100) = 25
```
