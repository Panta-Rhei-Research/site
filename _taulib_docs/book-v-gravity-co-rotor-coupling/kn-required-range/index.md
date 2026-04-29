---
{
  "projection_kind": "taulib_declaration",
  "title": "kn_required_range",
  "permalink": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/kn-required-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.CoRotorCoupling`.",
  "declaration_id": "TauLib.BookV.Gravity.CoRotorCoupling::kn_required_range",
  "declaration_slug": "kn-required-range",
  "kind": "theorem",
  "name": "kn_required_range",
  "module_name": "TauLib.BookV.Gravity.CoRotorCoupling",
  "module_url": "/verify/taulib/docs/book-v-gravity-co-rotor-coupling/",
  "source_line_start": 143,
  "source_line_end": 146,
  "registry_ids": [
    "V.T04"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L143-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L143-L146",
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
- Source path: [`TauLib/BookV/Gravity/CoRotorCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/CoRotorCoupling.lean#L143-L146)
- Source range: L143-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T04] κ_n is in the range (3.439, 3.441).

    This range is established by CODATA arithmetic:
    κ_n = 2 · G · m_n² / (α¹⁸ · ℏc) is fixed by measured constants.

    34399 × 10000 < 10000 × 34399723 < 34410 × 10000. -/
```

## Source Excerpt

```lean
theorem kn_required_range :
    3439 * kn_required_denom < 1000 * kn_required_numer ∧
    1000 * kn_required_numer < 3441 * kn_required_denom := by
  simp [kn_required_numer, kn_required_denom]
```
