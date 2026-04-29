---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L140",
  "permalink": "/verify/taulib/docs/tour-guided-tour-book-v/eval-l140/",
  "summary_short": "`eval` declaration in `TauLib.Tour.GuidedTour.BookV`.",
  "declaration_id": "TauLib.Tour.GuidedTour.BookV::#eval:140",
  "declaration_slug": "eval-l140",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.GuidedTour.BookV",
  "module_url": "/verify/taulib/docs/tour-guided-tour-book-v/",
  "source_line_start": 140,
  "source_line_end": 202,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L140-L202",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.GuidedTour.BookV",
        "url": "/verify/taulib/docs/tour-guided-tour-book-v/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L140-L202",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.Tour.GuidedTour.BookV](/verify/taulib/docs/tour-guided-tour-book-v/)
- Source path: [`TauLib/Tour/GuidedTour/BookV.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L140-L202)
- Source range: L140-L202
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- The first peak data: free parameters = 0
```

## Source Excerpt

```lean
#eval first_peak_data.free_params  -- 0


-- ================================================================
-- HINGE 7: No Dark Energy — Lambda = 0
-- ================================================================

/-
`τ-effective`: `dark_energy_artifact` is a typed structure recording the
monograph's claim that Λ = 0 and that apparent cosmic acceleration is a
readout artifact of the τ-framework's thermodynamic inversion (entropy
decreasing along proto-time). The structure compiles and its arithmetic
is self-consistent.

`monograph-level`: whether Λ = 0 in physical reality and whether apparent
acceleration is an artifact are claims defended in Book V. They are
pre-registered as falsifiable predictions; their correctness cannot be
established by a Lean type-check.
-/

#check dark_energy_artifact


-- ================================================================
-- HINGE 8: Black Holes as Topological Objects
-- ================================================================

/-
`τ-effective`: `bh_toroidal_topology` records the τ-framework's structural
claim that black hole horizons are T² (torus) and computes the QNM
frequency ratio ι_τ⁻¹ ≈ 2.930. The arithmetic is self-consistent.

`monograph-level`: that real astrophysical black holes have toroidal
horizons (not S²), lack interior singularities, and do not emit Hawking
radiation are forward-falsifier predictions defended in Book V. Lean
type-checking the record does not establish their physical truth.
-/

#check bh_toroidal_topology


-- ================================================================
-- VERIFICATION SUMMARY
-- ================================================================

/-
All 8 hinges of Book V are machine-checked:

  H1: constants_ledger (sector exhaustion)              ✓
  H2: τ-Einstein (gravitational sector)                 ✓
  H3: e1_complete (forces + constants + anchor)          ✓
  H4: flat_rotation_theorem, no_dark_halo                ✓
  H5: first_peak_holonomy (220.63), tensor_scalar_ratio  ✓
  H6: first_peak_data.free_params = 0                    ✓
  H7: dark_energy_artifact                               ✓
  H8: bh_toroidal_topology                               ✓

Zero sorry. Every prediction formula compiles and is data-consistent at
`a2d3384`. The `τ-effective` arithmetic layer is machine-checked. The
physical interpretations (no dark matter, Λ = 0, toroidal horizons) are
monograph-level forward falsifiers defended in Book V — not consequences
derivable from Lean alone.
-/
```
