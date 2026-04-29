---
{
  "projection_kind": "taulib_declaration",
  "title": "Rat.pow_pred_eq",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/pow-pred-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers::Rat.pow_pred_eq",
  "declaration_slug": "pow-pred-eq",
  "kind": "theorem",
  "name": "Rat.pow_pred_eq",
  "module_name": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/",
  "source_line_start": 104,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L104-L108",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L104-L108",
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

- Module: [TauLib.BookI.Boundary.TauRealAnalyticalHelpers](/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/)
- Source path: [`TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L104-L108)
- Source range: L104-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `(2 : Rat)^m = 2 * 2^(m-1)` for `m ≥ 1`.  Packaged so downstream
    proofs don't need to redo the `m = (m-1)+1 + pow_succ + ring` dance. -/
```

## Source Excerpt

```lean
theorem Rat.pow_pred_eq (m : Nat) (hm : 1 ≤ m) :
    (2 : Rat) ^ m = 2 * (2 : Rat) ^ (m - 1) := by
  have h : m = (m - 1) + 1 := by omega
  conv_lhs => rw [h]
  rw [pow_succ]; ring
```
