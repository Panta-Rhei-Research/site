---
{
  "projection_kind": "taulib_declaration",
  "title": "hl_twin_constant_approx",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/hl-twin-constant-approx/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::hl_twin_constant_approx",
  "declaration_slug": "hl-twin-constant-approx",
  "kind": "def",
  "name": "hl_twin_constant_approx",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 68,
  "source_line_end": 81,
  "registry_ids": [
    "III.D106"
  ],
  "related_registry_items": [
    {
      "id": "III.D106",
      "title": "Hardy-Littlewood Constant",
      "url": "/registry/object/III.D106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L68-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L68-L81",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L68-L81)
- Source range: L68-L81
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D106` — Hardy-Littlewood Constant

## Immediate Comment / Docstring

```lean
/-- [III.D106] Hardy-Littlewood twin constant C₂(k) approximation.
    C₂(k) = ∏_{i=2}^{k} p_i(p_i-2)/(p_i-1)² (starting from p₂=3).
    Returns (numerator, denominator) as integers. -/
```

## Source Excerpt

```lean
def hl_twin_constant_approx (k : Nat) : Nat × Nat :=
  go 2 1 1 (k + 1)
where
  go (i num den fuel : Nat) : Nat × Nat :=
    if fuel = 0 then (num, den)
    else if i > k then (num, den)
    else
      let p := nth_prime i
      if p < 3 then go (i + 1) num den (fuel - 1)
      else
        let num' := num * (p * (p - 2))
        let den' := den * ((p - 1) * (p - 1))
        go (i + 1) num' den' (fuel - 1)
  termination_by fuel
```
