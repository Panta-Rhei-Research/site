---
{
  "projection_kind": "taulib_declaration",
  "title": "iota6_denom_pos",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/iota6-denom-pos/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::iota6_denom_pos",
  "declaration_slug": "iota6-denom-pos",
  "kind": "theorem",
  "name": "iota6_denom_pos",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 110,
  "source_line_end": 124,
  "registry_ids": [
    "IV.D341"
  ],
  "related_registry_items": [
    {
      "id": "IV.D341",
      "title": "QCD Contribution to p-n splitting",
      "url": "/registry/object/IV.D341/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L110-L124",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L110-L124",
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L110-L124)
- Source range: L110-L124
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D341` — QCD Contribution to p-n splitting

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem iota6_denom_pos : iota6_denom > 0 := by simp [iota6_denom, iotaD, iota_tau_denom]

-- ============================================================
-- QCD CONTRIBUTION [IV.D341]
-- ============================================================

/-! [IV.D341] QCD Contribution = (3/16) · √3 · ι_τ⁵

    Cross-multiplied form for Nat arithmetic:
      numer = 3 · sqrt3_numer · iota⁵
      denom = 16 · sqrt3_denom · iotaD⁵

    Python lab confirms: ≈ 1.50408 × 10⁻³ in units of m_n
                          ≈ 1.413 MeV (with m_n = 939.565 MeV)
-/
```
