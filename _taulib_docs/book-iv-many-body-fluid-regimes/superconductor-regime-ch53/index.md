---
{
  "projection_kind": "taulib_declaration",
  "title": "SuperconductorRegimeCh53",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/superconductor-regime-ch53/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::SuperconductorRegimeCh53",
  "declaration_slug": "superconductor-regime-ch53",
  "kind": "structure",
  "name": "SuperconductorRegimeCh53",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 222,
  "source_line_end": 231,
  "registry_ids": [
    "IV.D234"
  ],
  "related_registry_items": [
    {
      "id": "IV.D234",
      "title": "Superconductor regime",
      "url": "/registry/object/IV.D234/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L222-L231",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L222-L231",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L222-L231)
- Source range: L222-L231
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D234` — Superconductor regime

## Immediate Comment / Docstring

```lean
/-- [IV.D234] Superconductor regime (ch53 formulation): B-sector mobility
    mu_B is maximal, topological charge theta_B in Z is quantized, and
    magnetic flux Phi is quantized in units of Phi_0 = h/(2e). -/
```

## Source Excerpt

```lean
structure SuperconductorRegimeCh53 where
  /-- B-sector mobility rank (1 = maximal). -/
  b_sector_rank : Nat := 1
  /-- Theta quantum number (1 = integer quantization). -/
  theta_quantum : Nat := 1
  /-- Cooper pair charge count (2e → Phi_0 = h/(2e)). -/
  flux_quantum_pairs : Nat := 2
  /-- Number of spectral gaps (1 = BCS gap). -/
  n_spectral_gaps : Nat := 1
  deriving Repr
```
