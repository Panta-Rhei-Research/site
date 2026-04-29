---
{
  "projection_kind": "taulib_declaration",
  "title": "null_set_invariant",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/null-set-invariant/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::null_set_invariant",
  "declaration_slug": "null-set-invariant",
  "kind": "theorem",
  "name": "null_set_invariant",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 158,
  "source_line_end": 159,
  "registry_ids": [
    "V.C02"
  ],
  "related_registry_items": [
    {
      "id": "V.C02",
      "title": "Relativity principle recovered",
      "url": "/registry/object/V.C02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L158-L159",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L158-L159",
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
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L158-L159)
- Source range: L158-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C02` — Relativity principle recovered

## Immediate Comment / Docstring

```lean
/-- [V.C02] The null set is readout-invariant: the set of null
    worldlines (light rays) is preserved by any admissible
    readout-functor transformation.

    This invariance is the structural origin of c = const.
    Speed of light constancy is NOT an axiom — it follows from
    null-intertwiner masslessness and readout-functor preservation. -/
```

## Source Excerpt

```lean
theorem null_set_invariant :
    photon_field.speed_is_c = true := by rfl
```
