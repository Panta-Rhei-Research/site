---
{
  "projection_kind": "taulib_declaration",
  "title": "BulkTerm",
  "permalink": "/corpus/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-term/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::BulkTerm",
  "declaration_slug": "bulk-term",
  "kind": "structure",
  "name": "BulkTerm",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/corpus/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 108,
  "source_line_end": 113,
  "registry_ids": [
    "IV.D316"
  ],
  "related_registry_items": [
    {
      "id": "IV.D316",
      "title": "Mass Ratio Bulk Term --- IV.D46",
      "url": "/registry/object/IV.D316/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L108-L113",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L108-L113",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L108-L113)
- Source range: L108-L113
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D316` — Mass Ratio Bulk Term --- IV.D46

## Immediate Comment / Docstring

```lean
/-- [IV.D316] Bulk term R_bulk = ι_τ^{-7}. Wraps MassRatioFormula. -/
```

## Source Excerpt

```lean
structure BulkTerm where
  numer : Nat
  denom : Nat
  denom_pos : denom > 0
  exponent : Int := -7
  deriving Repr
```
