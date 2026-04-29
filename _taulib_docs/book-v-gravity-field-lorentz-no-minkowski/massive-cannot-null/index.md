---
{
  "projection_kind": "taulib_declaration",
  "title": "massive_cannot_null",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/massive-cannot-null/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::massive_cannot_null",
  "declaration_slug": "massive-cannot-null",
  "kind": "theorem",
  "name": "massive_cannot_null",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 231,
  "source_line_end": 232,
  "registry_ids": [
    "V.P13"
  ],
  "related_registry_items": [
    {
      "id": "V.P13",
      "title": "Speed barrier as constraint saturation",
      "url": "/registry/object/V.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L231-L232",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.LorentzNoMinkowski",
        "url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L231-L232",
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

- Module: [TauLib.BookV.GravityField.LorentzNoMinkowski](/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/)
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L231-L232)
- Source range: L231-L232
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P13` — Speed barrier as constraint saturation

## Immediate Comment / Docstring

```lean
/-- [V.P13] Massive defects cannot reach the null condition.

    A defect with nonzero fiber stiffness (mass > 0) on T² cannot
    satisfy the null condition. The mass gap prevents massive
    particles from reaching light speed.

    Encoded: any NullIntertwinerField must have massless = true. -/
```

## Source Excerpt

```lean
theorem massive_cannot_null (n : NullIntertwinerField) :
    n.massless = true := n.massless_true
```
