---
{
  "projection_kind": "taulib_declaration",
  "title": "Level0Formula",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-formula/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::Level0Formula",
  "declaration_slug": "level0-formula",
  "kind": "structure",
  "name": "Level0Formula",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 142,
  "source_line_end": 146,
  "registry_ids": [
    "IV.D317"
  ],
  "related_registry_items": [
    {
      "id": "IV.D317",
      "title": "Level 0 Formula --- IV.D47",
      "url": "/registry/object/IV.D317/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L142-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L142-L146",
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

- Module: [TauLib.BookIV.MassDerivation.ElectronMass](/verify/taulib/docs/book-iv-mass-derivation-electron-mass/)
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L142-L146)
- Source range: L142-L146
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D317` — Level 0 Formula --- IV.D47

## Immediate Comment / Docstring

```lean
/-- [IV.D317] Level 0: R₀ = ι_τ^{-7} − √3·ι_τ^{-2}. -/
```

## Source Excerpt

```lean
structure Level0Formula where
  bulk_exp : Int := -7
  correction_exp : Int := -2
  accuracy_exact : String := "7.7 ppm"
  deriving Repr
```
