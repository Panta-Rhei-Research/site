---
{
  "projection_kind": "taulib_declaration",
  "title": "TauComplex.equiv_refl",
  "permalink": "/corpus/taulib/docs/book-i-boundary-complex-field/equiv-refl/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::TauComplex.equiv_refl",
  "declaration_slug": "equiv-refl",
  "kind": "theorem",
  "name": "TauComplex.equiv_refl",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 62,
  "source_line_end": 63,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L62-L63",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.ComplexField",
        "url": "/corpus/taulib/docs/book-i-boundary-complex-field/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L62-L63",
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

- Module: [TauLib.BookI.Boundary.ComplexField](/corpus/taulib/docs/book-i-boundary-complex-field/)
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L62-L63)
- Source range: L62-L63
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- TauComplex equivalence is reflexive. -/
```

## Source Excerpt

```lean
theorem TauComplex.equiv_refl (a : TauComplex) : TauComplex.equiv a a :=
  ⟨TauReal.equiv_refl a.re, TauReal.equiv_refl a.im⟩
```
