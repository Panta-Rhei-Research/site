---
{
  "projection_kind": "taulib_declaration",
  "title": "JetPoloidalField",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-poloidal-field/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::JetPoloidalField",
  "declaration_slug": "jet-poloidal-field",
  "kind": "structure",
  "name": "JetPoloidalField",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 375,
  "source_line_end": 386,
  "registry_ids": [
    "V.D289"
  ],
  "related_registry_items": [
    {
      "id": "V.D289",
      "title": "Jet Poloidal Field",
      "url": "/registry/object/V.D289/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L375-L386",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L375-L386",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L375-L386)
- Source range: L375-L386
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D289` — Jet Poloidal Field

## Immediate Comment / Docstring

```lean
/-- [V.D289] Jet Poloidal Field: axial B-field component in the jet,
    originating from topologically protected flux through the torus hole. -/
```

## Source Excerpt

```lean
structure JetPoloidalField where
  /-- Source name. -/
  source : String
  /-- Poloidal field at base (Gauss × 100). -/
  b_z_base_x100 : Nat
  /-- Toroidal field at base (Gauss × 100). -/
  b_phi_base_x100 : Nat
  /-- Ratio B_z/B_phi × 1000 at base (should be ≈ 341). -/
  ratio_x1000 : Nat := 341
  /-- Topologically anchored (1 = yes). -/
  topo_anchored : Nat := 1
  deriving Repr
```
