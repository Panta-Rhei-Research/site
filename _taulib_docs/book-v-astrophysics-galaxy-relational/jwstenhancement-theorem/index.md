---
{
  "projection_kind": "taulib_declaration",
  "title": "JWSTEnhancementTheorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/jwstenhancement-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.GalaxyRelational`.",
  "declaration_id": "TauLib.BookV.Astrophysics.GalaxyRelational::JWSTEnhancementTheorem",
  "declaration_slug": "jwstenhancement-theorem",
  "kind": "structure",
  "name": "JWSTEnhancementTheorem",
  "module_name": "TauLib.BookV.Astrophysics.GalaxyRelational",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/",
  "source_line_start": 272,
  "source_line_end": 285,
  "registry_ids": [
    "V.T239"
  ],
  "related_registry_items": [
    {
      "id": "V.T239",
      "title": "JWST Enhancement Theorem",
      "url": "/registry/object/V.T239/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L272-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.GalaxyRelational",
        "url": "/verify/taulib/docs/book-v-astrophysics-galaxy-relational/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L272-L285",
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

- Module: [TauLib.BookV.Astrophysics.GalaxyRelational](/verify/taulib/docs/book-v-astrophysics-galaxy-relational/)
- Source path: [`TauLib/BookV/Astrophysics/GalaxyRelational.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/GalaxyRelational.lean#L272-L285)
- Source range: L272-L285
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T239` — JWST Enhancement Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T239] JWST Enhancement Theorem:
    Enhanced a₀(z) produces deeper potential wells → faster collapse → higher SFE.
    SFE(z)/SFE(0) ~ [E(z)]^(1/2) from virial-threshold crossing. -/
```

## Source Excerpt

```lean
structure JWSTEnhancementTheorem where
  /-- Galaxy name / field. -/
  name : String
  /-- Observed redshift (×10). -/
  z_x10 : Nat
  /-- Observed stellar mass (log₁₀ M_☉, ×10). -/
  log_mass_x10 : Nat
  /-- ΛCDM required SFE (percent). -/
  lcdm_sfe_pct : Nat
  /-- τ-enhanced SFE (percent). -/
  tau_sfe_pct : Nat
  /-- Enhancement factor (×10). -/
  enhancement_x10 : Nat
  deriving Repr
```
