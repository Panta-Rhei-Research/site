---
{
  "projection_kind": "taulib_declaration",
  "title": "chain_indices",
  "permalink": "/corpus/taulib/docs/book-iv-mass-derivation-electron-mass/chain-indices/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::chain_indices",
  "declaration_slug": "chain-indices",
  "kind": "theorem",
  "name": "chain_indices",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/corpus/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 63,
  "source_line_end": 65,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L63-L65",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.ElectronMass",
        "url": "/corpus/taulib/docs/book-iv-mass-derivation-electron-mass/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L63-L65",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.MassDerivation.ElectronMass](/corpus/taulib/docs/book-iv-mass-derivation-electron-mass/)
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L63-L65)
- Source range: L63-L65
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem chain_indices :
    (derivation_chain.map ChainLink.index) =
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] := by rfl
```
