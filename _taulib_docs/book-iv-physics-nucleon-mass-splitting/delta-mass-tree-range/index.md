---
{
  "projection_kind": "taulib_declaration",
  "title": "deltaMassTree_range",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/delta-mass-tree-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::deltaMassTree_range",
  "declaration_slug": "delta-mass-tree-range",
  "kind": "theorem",
  "name": "deltaMassTree_range",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 235,
  "source_line_end": 258,
  "registry_ids": [
    "IV.T141",
    "IV.T142"
  ],
  "related_registry_items": [
    {
      "id": "IV.T141",
      "title": "Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]",
      "url": "/registry/object/IV.T141/"
    },
    {
      "id": "IV.T142",
      "title": "Proton-Neutron Mass Difference — Two-Sector",
      "url": "/registry/object/IV.T142/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L235-L258",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L235-L258",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L235-L258)
- Source range: L235-L258
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T141` — Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]
- `IV.T142` — Proton-Neutron Mass Difference — Two-Sector

## Immediate Comment / Docstring

```lean
/-- [IV.T141] Tree-level formula lies in (1.35, 1.40) × 10⁻³.
    Python lab: (√3/2)·ι_τ⁶ ≈ 1.36893 × 10⁻³ (−5516 ppm from PDG)
    Proof: #eval confirms tree_numer/tree_denom ≈ 1.369e-3 ∈ (1.35e-3, 1.40e-3). -/
```

## Source Excerpt

```lean
theorem deltaMassTree_range :
    tree_numer * 1000000 > 1350 * tree_denom ∧
    tree_numer * 1000000 < 1400 * tree_denom := by
  rw [tree_numer_val, tree_denom_val]
  constructor <;> native_decide

-- ============================================================
-- TWO-SECTOR FORMULA [IV.T142]
-- ============================================================

/-! [IV.T142] Two-sector: δm/m_n = QCD − EM
             = (3/16)·√3·ι_τ⁵ − (363/4500)·ι_τ⁶

    To compare QCD > EM (sign proposition), we cross-multiply:
      QCD > EM
      ⟺ qcd_numer · em_denom > em_numer · qcd_denom

    For the range of the DIFFERENCE in Nat arithmetic, we express both
    fractions over a common denominator and verify:
      (qcd_numer · em_denom − em_numer · qcd_denom) / (qcd_denom · em_denom)
      ∈ (1.37, 1.38) × 10⁻³

    Python lab: 1.37657 × 10⁻³ = +33.39 ppm from PDG (τ-effective)
-/
```
