---
{
  "projection_kind": "taulib_declaration",
  "title": "MeasurementProcedure",
  "permalink": "/verify/taulib/docs/book-iv-physics-readout-functor/measurement-procedure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "declaration_id": "TauLib.BookIV.Physics.ReadoutFunctor::MeasurementProcedure",
  "declaration_slug": "measurement-procedure",
  "kind": "structure",
  "name": "MeasurementProcedure",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_url": "/verify/taulib/docs/book-iv-physics-readout-functor/",
  "source_line_start": 72,
  "source_line_end": 85,
  "registry_ids": [
    "IV.D325"
  ],
  "related_registry_items": [
    {
      "id": "IV.D325",
      "title": "Measurement Procedure",
      "url": "/registry/object/IV.D325/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L72-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.ReadoutFunctor",
        "url": "/verify/taulib/docs/book-iv-physics-readout-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L72-L85",
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

- Module: [TauLib.BookIV.Physics.ReadoutFunctor](/verify/taulib/docs/book-iv-physics-readout-functor/)
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L72-L85)
- Source range: L72-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D325` — Measurement Procedure

## Immediate Comment / Docstring

```lean
/-- [IV.D325] An operational measurement procedure: the codomain of
    the readout functor R_μ.

    NOT an abstract SI number. NOT "mass itself." Rather: a complete
    specification of HOW to measure, yielding a number in SI units.

    Examples:
    - Penning trap frequency ratio for m_n
    - Quantum Hall resistance for α
    - Torsion balance protocol for G -/
```

## Source Excerpt

```lean
structure MeasurementProcedure where
  /-- Which physical quantity this procedure measures. -/
  quantity : PrimaryInvariant
  /-- Which sector the source internal object lives in. -/
  source_sector : Sector
  /-- Name of the operational protocol. -/
  protocol : String
  /-- Whether this is the calibration anchor (exactly one: m_n). -/
  is_anchor : Bool
  /-- SI unit string (e.g., "kg", "m/s", dimensionless). -/
  si_unit : String
  /-- Number of exact SI constants used in the readout chain. -/
  exact_constants_used : Nat
  deriving Repr
```
