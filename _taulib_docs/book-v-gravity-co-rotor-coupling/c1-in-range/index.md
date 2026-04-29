---
{
  "projection_kind": "taulib_declaration",
  "title": "c1_in_range",
  "permalink": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/c1-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.CoRotorCoupling`.",
  "declaration_id": "TauLib.BookV.Gravity.CoRotorCoupling::c1_in_range",
  "declaration_slug": "c1-in-range",
  "kind": "theorem",
  "name": "c1_in_range",
  "module_name": "TauLib.BookV.Gravity.CoRotorCoupling",
  "module_url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/",
  "source_line_start": 191,
  "source_line_end": 194,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L191-L194",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L191-L194",
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
- Source path: [`TauLib/BookV/Gravity/CoRotorCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L191-L194)
- Source range: L191-L194
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- c₁ = 3/π is in range (0.954, 0.956). -/
```

## Source Excerpt

```lean
theorem c1_in_range :
    954 * c1_three_over_pi_denom < 1000 * c1_three_over_pi_numer ∧
    1000 * c1_three_over_pi_numer < 956 * c1_three_over_pi_denom := by
  simp [c1_three_over_pi_numer, c1_three_over_pi_denom]
```
