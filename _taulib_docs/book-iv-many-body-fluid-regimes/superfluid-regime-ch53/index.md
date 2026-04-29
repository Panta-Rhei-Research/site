---
{
  "projection_kind": "taulib_declaration",
  "title": "SuperfluidRegimeCh53",
  "permalink": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/superfluid-regime-ch53/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::SuperfluidRegimeCh53",
  "declaration_slug": "superfluid-regime-ch53",
  "kind": "structure",
  "name": "SuperfluidRegimeCh53",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/verify/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 176,
  "source_line_end": 189,
  "registry_ids": [
    "IV.D233"
  ],
  "related_registry_items": [
    {
      "id": "IV.D233",
      "title": "Superfluid regime",
      "url": "/registry/object/IV.D233/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L176-L189",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L176-L189",
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
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L176-L189)
- Source range: L176-L189
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D233` — Superfluid regime

## Immediate Comment / Docstring

```lean
/-- [IV.D233] Superfluid regime (ch53 formulation): mu is maximal (free
    base-direction translation), nu = 0 except at isolated vortex cores
    with integer winding number, kappa = 0 (incompressible), theta quantized.

    Extended from ch52 with explicit circulation quantization. -/
```

## Source Excerpt

```lean
structure SuperfluidRegimeCh53 where
  /-- Mobility rank (1 = maximal among regimes). -/
  mobility_rank : Nat := 1
  /-- Bulk vorticity degree (0 = zero away from cores). -/
  bulk_vorticity_degree : Nat := 0
  /-- Compressibility degree (kappa = 0 means incompressible). -/
  kappa_degree : Nat := 0
  /-- Theta quantum number (1 = integer quantization in Z). -/
  theta_quantum : Nat := 1
  /-- Minimum nonzero winding number. -/
  min_winding_number : Nat := 1
  /-- Winding is integer: quantum equals minimum. -/
  winding_is_integer : theta_quantum = min_winding_number
  deriving Repr
```
