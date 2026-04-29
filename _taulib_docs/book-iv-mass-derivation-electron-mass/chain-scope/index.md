---
{
  "projection_kind": "taulib_declaration",
  "title": "ChainScope",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-scope/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::ChainScope",
  "declaration_slug": "chain-scope",
  "kind": "inductive",
  "name": "ChainScope",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 35,
  "source_line_end": 38,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L35-L38",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.ElectronMass",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L35-L38",
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

- Module: [TauLib.BookIV.MassDerivation.ElectronMass](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/)
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L35-L38)
- Source range: L35-L38
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Scope label for chain links. -/
```

## Source Excerpt

```lean
inductive ChainScope
  | Established    -- Standard mathematics
  | TauEffective   -- τ-framework derived
  deriving Repr, DecidableEq, BEq
```
