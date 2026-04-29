---
{
  "projection_kind": "taulib_declaration",
  "title": "FluxRatio",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/flux-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::FluxRatio",
  "declaration_slug": "flux-ratio",
  "kind": "structure",
  "name": "FluxRatio",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 358,
  "source_line_end": 367,
  "registry_ids": [
    "V.P153"
  ],
  "related_registry_items": [
    {
      "id": "V.P153",
      "title": "Flux Ratio",
      "url": "/registry/object/V.P153/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L358-L367",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.AccretionJets",
        "url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L358-L367",
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

- Module: [TauLib.BookV.Astrophysics.AccretionJets](/verify/taulib/docs/book-v-astrophysics-accretion-jets/)
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L358-L367)
- Source range: L358-L367
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P153` — Flux Ratio

## Immediate Comment / Docstring

```lean
/-- [V.P153] Flux Ratio: Φ_pol/Φ_tor ~ ι_τ ≈ 0.341 from area ratio. -/
```

## Source Excerpt

```lean
structure FluxRatio where
  /-- Poloidal flux (units × 1000). -/
  phi_pol_x1000 : Nat
  /-- Toroidal flux (units × 1000). -/
  phi_tor_x1000 : Nat
  /-- Toroidal flux is positive. -/
  tor_pos : phi_tor_x1000 > 0
  /-- Ratio × 1000 (should be ≈ 341). -/
  ratio_x1000 : Nat := 341
  deriving Repr
```
