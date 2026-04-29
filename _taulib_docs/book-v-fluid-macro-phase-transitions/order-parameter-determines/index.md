---
{
  "projection_kind": "taulib_declaration",
  "title": "order_parameter_determines",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/order-parameter-determines/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.PhaseTransitions`.",
  "declaration_id": "TauLib.BookV.FluidMacro.PhaseTransitions::order_parameter_determines",
  "declaration_slug": "order-parameter-determines",
  "kind": "theorem",
  "name": "order_parameter_determines",
  "module_name": "TauLib.BookV.FluidMacro.PhaseTransitions",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/",
  "source_line_start": 92,
  "source_line_end": 94,
  "registry_ids": [
    "V.P54"
  ],
  "related_registry_items": [
    {
      "id": "V.P54",
      "title": "Crossing preservation",
      "url": "/registry/object/V.P54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L92-L94",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.PhaseTransitions",
        "url": "/verify/taulib/docs/book-v-fluid-macro-phase-transitions/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L92-L94",
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

- Module: [TauLib.BookV.FluidMacro.PhaseTransitions](/verify/taulib/docs/book-v-fluid-macro-phase-transitions/)
- Source path: [`TauLib/BookV/FluidMacro/PhaseTransitions.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/PhaseTransitions.lean#L92-L94)
- Source range: L92-L94
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P54` — Crossing preservation

## Immediate Comment / Docstring

```lean
/-- [V.P54] Order parameter determines phase. -/
```

## Source Excerpt

```lean
theorem order_parameter_determines (op : TauOrderParameter)
    (h : op.value = 0) : op.phase = .Disordered :=
  op.consistent.1 h
```
