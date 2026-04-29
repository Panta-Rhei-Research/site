---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_scope_distribution",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/chain-scope-distribution/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::chain_scope_distribution",
  "declaration_slug": "chain-scope-distribution",
  "kind": "theorem",
  "name": "chain_scope_distribution",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 87,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L87-L90",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L87-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L87-L90)
- Source range: L87-L90
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem chain_scope_distribution :
    scope_distribution.established + scope_distribution.tau_effective +
    scope_distribution.conjectural = 10 :=
  scope_distribution.total_eq
```
