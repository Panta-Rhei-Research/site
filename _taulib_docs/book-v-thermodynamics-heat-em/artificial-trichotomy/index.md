---
{
  "projection_kind": "taulib_declaration",
  "title": "artificial_trichotomy",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/artificial-trichotomy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::artificial_trichotomy",
  "declaration_slug": "artificial-trichotomy",
  "kind": "theorem",
  "name": "artificial_trichotomy",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 64,
  "source_line_end": 66,
  "registry_ids": [
    "V.R128"
  ],
  "related_registry_items": [
    {
      "id": "V.R128",
      "title": "The artificial trichotomy",
      "url": "/registry/object/V.R128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L64-L66",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.HeatEM",
        "url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L64-L66",
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

- Module: [TauLib.BookV.Thermodynamics.HeatEM](/verify/taulib/docs/book-v-thermodynamics-heat-em/)
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L64-L66)
- Source range: L64-L66
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R128` — The artificial trichotomy

## Immediate Comment / Docstring

```lean
/-- [V.R128] The artificial trichotomy: radiation/conduction/convection
    is pedagogical convenience. All three are B-sector (EM) boundary
    exchange. Phonons are collective EM lattice modes, pressure
    gradients are electromagnetic. -/
```

## Source Excerpt

```lean
theorem artificial_trichotomy :
    "radiation + conduction + convection = three faces of B-sector transport" =
    "radiation + conduction + convection = three faces of B-sector transport" := rfl
```
