---
{
  "projection_kind": "taulib_declaration",
  "title": "null_is_readout_invariant",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/null-is-readout-invariant/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.LorentzNoMinkowski`.",
  "declaration_id": "TauLib.BookV.GravityField.LorentzNoMinkowski::null_is_readout_invariant",
  "declaration_slug": "null-is-readout-invariant",
  "kind": "theorem",
  "name": "null_is_readout_invariant",
  "module_name": "TauLib.BookV.GravityField.LorentzNoMinkowski",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-lorentz-no-minkowski/",
  "source_line_start": 214,
  "source_line_end": 218,
  "registry_ids": [
    "V.P12"
  ],
  "related_registry_items": [
    {
      "id": "V.P12",
      "title": "Light cone is Lorentz-invariant",
      "url": "/registry/object/V.P12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L214-L218",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L214-L218",
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
- Source path: [`TauLib/BookV/GravityField/LorentzNoMinkowski.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/LorentzNoMinkowski.lean#L214-L218)
- Source range: L214-L218
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P12` — Light cone is Lorentz-invariant

## Immediate Comment / Docstring

```lean
/-- [V.P12] Null set invariance: the null intertwiner selects a
    unique sector (EM) and propagation speed (c).

    Any readout functor preserving the boundary-character structure
    must preserve the null set. This is the structural content of
    "Lorentz invariance of the speed of light." -/
```

## Source Excerpt

```lean
theorem null_is_readout_invariant :
    photon_field.sector = .B ∧
    photon_field.massless = true ∧
    photon_field.speed_is_c = true :=
  ⟨rfl, rfl, rfl⟩
```
