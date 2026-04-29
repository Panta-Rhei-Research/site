---
{
  "projection_kind": "taulib_declaration",
  "title": "ck_observational_match",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-turbulence/ck-observational-match/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.Turbulence`.",
  "declaration_id": "TauLib.BookV.FluidMacro.Turbulence::ck_observational_match",
  "declaration_slug": "ck-observational-match",
  "kind": "theorem",
  "name": "ck_observational_match",
  "module_name": "TauLib.BookV.FluidMacro.Turbulence",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/",
  "source_line_start": 455,
  "source_line_end": 456,
  "registry_ids": [
    "V.P171"
  ],
  "related_registry_items": [
    {
      "id": "V.P171",
      "title": "C_K Observational Match",
      "url": "/registry/object/V.P171/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L455-L456",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.Turbulence",
        "url": "/verify/taulib/docs/book-v-fluid-macro-turbulence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L455-L456",
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

- Module: [TauLib.BookV.FluidMacro.Turbulence](/verify/taulib/docs/book-v-fluid-macro-turbulence/)
- Source path: [`TauLib/BookV/FluidMacro/Turbulence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/Turbulence.lean#L455-L456)
- Source range: L455-L456
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P171` — C_K Observational Match

## Immediate Comment / Docstring

```lean
/-- [V.P171] C_K observational match.

    Prediction: C_K = 3/2 = 1.5.
    Observed: C_K = 1.5 ± 0.1 (Sreenivasan 1995).
    Deviation: 0.0%. -/
```

## Source Excerpt

```lean
theorem ck_observational_match :
    ck_derived.deviation_ppm = 0 := rfl
```
