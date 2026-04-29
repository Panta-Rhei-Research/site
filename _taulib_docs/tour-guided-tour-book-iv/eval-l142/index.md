---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L142",
  "permalink": "/verify/taulib/docs/tour-guided-tour-book-iv/eval-l142/",
  "summary_short": "`eval` declaration in `TauLib.Tour.GuidedTour.BookIV`.",
  "declaration_id": "TauLib.Tour.GuidedTour.BookIV::#eval:142",
  "declaration_slug": "eval-l142",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.GuidedTour.BookIV",
  "module_url": "/verify/taulib/docs/tour-guided-tour-book-iv/",
  "source_line_start": 142,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookIV.lean#L142-L164",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookIV.lean#L142-L164",
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
- Source path: [`TauLib/Tour/GuidedTour/BookIV.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookIV.lean#L142-L164)
- Source range: L142-L164
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- 9 electroweak predictions, 0 free parameters
```

## Source Excerpt

```lean
#eval ew_prediction_table.length  -- 9


-- ================================================================
-- VERIFICATION SUMMARY
-- ================================================================

/-
All 7 hinges of Book IV are machine-checked:

  H1: NeutronParent, neutron_as_parent                ✓ (Primacy)
  H2: BetaDecayQValue, beta_decay_q_value             ✓ (Rosetta)
  H3: CalibrationAnchor, calibration_map               ✓ (Anchor)
  H4: alpha_tau, zero_vs_nineteen (0 vs 19 params)     ✓ (Alpha)
  H5: si_electron_mass                                 ✓ (Mass ratio)
  H6: exactly_three_generations (count = 3)             ✓ (Topology)
  H7: ew_prediction_table (9 predictions, 0 params)    ✓ (Completion)

Zero sorry. Zero free parameters. The arithmetic and structural identities
compile. Physical identification with SM predictions is monograph-level
and is defended in Book IV; the Lean content is the arithmetic and
data-consistency layer.
-/
```
