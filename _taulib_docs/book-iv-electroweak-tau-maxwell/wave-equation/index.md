---
{
  "projection_kind": "taulib_declaration",
  "title": "WaveEquation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/wave-equation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::WaveEquation",
  "declaration_slug": "wave-equation",
  "kind": "structure",
  "name": "WaveEquation",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 332,
  "source_line_end": 339,
  "registry_ids": [
    "IV.T47"
  ],
  "related_registry_items": [
    {
      "id": "IV.T47",
      "title": "EM Wave Equation",
      "url": "/registry/object/IV.T47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L332-L339",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L332-L339",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L332-L339)
- Source range: L332-L339
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T47` — EM Wave Equation

## Immediate Comment / Docstring

```lean
/-- [IV.T47] Source-free Lorenz gauge gives wave equation □A_μ = 0.
    Solutions are plane waves: the photon field. -/
```

## Source Excerpt

```lean
structure WaveEquation where
  /-- Source-free (J = 0). -/
  source_free : Bool := true
  /-- Lorenz gauge imposed. -/
  lorenz_gauge : Bool := true
  /-- Resulting equation is □A = 0. -/
  is_wave_eq : Bool := true
  deriving Repr
```
