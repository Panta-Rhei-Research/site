---
{
  "projection_kind": "taulib_declaration",
  "title": "brun_sieve_density",
  "permalink": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/brun-sieve-density/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.SieveInfrastructure`.",
  "declaration_id": "TauLib.BookIII.Spectral.SieveInfrastructure::brun_sieve_density",
  "declaration_slug": "brun-sieve-density",
  "kind": "def",
  "name": "brun_sieve_density",
  "module_name": "TauLib.BookIII.Spectral.SieveInfrastructure",
  "module_url": "/verify/taulib/docs/book-iii-spectral-sieve-infrastructure/",
  "source_line_start": 153,
  "source_line_end": 154,
  "registry_ids": [
    "III.D101"
  ],
  "related_registry_items": [
    {
      "id": "III.D101",
      "title": "Brun Sieve Count",
      "url": "/registry/object/III.D101/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L153-L154",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L153-L154",
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
- Source path: [`TauLib/BookIII/Spectral/SieveInfrastructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/SieveInfrastructure.lean#L153-L154)
- Source range: L153-L154
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D101` — Brun Sieve Count

## Immediate Comment / Docstring

```lean
/-- [III.D101] Brun sieve density: fraction coprime to first d primes.
    Returns (count, total) as a pair. -/
```

## Source Excerpt

```lean
def brun_sieve_density (n d : Nat) : Nat × Nat :=
  (brun_sieve_count n d, n)
```
