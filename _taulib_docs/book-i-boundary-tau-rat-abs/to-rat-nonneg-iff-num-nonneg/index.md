---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.toRat_nonneg_iff_num_nonneg",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/to-rat-nonneg-iff-num-nonneg/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatAbs::TauRat.toRat_nonneg_iff_num_nonneg",
  "declaration_slug": "to-rat-nonneg-iff-num-nonneg",
  "kind": "theorem",
  "name": "TauRat.toRat_nonneg_iff_num_nonneg",
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/",
  "source_line_start": 72,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L72-L84",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatAbs",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L72-L84",
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

- Module: [TauLib.BookI.Boundary.TauRatAbs](/verify/taulib/docs/book-i-boundary-tau-rat-abs/)
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L72-L84)
- Source range: L72-L84
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `q.toRat ≥ 0` iff `q.num.toInt ≥ 0`.  The denominator is positive,
    so the sign of `q.toRat = q.num.toInt / q.den` is controlled
    entirely by the numerator. -/
```

## Source Excerpt

```lean
theorem TauRat.toRat_nonneg_iff_num_nonneg (q : TauRat) :
    0 ≤ q.toRat ↔ 0 ≤ q.num.toInt := by
  unfold TauRat.toRat
  have hp : (0 : Rat) < (q.den : Rat) := q.den_pos_rat
  constructor
  · intro h
    have h_rat : (0 : Rat) ≤ (q.num.toInt : Rat) := by
      have hmul := mul_nonneg h (_root_.le_of_lt hp)
      rwa [div_mul_cancel₀ _ (ne_of_gt hp)] at hmul
    exact_mod_cast h_rat
  · intro h
    have h_rat : (0 : Rat) ≤ (q.num.toInt : Rat) := by exact_mod_cast h
    exact div_nonneg h_rat (_root_.le_of_lt hp)
```
