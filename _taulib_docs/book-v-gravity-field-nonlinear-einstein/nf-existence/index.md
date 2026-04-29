---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_existence",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-existence/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::nf_existence",
  "declaration_slug": "nf-existence",
  "kind": "theorem",
  "name": "nf_existence",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 290,
  "source_line_end": 292,
  "registry_ids": [
    "V.T33"
  ],
  "related_registry_items": [
    {
      "id": "V.T33",
      "title": "Existence",
      "url": "/registry/object/V.T33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L290-L292",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L290-L292",
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
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L290-L292)
- Source range: L290-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T33` — Existence

## Immediate Comment / Docstring

```lean
/-- [V.T33] Existence of NF Einstein iteration: for any initial
    matter configuration, the NF iteration exists and produces
    a sequence of decreasing-defect solutions.

    Encoded: any NFEinsteinIteration has a well-defined depth
    and current defect with positive denominator. -/
```

## Source Excerpt

```lean
theorem nf_existence (nf : NFEinsteinIteration) :
    nf.current_defect.defect_denom > 0 :=
  nf.current_defect.denom_pos
```
