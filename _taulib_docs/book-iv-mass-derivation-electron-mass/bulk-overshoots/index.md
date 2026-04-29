---
{
  "projection_kind": "taulib_declaration",
  "title": "bulk_overshoots",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/bulk-overshoots/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::bulk_overshoots",
  "declaration_slug": "bulk-overshoots",
  "kind": "theorem",
  "name": "bulk_overshoots",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 128,
  "source_line_end": 130,
  "registry_ids": [
    "IV.T118"
  ],
  "related_registry_items": [
    {
      "id": "IV.T118",
      "title": "Bulk Overshoots --- IV.T13",
      "url": "/registry/object/IV.T118/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L128-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L128-L130",
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L128-L130)
- Source range: L128-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T118` — Bulk Overshoots --- IV.T13

## Immediate Comment / Docstring

```lean
/-- [IV.T118] ι_τ^{-7} overshoots R_CODATA (correction sign is correct). -/
```

## Source Excerpt

```lean
theorem bulk_overshoots :
    bulk_numer * si_mass_ratio.denom > si_mass_ratio.numer * bulk_denom :=
  bulk_overshoots_codata
```
