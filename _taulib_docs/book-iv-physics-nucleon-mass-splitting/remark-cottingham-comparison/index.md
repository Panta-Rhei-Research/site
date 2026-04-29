---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_cottingham_comparison",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/remark-cottingham-comparison/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::remark_cottingham_comparison",
  "declaration_slug": "remark-cottingham-comparison",
  "kind": "def",
  "name": "remark_cottingham_comparison",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 372,
  "source_line_end": 375,
  "registry_ids": [
    "IV.R394"
  ],
  "related_registry_items": [
    {
      "id": "IV.R394",
      "title": "Comparison to Cottingham decomposition",
      "url": "/registry/object/IV.R394/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L372-L375",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L372-L375",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L372-L375)
- Source range: L372-L375
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R394` — Comparison to Cottingham decomposition

## Immediate Comment / Docstring

```lean
/-- [IV.R394] Cottingham comparison remark.

    Orthodox QCD:
    - EM (Cottingham/Coulomb): ≈ +0.63 MeV (hadron-level, integer charges)
    - QCD (quark mass, m_d > m_u): ≈ +0.66 MeV
    - Total: ≈ 1.29 MeV ✓

    Tau-framework C.5:
    - C-sector (QCD): ≈ +1.413 MeV (quark-level, chi_minus mode)
    - B-sector (EM):  ≈ −0.120 MeV (quark-level, fractional charges)
    - Total: ≈ +1.293 MeV ✓ (33 ppm)

    Factor-5 EM discrepancy (0.63/0.120 ≈ 5.26):
    - Factor 3 explained: tau operates at quark level, alpha_quark ≈ alpha/3
      => 0.63/3 ≈ 0.21 MeV (partial match)
    - Remaining factor ~1.75: vector meson dominance + QCD renormalization
    - Open question OQ.B for Milestone 3
-/
```

## Source Excerpt

```lean
def remark_cottingham_comparison : String :=
  "Orthodox: EM~0.63 MeV + QCD~0.66 MeV. Tau C.5: EM~0.120 MeV + QCD~1.413 MeV. " ++
  "Factor-5 EM discrepancy: tau operates at quark level (alpha/3 fractional charges " ++
  "explains factor 3; remaining ~1.75 from vector meson dominance renormalization)."
```
