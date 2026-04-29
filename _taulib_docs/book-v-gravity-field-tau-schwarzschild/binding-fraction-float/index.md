---
{
  "projection_kind": "taulib_declaration",
  "title": "GeometricRelaxation.bindingFractionFloat",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/binding-fraction-float/",
  "summary_short": "`def` declaration in `TauLib.BookV.GravityField.TauSchwarzschild`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschild::GeometricRelaxation.bindingFractionFloat",
  "declaration_slug": "binding-fraction-float",
  "kind": "def",
  "name": "GeometricRelaxation.bindingFractionFloat",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/",
  "source_line_start": 123,
  "source_line_end": 125,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L123-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L123-L125",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschild](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschild.lean#L123-L125)
- Source range: L123-L125
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Binding energy fraction as Float. -/
```

## Source Excerpt

```lean
def GeometricRelaxation.bindingFractionFloat (g : GeometricRelaxation) : Float :=
  let lost := g.initial_mass_numer - g.stable_mass_numer
  Float.ofNat lost / Float.ofNat g.initial_mass_numer
```
