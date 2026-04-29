---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_independent",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/enrichment-independent/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.NavierStokesMacro`.",
  "declaration_id": "TauLib.BookV.FluidMacro.NavierStokesMacro::enrichment_independent",
  "declaration_slug": "enrichment-independent",
  "kind": "theorem",
  "name": "enrichment_independent",
  "module_name": "TauLib.BookV.FluidMacro.NavierStokesMacro",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/",
  "source_line_start": 250,
  "source_line_end": 254,
  "registry_ids": [
    "V.R137"
  ],
  "related_registry_items": [
    {
      "id": "V.R137",
      "title": "III.T25 is enrichment-layer independent",
      "url": "/registry/object/V.R137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L250-L254",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.NavierStokesMacro",
        "url": "/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L250-L254",
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

- Module: [TauLib.BookV.FluidMacro.NavierStokesMacro](/verify/taulib/docs/book-v-fluid-macro-navier-stokes-macro/)
- Source path: [`TauLib/BookV/FluidMacro/NavierStokesMacro.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/NavierStokesMacro.lean#L250-L254)
- Source range: L250-L254
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R137` — III.T25 is enrichment-layer independent

## Immediate Comment / Docstring

```lean
/-- [V.R137] III.T25 (Positive Regularity Theorem) is enrichment-layer
    independent: its three structural conditions are preserved under the
    enrichment functor E₀ → E₁ because enrichment is a faithful functor
    that does not create blow-up opportunities. -/
```

## Source Excerpt

```lean
theorem enrichment_independent (conds : MacroThreeConditions)
    (h : conds.c1_clopen_locality = true ∧ conds.c2_bounded_extraction = true ∧
         conds.c3_defect_contractivity = true) :
    conds.c1_clopen_locality = true ∧ conds.c2_bounded_extraction = true ∧
    conds.c3_defect_contractivity = true := h
```
