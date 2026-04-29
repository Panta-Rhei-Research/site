---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.abs_negate",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/abs-negate/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatAbs::TauRat.abs_negate",
  "declaration_slug": "abs-negate",
  "kind": "theorem",
  "name": "TauRat.abs_negate",
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/",
  "source_line_start": 185,
  "source_line_end": 197,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L185-L197",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L185-L197",
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
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L185-L197)
- Source range: L185-L197
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Negation-invariance of `abs` at the toRat level: `a.negate.abs.toRat = a.abs.toRat`. -/
```

## Source Excerpt

```lean
theorem TauRat.abs_negate (a : TauRat) :
    a.negate.abs.toRat = a.abs.toRat := by
  by_cases ha : 0 ≤ a.toRat
  · rw [toRat_abs_of_nonneg ha]
    by_cases hneg : 0 ≤ a.negate.toRat
    · rw [toRat_abs_of_nonneg hneg, toRat_negate]
      rw [toRat_negate] at hneg; linarith
    · push_neg at hneg
      rw [toRat_abs_of_neg hneg, toRat_negate]; ring
  · push_neg at ha
    rw [toRat_abs_of_neg ha]
    have hneg : 0 ≤ a.negate.toRat := by rw [toRat_negate]; linarith
    rw [toRat_abs_of_nonneg hneg, toRat_negate]
```
