---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.abs_triangle",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/abs-triangle/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatAbs::TauRat.abs_triangle",
  "declaration_slug": "abs-triangle",
  "kind": "theorem",
  "name": "TauRat.abs_triangle",
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/",
  "source_line_start": 179,
  "source_line_end": 182,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L179-L182",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L179-L182",
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
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L179-L182)
- Source range: L179-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Triangle inequality for `TauRat.abs` at the `toRat` level:
    `(a + b).abs.toRat ≤ a.abs.toRat + b.abs.toRat`.

    Proved by lifting all three abs values through `toRat_abs` to Lean's
    `|·|` on `Rat`, then applying mathlib's `abs_add`. -/
```

## Source Excerpt

```lean
theorem TauRat.abs_triangle (a b : TauRat) :
    (a.add b).abs.toRat ≤ a.abs.toRat + b.abs.toRat := by
  rw [TauRat.toRat_abs, TauRat.toRat_abs, TauRat.toRat_abs, toRat_add]
  exact abs_add_le _ _
```
