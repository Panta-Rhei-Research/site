---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L98",
  "permalink": "/verify/taulib/docs/tour-guided-tour-book-iv/eval-l98/",
  "summary_short": "`eval` declaration in `TauLib.Tour.GuidedTour.BookIV`.",
  "declaration_id": "TauLib.Tour.GuidedTour.BookIV::#eval:98",
  "declaration_slug": "eval-l98",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.GuidedTour.BookIV",
  "module_url": "/verify/taulib/docs/tour-guided-tour-book-iv/",
  "source_line_start": 98,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookIV.lean#L98-L128",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.GuidedTour.BookIV",
        "url": "/verify/taulib/docs/tour-guided-tour-book-iv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookIV.lean#L98-L128",
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

- Module: [TauLib.Tour.GuidedTour.BookIV](/verify/taulib/docs/tour-guided-tour-book-iv/)
- Source path: [`TauLib/Tour/GuidedTour/BookIV.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookIV.lean#L98-L128)
- Source range: L98-L128
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
#eval zero_vs_nineteen.sm_params    -- 19


-- ================================================================
-- HINGE 5: Electron Mass Prediction
-- ================================================================

/-
R₀ = ι_τ⁻⁷ − √3 · ι_τ⁻² ≈ 1838.7
CODATA: m_n/m_e = 1838.684...
Agreement: 7.7 ppm (leading), 0.025 ppm (with holonomy).
-/

#check si_electron_mass


-- ================================================================
-- HINGE 6: Three Generations [IV.T10–T11]
-- ================================================================

/-
The Lean formalization of `exactly_three_generations` proves
`π₁(τ³) ≅ ℤ³`, which implies a 3-winding-class decomposition.
The identification of these three winding classes with the three
fermion generations (electron/muon/tau families) is monograph-level:
it is defended in Book IV (IV.T10–T11) but is not itself a Lean theorem.
The `τ-effective` content here is the topological count of three; the
physical labeling is separate.
-/

#check exactly_three_generations
```
