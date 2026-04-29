---
{
  "projection_kind": "taulib_declaration",
  "title": "Rat.four_div_two_pow_succ_eq_two_div_two_pow",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/four-div-two-pow-succ-eq-two-div-two-pow/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRealAnalyticalHelpers`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers::Rat.four_div_two_pow_succ_eq_two_div_two_pow",
  "declaration_slug": "four-div-two-pow-succ-eq-two-div-two-pow",
  "kind": "theorem",
  "name": "Rat.four_div_two_pow_succ_eq_two_div_two_pow",
  "module_name": "TauLib.BookI.Boundary.TauRealAnalyticalHelpers",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-analytical-helpers/",
  "source_line_start": 111,
  "source_line_end": 118,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L111-L118",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L111-L118",
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
- Source path: [`TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAnalyticalHelpers.lean#L111-L118)
- Source range: L111-L118
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `4/2^(m+1) = 2/2^m` — a common reshuffle in telescoping geometric bounds. -/
```

## Source Excerpt

```lean
theorem Rat.four_div_two_pow_succ_eq_two_div_two_pow (m : Nat) :
    (4 : Rat) / (2 : Rat) ^ (m + 1) = 2 / (2 : Rat) ^ m := by
  have h_pow : (2 : Rat) ^ (m + 1) = 2 * 2 ^ m := by ring
  rw [h_pow]
  have h_pos : (0 : Rat) < 2 ^ m := by positivity
  have h_ne : (2 : Rat) ^ m ≠ 0 := ne_of_gt h_pos
  field_simp
  ring
```
