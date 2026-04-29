---
{
  "projection_kind": "taulib_declaration",
  "title": "qcd_in_range",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/qcd-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::qcd_in_range",
  "declaration_slug": "qcd-in-range",
  "kind": "theorem",
  "name": "qcd_in_range",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 150,
  "source_line_end": 172,
  "registry_ids": [
    "IV.D341",
    "IV.D342"
  ],
  "related_registry_items": [
    {
      "id": "IV.D341",
      "title": "QCD Contribution to p-n splitting",
      "url": "/registry/object/IV.D341/"
    },
    {
      "id": "IV.D342",
      "title": "EM Coulomb Contribution to p-n splitting",
      "url": "/registry/object/IV.D342/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L150-L172",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L150-L172",
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L150-L172)
- Source range: L150-L172
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D341` — QCD Contribution to p-n splitting
- `IV.D342` — EM Coulomb Contribution to p-n splitting

## Immediate Comment / Docstring

```lean
/-- [IV.D341] QCD contribution is in range (1.49, 1.51) × 10⁻³.
    Python lab: (3/16)·√3·ι_τ⁵ ≈ 1.50408 × 10⁻³
    Proof: (3/16)·√3·ι_τ⁵ ≈ 1.504e-3 confirmed by #eval above. -/
```

## Source Excerpt

```lean
theorem qcd_in_range :
    qcd_numer * 1000000 > 1490 * qcd_denom ∧
    qcd_numer * 1000000 < 1510 * qcd_denom := by
  rw [qcd_numer_val, qcd_denom_val]
  constructor <;> native_decide

-- ============================================================
-- EM COULOMB CONTRIBUTION [IV.D342]
-- ============================================================

/-! [IV.D342] EM Contribution = (3/20) · α · ι_τ²

    α = (121/225)·ι_τ⁴, so:
    (3/20) · α · ι_τ² = (3 · 121 / (20 · 225)) · ι_τ⁶
                       = (363/4500) · ι_τ⁶

    Cross-multiplied form:
      numer = 363 · iota⁶ = 3 · 121 · iota⁶
      denom = 4500 · iotaD⁶ = 20 · 225 · iotaD⁶

    Python lab confirms: ≈ 1.27510 × 10⁻⁴ in units of m_n
                          ≈ 0.120 MeV
-/
```
