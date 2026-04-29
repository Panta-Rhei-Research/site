---
{
  "projection_kind": "taulib_declaration",
  "title": "EtaBarExponentData",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/eta-bar-exponent-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::EtaBarExponentData",
  "declaration_slug": "eta-bar-exponent-data",
  "kind": "structure",
  "name": "EtaBarExponentData",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2027,
  "source_line_end": 2040,
  "registry_ids": [
    "IV.T173"
  ],
  "related_registry_items": [
    {
      "id": "IV.T173",
      "title": "η̄ Exponent Derivation: All from |lobes|=2, |gen|=5 (τ-effective)",
      "url": "/registry/object/IV.T173/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2027-L2040",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2027-L2040",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2027-L2040)
- Source range: L2027-L2040
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T173` — η̄ Exponent Derivation: All from |lobes|=2, |gen|=5 (τ-effective)

## Immediate Comment / Docstring

```lean
/-- [IV.T173] η̄ exponent derivation structure (formalized). -/
```

## Source Excerpt

```lean
structure EtaBarExponentData where
  /-- ι_τ exponent numerator: 1. -/
  iota_exp_numer : Nat := 1
  /-- ι_τ exponent denominator: 4. -/
  iota_exp_denom : Nat := 4
  /-- κ_D exponent numerator: 5. -/
  kappa_d_exp_numer : Nat := 5
  /-- κ_D exponent denominator: 4. -/
  kappa_d_exp_denom : Nat := 4
  /-- √N normalization denominator (N=5 = |generators|). -/
  norm_denom : Nat := 5
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 2285
  deriving Repr
```
