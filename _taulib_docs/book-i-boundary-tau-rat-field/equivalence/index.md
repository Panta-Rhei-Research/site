---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.equivalence",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/equivalence/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatField`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatField::TauRat.equivalence",
  "declaration_slug": "equivalence",
  "kind": "theorem",
  "name": "TauRat.equivalence",
  "module_name": "TauLib.BookI.Boundary.TauRatField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-field/",
  "source_line_start": 79,
  "source_line_end": 80,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L79-L80",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L79-L80",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookI/Boundary/TauRatField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatField.lean#L79-L80)
- Source range: L79-L80
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauRat.equiv as a fully-fledged equivalence relation. -/
```

## Source Excerpt

```lean
theorem TauRat.equivalence : Equivalence TauRat.equiv :=
  ⟨TauRat.equiv_refl, TauRat.equiv_symm, TauRat.equiv_trans⟩
```
