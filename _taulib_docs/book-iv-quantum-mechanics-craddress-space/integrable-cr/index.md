---
{
  "projection_kind": "taulib_declaration",
  "title": "IntegrableCR",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/integrable-cr/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.CRAddressSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.CRAddressSpace::IntegrableCR",
  "declaration_slug": "integrable-cr",
  "kind": "structure",
  "name": "IntegrableCR",
  "module_name": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/",
  "source_line_start": 70,
  "source_line_end": 74,
  "registry_ids": [
    "IV.P08"
  ],
  "related_registry_items": [
    {
      "id": "IV.P08",
      "title": "Integrability Criterion",
      "url": "/registry/object/IV.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L70-L74",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.CRAddressSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L70-L74",
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

- Module: [TauLib.BookIV.QuantumMechanics.CRAddressSpace](/verify/taulib/docs/book-iv-quantum-mechanics-craddress-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/CRAddressSpace.lean#L70-L74)
- Source range: L70-L74
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P08` — Integrability Criterion

## Immediate Comment / Docstring

```lean
/-- [IV.P08] CR-structure integrability: a CR-structure is integrable
    iff the Nijenhuis tensor of J vanishes. Formalized structurally:
    the boolean flag records the vanishing condition. -/
```

## Source Excerpt

```lean
structure IntegrableCR extends CRManifold where
  /-- Nijenhuis tensor vanishes. -/
  nijenhuis_vanishes : Bool
  nij_true : nijenhuis_vanishes = true
  deriving Repr
```
