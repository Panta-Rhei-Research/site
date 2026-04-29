---
{
  "projection_kind": "taulib_declaration",
  "title": "IsospinExponent",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/isospin-exponent/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::IsospinExponent",
  "declaration_slug": "isospin-exponent",
  "kind": "structure",
  "name": "IsospinExponent",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2925,
  "source_line_end": 2943,
  "registry_ids": [
    "IV.T201"
  ],
  "related_registry_items": [
    {
      "id": "IV.T201",
      "title": "m_u/m_d Isospin Exponent from Higgs-Mediated Splitting",
      "url": "/registry/object/IV.T201/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2925-L2943",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2925-L2943",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2925-L2943)
- Source range: L2925-L2943
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T201` — m_u/m_d Isospin Exponent from Higgs-Mediated Splitting

## Immediate Comment / Docstring

```lean
/-- [IV.T201] m_u/m_d isospin exponent from Higgs-mediated splitting.
    β(u/d) = lobes · n_H / W₃(4) = 14/5. -/
```

## Source Excerpt

```lean
structure IsospinExponent where
  /-- Numerator: lobes × n_H. -/
  exp_num : Nat := 14
  /-- Denominator: W₃(4). -/
  exp_den : Nat := 5
  /-- Higgs crossing number. -/
  n_H : Nat := 7
  /-- Lemniscate lobes. -/
  lobes : Nat := 2
  /-- Deviation from PDG (ppm). -/
  deviation_ppm : Int := 82
  /-- Numerator check: lobes × n_H. -/
  num_check : 2 * 7 = exp_num := by decide
  /-- NLO coefficient 5/8 = W₃(4)/lobes³. -/
  nlo_coeff_num : Nat := 5
  nlo_coeff_den : Nat := 8
  /-- NLO coefficient check. -/
  nlo_check : 2 ^ 3 = nlo_coeff_den := by decide
  deriving Repr
```
