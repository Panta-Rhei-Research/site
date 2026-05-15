---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L215",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/example-l215/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::#eval:215",
  "declaration_slug": "example-l215",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 215,
  "source_line_end": 216,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L215-L216",
  "formal_status": "example",
  "declaration_role": "example check",
  "formal_status_label": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatField",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L215-L216",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "role": "example check",
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

- Module: [TauLib.BookI.Boundary.TauRatField](/corpus/taulib/docs/book-i-boundary-tau-rat-field/)
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L215-L216)
- Source range: L215-L216
- Kind: `example`
- Public role: `example check`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- PART 5: SMOKE TESTS
-- ============================================================

-- toRat semantic bridge sanity
```

## Source Excerpt

```lean
example : (⟨⟨1, 0⟩, 2, by norm_num⟩ : TauRat).toRat = 1/2 := by
  simp [TauRat.toRat, TauInt.toInt]
```
