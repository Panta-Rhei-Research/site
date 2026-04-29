---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L112",
  "permalink": "/verify/taulib/docs/tour-physics/eval-l112/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Physics`.",
  "declaration_id": "TauLib.Tour.Physics::#eval:112",
  "declaration_slug": "eval-l112",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Physics",
  "module_url": "/verify/taulib/docs/tour-physics/",
  "source_line_start": 112,
  "source_line_end": 135,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L112-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L112-L135",
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
- Source path: [`TauLib/Tour/Physics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L112-L135)
- Source range: L112-L135
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
#eval nu_tau.charge                 -- 0

-- Consequence: neutrinoless double beta decay (0νββ) must exist.
-- Within LEGEND-1000 reach (~10 meV sensitivity).

-- ================================================================
-- PART 4: STRONG CP RESOLUTION (Book IV, Chapter 31)
-- ================================================================

-- The Strong CP problem: why is θ_QCD ≈ 0? The SM has no explanation.
-- In Category τ, the SA-i condition (η-winding mod 3) forbids
-- instantons outright:
--   Instanton: Δ(η-winding) = +1, but 1 mod 3 ≠ 0 → forbidden
--   Anti-instanton: Δ(η-winding) = -1, but -1 mod 3 ≠ 0 → forbidden
-- Therefore Q_top = 0 and θ_QCD = 0 exactly.

#check theta_qcd_zero_from_sa_i    -- True (structural θ_QCD = 0)
-- NOTE: theta_qcd_zero_from_sa_i is currently a `theorem X : True := trivial`
-- structural marker (analogous to the retired Book VII pattern noted in Part 8).
-- The full derivation lives in Book IV ch. X (StrongCP). A future PR
-- (peer-review-fixes-v2 or later) will re-encode this as either a full proof
-- or a `Commitment`-style inspectable def. Acknowledged pending technical debt;
-- the physical claim (θ_QCD = 0 from SA-i) is load-bearing at monograph level.
#check sa_i_forbids_instantons     -- 1 % 3 ≠ 0 ∧ (-1) % 3 ≠ 0
```
