---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L85",
  "permalink": "/verify/taulib/docs/tour-physics/eval-l85/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Physics`.",
  "declaration_id": "TauLib.Tour.Physics::#eval:85",
  "declaration_slug": "eval-l85",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Physics",
  "module_url": "/verify/taulib/docs/tour-physics/",
  "source_line_start": 85,
  "source_line_end": 109,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L85-L109",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L85-L109",
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
- Source path: [`TauLib/Tour/Physics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L85-L109)
- Source range: L85-L109
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
#eval koide_relation.predicted_denom -- 3

-- ================================================================
-- PART 3: MAJORANA NEUTRINOS (Book IV, σ = C_τ sprint)
-- ================================================================

-- The polarity involution σ on L = S¹ ∨ S¹ IS charge conjugation.
-- This is not assumed — it is proved from the bipolar decomposition
-- uniqueness (I.D18). The four-step chain:
--   1. σ uniquely swaps χ₊ ↔ χ₋   (I.D18)
--   2. Any charge conjugation C must do the same
--   3. Therefore C_τ = σ
--   4. Zero-U(1)-holonomy modes are σ-eigenstates → Majorana

#check c_tau_equals_sigma           -- True (definitional identification)
-- NOTE: c_tau_equals_sigma is currently a `theorem X : True := trivial`
-- structural marker (analogous to the retired Book VII pattern noted in Part 8).
-- The full derivation lives in Book IV ch. X (MajoranaStructure). A future PR
-- (peer-review-fixes-v2 or later) will re-encode this as either a full proof
-- or a `Commitment`-style inspectable def. Acknowledged pending technical debt;
-- the physical claim (σ = C_τ) is load-bearing at monograph level.
#check sigma_is_charge_conjugation  -- ∀ z, chi_plus(σz) = chi_minus(z) ∧ ...

-- All three neutrinos have zero U(1)-holonomy charge:
#check all_neutrinos_majorana       -- nu_e.charge = 0 ∧ nu_mu.charge = 0 ∧ nu_tau.charge = 0
```
