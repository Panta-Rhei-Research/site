---
{
  "projection_kind": "taulib_declaration",
  "title": "CollapsePhase",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/collapse-phase/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::CollapsePhase",
  "declaration_slug": "collapse-phase",
  "kind": "inductive",
  "name": "CollapsePhase",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 111,
  "source_line_end": 124,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L111-L124",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L111-L124",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L111-L124)
- Source range: L111-L124
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Core collapse phase. -/
```

## Source Excerpt

```lean
inductive CollapsePhase where
  /-- Iron core growth to M_Ch. -/
  | IronCoreGrowth
  /-- Electron capture and core collapse. -/
  | ElectronCapture
  /-- Bounce at nuclear density. -/
  | Bounce
  /-- Shock revival by neutrino heating. -/
  | ShockRevival
  /-- Envelope ejection. -/
  | EnvelopeEjection
  /-- Remnant formation (NS or BH). -/
  | RemnantFormation
  deriving Repr, DecidableEq, BEq
```
