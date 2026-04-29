---
{
  "projection_kind": "taulib_declaration",
  "title": "QuantizedCirculationProp",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/quantized-circulation-prop/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::QuantizedCirculationProp",
  "declaration_slug": "quantized-circulation-prop",
  "kind": "structure",
  "name": "QuantizedCirculationProp",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 201,
  "source_line_end": 210,
  "registry_ids": [
    "IV.P141"
  ],
  "related_registry_items": [
    {
      "id": "IV.P141",
      "title": "Quantized circulation",
      "url": "/registry/object/IV.P141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L201-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L201-L210",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L201-L210)
- Source range: L201-L210
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P141` — Quantized circulation

## Immediate Comment / Docstring

```lean
/-- [IV.P141] In the superfluid regime the circulation around any closed
    loop C on T^2 is quantized: integral v_s dot dl = (2*pi*hbar_tau/m) * theta_C
    with theta_C in Z. This follows from theta integrality on T^2. -/
```

## Source Excerpt

```lean
structure QuantizedCirculationProp where
  /-- Circulation quantum (1 quantum per winding number). -/
  circulation_quantum : Nat := 1
  /-- Quantum: 2*pi*hbar_tau/m per winding number. -/
  quantum_formula : String := "2*pi*hbar_tau/m * theta_C"
  /-- Theta denominator (1 = integer, i.e., theta_C in Z). -/
  theta_denominator : Nat := 1
  /-- Integer quantization: denominator is 1. -/
  is_integer : theta_denominator = 1
  deriving Repr
```
