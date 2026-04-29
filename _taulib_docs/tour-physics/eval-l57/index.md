---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L57",
  "permalink": "/verify/taulib/docs/tour-physics/eval-l57/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Physics`.",
  "declaration_id": "TauLib.Tour.Physics::#eval:57",
  "declaration_slug": "eval-l57",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Physics",
  "module_url": "/verify/taulib/docs/tour-physics/",
  "source_line_start": 57,
  "source_line_end": 74,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L57-L74",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.Physics",
        "url": "/verify/taulib/docs/tour-physics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L57-L74",
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

- Module: [TauLib.Tour.Physics](/verify/taulib/docs/tour-physics/)
- Source path: [`TauLib/Tour/Physics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L57-L74)
- Source range: L57-L74
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
#eval zero_vs_nineteen.sm_params   -- 19

-- Every prediction traces to ι_τ + K0-K6:
#check ew_two_inputs               -- ew_traces_to_axioms.input_count = 2

-- ================================================================
-- PART 2: THREE GENERATIONS (Book IV, Chapter 46)
-- ================================================================

-- Why exactly three fermion families? The lemniscate L = S¹ ∨ S¹
-- has exactly three structurally distinct regions:
--   1. Crossing point → Generation 1 (electron, u/d quarks)
--   2. Single lobe    → Generation 2 (muon, c/s quarks)
--   3. Full figure    → Generation 3 (tau lepton, t/b quarks)
-- This is topological — no fourth class exists at any energy.

#check LemniscateModeClass          -- inductive: crossingPoint | singleLobe | fullLemniscate
#check three_mode_classes_count     -- three_mode_classes.length = 3
```
