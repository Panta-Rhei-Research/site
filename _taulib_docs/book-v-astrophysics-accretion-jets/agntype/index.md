---
{
  "projection_kind": "taulib_declaration",
  "title": "AGNType",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/agntype/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.AccretionJets`.",
  "declaration_id": "TauLib.BookV.Astrophysics.AccretionJets::AGNType",
  "declaration_slug": "agntype",
  "kind": "inductive",
  "name": "AGNType",
  "module_name": "TauLib.BookV.Astrophysics.AccretionJets",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-accretion-jets/",
  "source_line_start": 211,
  "source_line_end": 224,
  "registry_ids": [
    "V.D132"
  ],
  "related_registry_items": [
    {
      "id": "V.D132",
      "title": "AGN Lifecycle Phase",
      "url": "/registry/object/V.D132/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L211-L224",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L211-L224",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookV/Astrophysics/AccretionJets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/AccretionJets.lean#L211-L224)
- Source range: L211-L224
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D132` — AGN Lifecycle Phase

## Immediate Comment / Docstring

```lean
/-- [V.D132] AGN classification: active galactic nuclei classified
    by accretion rate and viewing angle.

    In the τ-framework, the AGN "zoo" is a single phenomenon
    (accretion + jets around a supermassive BH) viewed from
    different angles and accretion states. -/
```

## Source Excerpt

```lean
inductive AGNType where
  /-- Seyfert 1: face-on view, broad lines visible. -/
  | Seyfert1
  /-- Seyfert 2: edge-on, broad lines obscured. -/
  | Seyfert2
  /-- Quasar: high-luminosity AGN. -/
  | Quasar
  /-- Blazar: jet pointed at observer. -/
  | Blazar
  /-- Radio galaxy: powerful jets, large lobes. -/
  | RadioGalaxy
  /-- LINER: low-ionization nuclear emission region. -/
  | LINER
  deriving Repr, DecidableEq, BEq
```
