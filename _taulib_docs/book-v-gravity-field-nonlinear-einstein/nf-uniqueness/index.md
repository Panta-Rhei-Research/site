---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_uniqueness",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::nf_uniqueness",
  "declaration_slug": "nf-uniqueness",
  "kind": "theorem",
  "name": "nf_uniqueness",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 302,
  "source_line_end": 305,
  "registry_ids": [
    "V.T34"
  ],
  "related_registry_items": [
    {
      "id": "V.T34",
      "title": "Uniqueness",
      "url": "/registry/object/V.T34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L302-L305",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L302-L305",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L302-L305)
- Source range: L302-L305
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T34` — Uniqueness

## Immediate Comment / Docstring

```lean
/-- [V.T34] Uniqueness: if two NF iterations converge, they converge
    to the same fixed point (zero defect).

    Encoded: if converged, defect numerator = 0. -/
```

## Source Excerpt

```lean
theorem nf_uniqueness (nf : NFEinsteinIteration)
    (h : nf.converged = true) :
    nf.current_defect.defect_numer = 0 :=
  nf.convergence_check h
```
