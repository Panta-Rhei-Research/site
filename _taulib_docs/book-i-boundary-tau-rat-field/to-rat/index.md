---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.toRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-field/to-rat/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::TauRat.toRat",
  "declaration_slug": "to-rat",
  "kind": "def",
  "name": "TauRat.toRat",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 89,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L89-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatField",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L89-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Boundary.TauRatField](/verify/taulib/docs/book-i-boundary-tau-rat-field/)
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L89-L90)
- Source range: L89-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Semantic bridge from TauRat to Lean's built-in `Rat`.  Computes the
    rational number represented by a TauRat structure.  Parallels
    `TauInt.toInt`. -/
```

## Source Excerpt

```lean
def TauRat.toRat (q : TauRat) : Rat :=
  (q.num.toInt : Rat) / (q.den : Rat)
```
