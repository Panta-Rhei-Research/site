---
{
  "projection_kind": "taulib_declaration",
  "title": "nucleon_modes_distinct",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-modes-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::nucleon_modes_distinct",
  "declaration_slug": "nucleon-modes-distinct",
  "kind": "theorem",
  "name": "nucleon_modes_distinct",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 71,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L71-L89",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L71-L89",
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
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L71-L89)
- Source range: L71-L89
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The two nucleon modes are distinct. -/
```

## Source Excerpt

```lean
theorem nucleon_modes_distinct : NucleonMode.Proton ≠ NucleonMode.Neutron := by
  decide

-- ============================================================
-- RATIONAL APPROXIMATION CONSTANTS
-- ============================================================

/-! We work in the same Nat-rational framework as LemniscateCapacity.lean
    and MassRatioFormula.lean.

    ι_τ ≈ 341304/1000000  (iota / iotaD from SectorParameters)

    ι_τ⁵: numer = 341304⁵ = iota⁵, denom = 1000000⁵ = iotaD⁵
    ι_τ²: numer = 341304² = iota², denom = 1000000² = iotaD²

    √3 ≈ 17320508/10000000  (from LemniscateCapacity.lean: sqrt3_numer/sqrt3_denom)

    α = (121/225)·ι_τ⁴: numer = 121·iota⁴, denom = 225·iotaD⁴
-/
```
