---
{
  "projection_kind": "taulib_declaration",
  "title": "ChargeQuantum",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/charge-quantum/",
  "summary_short": "`structure` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::ChargeQuantum",
  "declaration_slug": "charge-quantum",
  "kind": "structure",
  "name": "ChargeQuantum",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 118,
  "source_line_end": 121,
  "registry_ids": [
    "V.R149"
  ],
  "related_registry_items": [
    {
      "id": "V.R149",
      "title": "Charge quantization",
      "url": "/registry/object/V.R149/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L118-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.ChargeObstruction",
        "url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L118-L121",
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

- Module: [TauLib.BookV.FluidMacro.ChargeObstruction](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/)
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L118-L121)
- Source range: L118-L121
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R149` — Charge quantization

## Immediate Comment / Docstring

```lean
/-- [V.R149] Charge quantization: the holonomy takes values in a compact
    group, and compact-group representations are discrete (q ∈ ℤ).

    In the orthodox framework, charge quantization is postulated;
    here it follows from the topology of L. -/
```

## Source Excerpt

```lean
structure ChargeQuantum where
  /-- Integer charge in units of elementary charge. -/
  q : Int
  deriving Repr, DecidableEq, BEq
```
