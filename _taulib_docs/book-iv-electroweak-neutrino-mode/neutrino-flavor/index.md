---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoFlavor",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-flavor/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::NeutrinoFlavor",
  "declaration_slug": "neutrino-flavor",
  "kind": "inductive",
  "name": "NeutrinoFlavor",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 36,
  "source_line_end": 43,
  "registry_ids": [
    "IV.D125"
  ],
  "related_registry_items": [
    {
      "id": "IV.D125",
      "title": "Neutrino Flavor Eigenstates",
      "url": "/registry/object/IV.D125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L36-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L36-L43",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L36-L43)
- Source range: L36-L43
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D125` — Neutrino Flavor Eigenstates

## Immediate Comment / Docstring

```lean
/-- [IV.D125] The three neutrino flavors, one per generation.
    Each flavor is paired with its charged lepton partner in
    a left-handed doublet under SU(2)_L. -/
```

## Source Excerpt

```lean
inductive NeutrinoFlavor where
  /-- Electron neutrino (1st generation). -/
  | Electron
  /-- Muon neutrino (2nd generation). -/
  | Muon
  /-- Tau neutrino (3rd generation). -/
  | Tau
  deriving Repr, DecidableEq, BEq
```
