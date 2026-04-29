---
{
  "projection_kind": "taulib_declaration",
  "title": "hl_constant_decreasing_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/hl-constant-decreasing-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::hl_constant_decreasing_check",
  "declaration_slug": "hl-constant-decreasing-check",
  "kind": "def",
  "name": "hl_constant_decreasing_check",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 84,
  "source_line_end": 94,
  "registry_ids": [
    "III.T74"
  ],
  "related_registry_items": [
    {
      "id": "III.T74",
      "title": "HL Constant Convergence",
      "url": "/registry/object/III.T74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L84-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L84-L94",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L84-L94)
- Source range: L84-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T74` — HL Constant Convergence

## Immediate Comment / Docstring

```lean
/-- [III.T74] HL constant is decreasing: C₂(k+1) ≤ C₂(k). -/
```

## Source Excerpt

```lean
def hl_constant_decreasing_check (lo hi : Nat) : Bool :=
  go lo (hi - lo + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= hi then true
    else
      let (n1, d1) := hl_twin_constant_approx k
      let (n2, d2) := hl_twin_constant_approx (k + 1)
      (n2 * d1 <= n1 * d2) && go (k + 1) (fuel - 1)
  termination_by fuel
```
