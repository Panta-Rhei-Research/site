---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L77",
  "permalink": "/verify/taulib/docs/tour-guided-tour-book-v/eval-l77/",
  "summary_short": "`eval` declaration in `TauLib.Tour.GuidedTour.BookV`.",
  "declaration_id": "TauLib.Tour.GuidedTour.BookV::#eval:77",
  "declaration_slug": "eval-l77",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.GuidedTour.BookV",
  "module_url": "/verify/taulib/docs/tour-guided-tour-book-v/",
  "source_line_start": 77,
  "source_line_end": 117,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L77-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L77-L117",
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
- Source path: [`TauLib/Tour/GuidedTour/BookV.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L77-L117)
- Source range: L77-L117
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval e1_complete.single_anchor       -- true


-- ================================================================
-- HINGE 4: Flat Rotation Curves Without Dark Matter
-- ================================================================

/-
`τ-effective`: the boundary holonomy correction κ(D;1) = 1 - ι_τ ≈ 0.659
produces flat rotation curve profiles numerically consistent with
galactic observations. `flat_rotation_theorem`, `no_dark_halo`, and
`rar_from_single_coupling` are typed structures recording these
data-consistency checks; `mond_scale_from_iota` records the derivation
of the MOND acceleration scale from ι_τ.

`monograph-level`: the claim that dark matter halos are absent in real
galaxies and that this formula is the correct physical explanation is
defended in Book V. It is not a consequence provable from the Lean
structures alone.
-/

#check flat_rotation_theorem
#check mond_scale_from_iota
#check no_dark_halo
#check rar_from_single_coupling


-- ================================================================
-- HINGE 5: CMB Pipeline — All Observables from One Constant
-- ================================================================

/-
The decisive predictions:
  r = ι_τ⁴ ≈ 0.0136      (tensor-to-scalar, pre-registered for CMB-S4)
  n_s = 1 - 2/57 = 0.9649  (spectral index)
  ℓ₁ = 220.6               (first acoustic peak)
  ω_b = 0.02209             (baryon density)
-/

-- First acoustic peak
#check first_peak_holonomy_thm
```
