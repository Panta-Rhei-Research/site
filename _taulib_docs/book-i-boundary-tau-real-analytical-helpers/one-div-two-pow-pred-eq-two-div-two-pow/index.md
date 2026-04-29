---
{
  "projection_kind": "taulib_declaration",
  "title": "Rat.one_div_two_pow_pred_eq_two_div_two_pow",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/one-div-two-pow-pred-eq-two-div-two-pow/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers::Rat.one_div_two_pow_pred_eq_two_div_two_pow",
  "declaration_slug": "one-div-two-pow-pred-eq-two-div-two-pow",
  "kind": "theorem",
  "name": "Rat.one_div_two_pow_pred_eq_two_div_two_pow",
  "module_name": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/",
  "source_line_start": 121,
  "source_line_end": 125,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L121-L125",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L121-L125",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L121-L125)
- Source range: L121-L125
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `1/2^(m-1) = 2/2^m` for `m ≥ 1`. -/
```

## Source Excerpt

```lean
theorem Rat.one_div_two_pow_pred_eq_two_div_two_pow (m : Nat) (hm : 1 ≤ m) :
    (1 : Rat) / (2 : Rat) ^ (m - 1) = 2 / (2 : Rat) ^ m := by
  rw [Rat.pow_pred_eq m hm]
  have h_pos : (0 : Rat) < (2 : Rat) ^ (m - 1) := by positivity
  field_simp
```
