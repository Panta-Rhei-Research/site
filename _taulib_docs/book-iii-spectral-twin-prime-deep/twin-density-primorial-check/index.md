---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_density_primorial_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/twin-density-primorial-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::twin_density_primorial_check",
  "declaration_slug": "twin-density-primorial-check",
  "kind": "def",
  "name": "twin_density_primorial_check",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 150,
  "source_line_end": 161,
  "registry_ids": [
    "III.T73"
  ],
  "related_registry_items": [
    {
      "id": "III.T73",
      "title": "Twin Density Primorial",
      "url": "/registry/object/III.T73/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L150-L161",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L150-L161",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L150-L161)
- Source range: L150-L161
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T73` — Twin Density Primorial

## Immediate Comment / Docstring

```lean
/-- [III.T73] Twin prime density: at least one twin pair exists at
    each primorial level k ≥ 2 (M_1=2 is too small).
    Uses min(M_k, 500) for computability. -/
```

## Source Excerpt

```lean
def twin_density_primorial_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      let bound := min pk 500
      let count := twin_prime_sieve_count bound
      count > 0 && go (k + 1) (fuel - 1)
  termination_by fuel
```
