---
{
  "projection_kind": "taulib_declaration",
  "title": "TauComplex",
  "permalink": "/corpus/taulib/docs/book-i-boundary-complex-field/tau-complex/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Boundary.ComplexField`.",
  "declaration_id": "TauLib.BookI.Boundary.ComplexField::TauComplex",
  "declaration_slug": "tau-complex",
  "kind": "structure",
  "name": "TauComplex",
  "module_name": "TauLib.BookI.Boundary.ComplexField",
  "module_url": "/corpus/taulib/docs/book-i-boundary-complex-field/",
  "source_line_start": 46,
  "source_line_end": 50,
  "registry_ids": [
    "I.D85"
  ],
  "related_registry_items": [
    {
      "id": "I.D85",
      "title": "Elliptic Complex Field",
      "url": "/registry/object/I.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L46-L50",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L46-L50",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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
- Source path: [`TauLib/BookI/Boundary/ComplexField.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/ComplexField.lean#L46-L50)
- Source range: L46-L50
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `I.D85` — Elliptic Complex Field

## Immediate Comment / Docstring

```lean
/-- [I.D85] TauComplex: the elliptic complex field TauReal[i]/(i² + 1).
    A pair (re, im) represents re + im * i. -/
```

## Source Excerpt

```lean
structure TauComplex where
  /-- Real part. -/
  re : TauReal
  /-- Imaginary part. -/
  im : TauReal
```
