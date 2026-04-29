---
{
  "projection_kind": "taulib_declaration",
  "title": "em_in_range",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/em-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::em_in_range",
  "declaration_slug": "em-in-range",
  "kind": "theorem",
  "name": "em_in_range",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 198,
  "source_line_end": 215,
  "registry_ids": [
    "IV.D342",
    "IV.T141"
  ],
  "related_registry_items": [
    {
      "id": "IV.D342",
      "title": "EM Coulomb Contribution to p-n splitting",
      "url": "/registry/object/IV.D342/"
    },
    {
      "id": "IV.T141",
      "title": "Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]",
      "url": "/registry/object/IV.T141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L198-L215",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L198-L215",
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L198-L215)
- Source range: L198-L215
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D342` — EM Coulomb Contribution to p-n splitting
- `IV.T141` — Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]

## Immediate Comment / Docstring

```lean
/-- [IV.D342] EM contribution is in range (1.26, 1.29) × 10⁻⁴.
    Python lab: (3/20)·α·ι_τ² ≈ 1.27510 × 10⁻⁴
    Proof: #eval confirms em_float ≈ 1.275e-4 ∈ (1.26e-4, 1.29e-4). -/
```

## Source Excerpt

```lean
theorem em_in_range :
    em_numer * 10000000 > 1260 * em_denom ∧
    em_numer * 10000000 < 1290 * em_denom := by
  rw [em_numer_val, em_denom_val]
  constructor <;> native_decide

-- ============================================================
-- TREE-LEVEL FORMULA [IV.T141]
-- ============================================================

/-! [IV.T141] Tree-level: δm/m_n = (√3/2) · ι_τ⁶

    Cross-multiplied form:
      numer = sqrt3_numer · iota⁶
      denom = 2 · sqrt3_denom · iotaD⁶

    Python lab: −5516 ppm (conjectural scope)
-/
```
