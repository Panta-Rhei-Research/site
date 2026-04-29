---
{
  "projection_kind": "taulib_declaration",
  "title": "c1_matches_three_over_pi",
  "permalink": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/c1-matches-three-over-pi/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.CoRotorCoupling`.",
  "declaration_id": "TauLib.BookV.Gravity.CoRotorCoupling::c1_matches_three_over_pi",
  "declaration_slug": "c1-matches-three-over-pi",
  "kind": "theorem",
  "name": "c1_matches_three_over_pi",
  "module_name": "TauLib.BookV.Gravity.CoRotorCoupling",
  "module_url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/",
  "source_line_start": 185,
  "source_line_end": 188,
  "registry_ids": [
    "V.T05"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L185-L188",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.CoRotorCoupling",
        "url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L185-L188",
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

- Module: [TauLib.BookV.Gravity.CoRotorCoupling](/verify/taulib/docs/book-v-gravity-co-rotor-coupling/)
- Source path: [`TauLib/BookV/Gravity/CoRotorCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L185-L188)
- Source range: L185-L188
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T05] c₁ = 3/π matches the target to better than 0.05%.

    |c₁(3/π) - c₁(target)| < 5000/10000000 = 0.0005

    Verified: |9549297 - 9545279| = 4018 < 5000.
    Relative error: 4018/9545279 ≈ 0.042% < 0.05%. -/
```

## Source Excerpt

```lean
theorem c1_matches_three_over_pi :
    c1_three_over_pi_numer < c1_target_numer + 5000 ∧
    c1_target_numer < c1_three_over_pi_numer + 5000 := by
  simp [c1_three_over_pi_numer, c1_target_numer]
```
