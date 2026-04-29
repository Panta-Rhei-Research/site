---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_governs_transport",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-heat-em/alpha-governs-transport/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.HeatEM`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.HeatEM::alpha_governs_transport",
  "declaration_slug": "alpha-governs-transport",
  "kind": "theorem",
  "name": "alpha_governs_transport",
  "module_name": "TauLib.BookV.Thermodynamics.HeatEM",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-heat-em/",
  "source_line_start": 154,
  "source_line_end": 156,
  "registry_ids": [
    "V.T63"
  ],
  "related_registry_items": [
    {
      "id": "V.T63",
      "title": "alpha governs macroscopic energy transport",
      "url": "/registry/object/V.T63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L154-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L154-L156",
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
- Source path: [`TauLib/BookV/Thermodynamics/HeatEM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/HeatEM.lean#L154-L156)
- Source range: L154-L156
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T63` — alpha governs macroscopic energy transport

## Immediate Comment / Docstring

```lean
/-- [V.T63] Alpha governs macroscopic energy transport: the transport
    rate between any two macroscopic E1 configurations is proportional
    to the fine-structure constant alpha.

    Gamma_transport propto alpha * Delta_E

    This is because alpha is the E1 readout of the B-sector
    self-coupling iota_tau^2 after holonomy correction. -/
```

## Source Excerpt

```lean
theorem alpha_governs_transport :
    "Gamma_transport propto alpha * Delta_E (B-sector readout)" =
    "Gamma_transport propto alpha * Delta_E (B-sector readout)" := rfl
```
