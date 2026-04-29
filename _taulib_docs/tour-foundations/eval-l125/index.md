---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L125",
  "permalink": "/verify/taulib/docs/tour-foundations/eval-l125/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Foundations`.",
  "declaration_id": "TauLib.Tour.Foundations::#eval:125",
  "declaration_slug": "eval-l125",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Foundations",
  "module_url": "/verify/taulib/docs/tour-foundations/",
  "source_line_start": 125,
  "source_line_end": 144,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Foundations.lean#L125-L144",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.Foundations",
        "url": "/verify/taulib/docs/tour-foundations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Foundations.lean#L125-L144",
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

- Module: [TauLib.Tour.Foundations](/verify/taulib/docs/tour-foundations/)
- Source path: [`TauLib/Tour/Foundations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Foundations.lean#L125-L144)
- Source range: L125-L144
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
#eval iota_tau_denom       -- 1000000 (denominator)

-- κ_D = 1 − ι_τ ≈ 0.658696 (the complementary constant)
-- κ_ω = ι_τ/(1 + ι_τ) ≈ 0.254485

-- These two constants, together with ι_τ, govern all quantitative
-- predictions across physics (Books IV–V).

-- ================================================================
-- PART 6: RIGIDITY — Aut(τ) = {id}
-- ================================================================

-- The most striking structural theorem in Book I:
-- Category τ admits NO non-trivial automorphisms.
-- Any structure-preserving map must be the identity.

-- This means τ is *categorically unique* — there is exactly one
-- model satisfying the axioms, up to isomorphism.

#check @rigidity_non_omega
```
