---
{
  "projection_kind": "taulib_declaration",
  "title": "JetHelicity",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/jet-helicity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::JetHelicity",
  "declaration_slug": "jet-helicity",
  "kind": "structure",
  "name": "JetHelicity",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 389,
  "source_line_end": 398,
  "registry_ids": [
    "V.D290"
  ],
  "related_registry_items": [
    {
      "id": "V.D290",
      "title": "Jet Magnetic Helicity",
      "url": "/registry/object/V.D290/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L389-L398",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L389-L398",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L389-L398)
- Source range: L389-L398
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D290` — Jet Magnetic Helicity

## Immediate Comment / Docstring

```lean
/-- [V.D290] Jet Magnetic Helicity: H_m = ∫ A·B dV, conserved in ideal MHD. -/
```

## Source Excerpt

```lean
structure JetHelicity where
  /-- Helicity sign: +1 or -1, fixed by T² topology. -/
  sign : Int
  /-- Sign is ±1. -/
  sign_valid : sign = 1 ∨ sign = -1
  /-- Conserved in ideal MHD (1 = yes). -/
  conserved : Nat := 1
  /-- Fixed by topology (1 = yes). -/
  fixed_by_topology : Nat := 1
  deriving Repr
```
