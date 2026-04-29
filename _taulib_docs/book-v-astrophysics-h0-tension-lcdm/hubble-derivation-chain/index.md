---
{
  "projection_kind": "taulib_declaration",
  "title": "HubbleDerivationChain",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-derivation-chain/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::HubbleDerivationChain",
  "declaration_slug": "hubble-derivation-chain",
  "kind": "structure",
  "name": "HubbleDerivationChain",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 536,
  "source_line_end": 553,
  "registry_ids": [
    "V.D319"
  ],
  "related_registry_items": [
    {
      "id": "V.D319",
      "title": "Hubble Derivation Chain",
      "url": "/registry/object/V.D319/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L536-L553",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L536-L553",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L536-L553)
- Source range: L536-L553
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D319` — Hubble Derivation Chain

## Immediate Comment / Docstring

```lean
/-- [V.D319] Hubble Derivation Chain.
    h = 2/3 + ι_τ²/W₃(3) = 0.67352 at −120 ppm from Planck.
    Two-step: EdS base (2/3) + holonomy correction (ι_τ²/17).
    Scope: τ-effective (Wave 38C). -/
```

## Source Excerpt

```lean
structure HubbleDerivationChain where
  /-- EdS base × 100000. -/
  eds_base_x100000 : Nat := 66667
  /-- Holonomy correction × 100000. -/
  correction_x100000 : Nat := 685
  /-- h × 100000. -/
  h_x100000 : Nat := 67352
  /-- Planck h × 100000. -/
  planck_h_x100000 : Nat := 67360
  /-- Deviation ppm. -/
  deviation_ppm : Nat := 120
  /-- W₃(3) = 17 (CF window sum). -/
  w3_3 : Nat := 17
  /-- Free parameters. -/
  free_params : Nat := 0
  /-- Derivation steps. -/
  derivation_steps : Nat := 2
  deriving Repr
```
