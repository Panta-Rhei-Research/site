---
{
  "projection_kind": "taulib_declaration",
  "title": "TauNSRegularity",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/tau-nsregularity/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::TauNSRegularity",
  "declaration_slug": "tau-nsregularity",
  "kind": "structure",
  "name": "TauNSRegularity",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 150,
  "source_line_end": 159,
  "registry_ids": [
    "IV.T93"
  ],
  "related_registry_items": [
    {
      "id": "IV.T93",
      "title": "τ-NS Regularity on T² Fiber (C3 Defect Contractivity)",
      "url": "/registry/object/IV.T93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L150-L159",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L150-L159",
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/verify/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L150-L159)
- Source range: L150-L159
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T93` — τ-NS Regularity on T² Fiber (C3 Defect Contractivity)

## Immediate Comment / Docstring

```lean
/-- [IV.T93] (CONJECTURAL) tau-NS regularity: for every tau-admissible initial
    datum on the fiber T^2, the tau-NS evolution produces a well-defined,
    bounded velocity readout at all times.

    SCOPE: conjectural. Regularity is unconditional within the tau-admissible
    class, but closing the gap to the Clay Millennium Problem's Sobolev-class
    solutions requires further analysis. -/
```

## Source Excerpt

```lean
structure TauNSRegularity where
  /-- Bounded velocity readout at all times. -/
  bounded_readout : Bool := true
  /-- Unconditional within tau-admissible class. -/
  within_tau_admissible : Bool := true
  /-- Gap to Clay problem remains. -/
  clay_gap_open : Bool := true
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  deriving Repr
```
