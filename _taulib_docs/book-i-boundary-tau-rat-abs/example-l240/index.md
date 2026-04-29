---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L240",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/example-l240/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.TauRatAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatAbs::#eval:240",
  "declaration_slug": "example-l240",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.TauRatAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-abs/",
  "source_line_start": 240,
  "source_line_end": 245,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L240-L245",
  "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L240-L245",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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
- Source path: [`TauLib/BookI/Boundary/TauRatAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatAbs.lean#L240-L245)
- Source range: L240-L245
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- abs of a negative TauRat flips the sign
```

## Source Excerpt

```lean
example :
    (⟨⟨0, 3⟩, 5, by norm_num⟩ : TauRat).abs.toRat =
      -(⟨⟨0, 3⟩, 5, by norm_num⟩ : TauRat).toRat := by
  apply toRat_abs_of_neg
  simp [TauRat.toRat, TauInt.toInt]
  norm_num
```
