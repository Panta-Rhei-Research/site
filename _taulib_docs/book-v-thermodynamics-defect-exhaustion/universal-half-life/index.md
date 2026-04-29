---
{
  "projection_kind": "taulib_declaration",
  "title": "universal_half_life",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/universal-half-life/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.DefectExhaustion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.DefectExhaustion::universal_half_life",
  "declaration_slug": "universal-half-life",
  "kind": "theorem",
  "name": "universal_half_life",
  "module_name": "TauLib.BookV.Thermodynamics.DefectExhaustion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/",
  "source_line_start": 343,
  "source_line_end": 344,
  "registry_ids": [
    "V.R125",
    "V.R126"
  ],
  "related_registry_items": [
    {
      "id": "V.R125",
      "title": "Contrast with heat death",
      "url": "/registry/object/V.R125/"
    },
    {
      "id": "V.R126",
      "title": "Universal half-life",
      "url": "/registry/object/V.R126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L343-L344",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.DefectExhaustion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L343-L344",
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

- Module: [TauLib.BookV.Thermodynamics.DefectExhaustion](/verify/taulib/docs/book-v-thermodynamics-defect-exhaustion/)
- Source path: [`TauLib/BookV/Thermodynamics/DefectExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/DefectExhaustion.lean#L343-L344)
- Source range: L343-L344
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R125` — Contrast with heat death
- `V.R126` — Universal half-life

## Immediate Comment / Docstring

```lean
-- [V.R125] Contrast with Heat Death: classical heat death is asymptotic
-- (never exactly arrives). The coherence horizon is a finite event.

-- [V.R126] Universal Half-Life: n_{1/2} ~ 1.66 does not depend on
-- defect type or regime.
```

## Source Excerpt

```lean
theorem universal_half_life :
    canonical_half_life.is_universal = true := rfl
```
