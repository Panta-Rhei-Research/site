---
{
  "projection_kind": "taulib_declaration",
  "title": "GrowthIndex",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/growth-index/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::GrowthIndex",
  "declaration_slug": "growth-index",
  "kind": "structure",
  "name": "GrowthIndex",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 447,
  "source_line_end": 454,
  "registry_ids": [
    "V.T238"
  ],
  "related_registry_items": [
    {
      "id": "V.T238",
      "title": "Growth Index Theorem",
      "url": "/registry/object/V.T238/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L447-L454",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L447-L454",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L447-L454)
- Source range: L447-L454
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T238` — Growth Index Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T238] Growth index: γ_τ = 0.55 + 0.05·ι_τ³ ≈ 0.552. -/
```

## Source Excerpt

```lean
structure GrowthIndex where
  /-- γ_τ (×1000): 0.552 → 552. -/
  gamma_tau_x1000 : Nat
  /-- γ_ΛCDM (×1000): 0.545 → 545. -/
  gamma_lcdm_x1000 : Nat := 545
  /-- Δγ (×1000): 0.007 → 7. -/
  delta_gamma_x1000 : Nat
  deriving Repr
```
