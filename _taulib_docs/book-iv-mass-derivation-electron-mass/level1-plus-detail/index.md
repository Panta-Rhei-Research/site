---
{
  "projection_kind": "taulib_declaration",
  "title": "Level1PlusDetail",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level1-plus-detail/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::Level1PlusDetail",
  "declaration_slug": "level1-plus-detail",
  "kind": "structure",
  "name": "Level1PlusDetail",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 170,
  "source_line_end": 177,
  "registry_ids": [
    "IV.D318"
  ],
  "related_registry_items": [
    {
      "id": "IV.D318",
      "title": "Level 1+ Formula --- IV.D48",
      "url": "/registry/object/IV.D318/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L170-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L170-L177",
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L170-L177)
- Source range: L170-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D318` — Level 1+ Formula --- IV.D48

## Immediate Comment / Docstring

```lean
/-- [IV.D318] Level 1+: R₁ = ι_τ^{-7} − (√3 + π³α²)·ι_τ^{-2}.
    At exact ι_τ: 0.025 ppm, m_e = 0.510998937 MeV, zero free params. -/
```

## Source Excerpt

```lean
structure Level1PlusDetail where
  bulk_exp : Int := -7
  correction_exp : Int := -2
  accuracy_exact : String := "0.025 ppm"
  electron_mass_MeV : String := "0.510998937 MeV"
  free_parameters : Nat := 0
  scope : String := "tau-effective"
  deriving Repr
```
