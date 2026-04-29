---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_prime_sieve_count",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/twin-prime-sieve-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::twin_prime_sieve_count",
  "declaration_slug": "twin-prime-sieve-count",
  "kind": "def",
  "name": "twin_prime_sieve_count",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 50,
  "source_line_end": 59,
  "registry_ids": [
    "III.D105"
  ],
  "related_registry_items": [
    {
      "id": "III.D105",
      "title": "Twin Prime Sieve Count",
      "url": "/registry/object/III.D105/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L50-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L50-L59",
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

- Module: [TauLib.BookIII.Spectral.TwinPrimeDeep](/verify/taulib/docs/book-iii-spectral-twin-prime-deep/)
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L50-L59)
- Source range: L50-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D105` — Twin Prime Sieve Count

## Immediate Comment / Docstring

```lean
/-- [III.D105] Count twin prime pairs (p, p+2) with p ≤ bound via sieve. -/
```

## Source Excerpt

```lean
def twin_prime_sieve_count (bound : Nat) : Nat :=
  go 2 0 (bound + 1)
where
  go (p acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if p > bound then acc
    else
      let hit := if eratosthenes_sieve p && eratosthenes_sieve (p + 2) then 1 else 0
      go (p + 1) (acc + hit) (fuel - 1)
  termination_by fuel
```
