---
{
  "projection_kind": "taulib_declaration",
  "title": "EWAxiomTrace",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/ewaxiom-trace/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::EWAxiomTrace",
  "declaration_slug": "ewaxiom-trace",
  "kind": "structure",
  "name": "EWAxiomTrace",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 171,
  "source_line_end": 180,
  "registry_ids": [
    "IV.T67"
  ],
  "related_registry_items": [
    {
      "id": "IV.T67",
      "title": "Zero Free Parameters in Electroweak Sector",
      "url": "/registry/object/IV.T67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L171-L180",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L171-L180",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L171-L180)
- Source range: L171-L180
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T67` — Zero Free Parameters in Electroweak Sector

## Immediate Comment / Docstring

```lean
/-- [IV.T67] The derivation chain for every EW quantity passes
    through at most two fundamental inputs:
    1. ι_τ = 2/(π+e) — the master constant from K0-K6.
    2. m_n — the neutron mass anchor (a single measured input).

    All coupling constants, mixing angles, and masses are
    rational functions of ι_τ evaluated at the neutron anchor. -/
```

## Source Excerpt

```lean
structure EWAxiomTrace where
  /-- Number of fundamental inputs. -/
  input_count : Nat := 2
  /-- Input 1: master constant. -/
  input_1 : String := "iota_tau = 2/(pi+e)"
  /-- Input 2: neutron mass anchor. -/
  input_2 : String := "m_n = 939.565 MeV"
  /-- All 9 quantities trace to these. -/
  all_trace : Bool := true
  deriving Repr
```
