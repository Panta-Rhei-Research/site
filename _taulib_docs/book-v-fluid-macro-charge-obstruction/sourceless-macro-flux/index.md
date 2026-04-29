---
{
  "projection_kind": "taulib_declaration",
  "title": "sourceless_macro_flux",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/sourceless-macro-flux/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.ChargeObstruction`.",
  "declaration_id": "TauLib.BookV.FluidMacro.ChargeObstruction::sourceless_macro_flux",
  "declaration_slug": "sourceless-macro-flux",
  "kind": "theorem",
  "name": "sourceless_macro_flux",
  "module_name": "TauLib.BookV.FluidMacro.ChargeObstruction",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/",
  "source_line_start": 137,
  "source_line_end": 138,
  "registry_ids": [
    "V.C10"
  ],
  "related_registry_items": [
    {
      "id": "V.C10",
      "title": "Sourceless macro flux",
      "url": "/registry/object/V.C10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L137-L138",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L137-L138",
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

- Module: [TauLib.BookV.FluidMacro.ChargeObstruction](/verify/taulib/docs/book-v-fluid-macro-charge-obstruction/)
- Source path: [`TauLib/BookV/FluidMacro/ChargeObstruction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/ChargeObstruction.lean#L137-L138)
- Source range: L137-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C10` — Sourceless macro flux

## Immediate Comment / Docstring

```lean
/-- [V.C10] Sourceless macro flux: for any closed surface Σ in τ³,
    the net B-sector flux vanishes.

    ∫_Σ F_B · dΣ = 0

    Gauss's law is trivially satisfied because every closed surface
    encloses zero net charge. -/
```

## Source Excerpt

```lean
theorem sourceless_macro_flux (t : NoIsolatedChargesThm) :
    t.positive_charges = t.negative_charges := t.balance
```
