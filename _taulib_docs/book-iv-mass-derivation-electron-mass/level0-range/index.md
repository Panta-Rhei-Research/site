---
{
  "projection_kind": "taulib_declaration",
  "title": "level0_range",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/level0-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::level0_range",
  "declaration_slug": "level0-range",
  "kind": "theorem",
  "name": "level0_range",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 151,
  "source_line_end": 156,
  "registry_ids": [
    "IV.T119"
  ],
  "related_registry_items": [
    {
      "id": "IV.T119",
      "title": "Level 0 Range --- IV.T14",
      "url": "/registry/object/IV.T119/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L151-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L151-L156",
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L151-L156)
- Source range: L151-L156
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T119` — Level 0 Range --- IV.T14

## Immediate Comment / Docstring

```lean
/-- [IV.T119] R₀ ∈ (1837, 1840) with 6-digit ι_τ. -/
```

## Source Excerpt

```lean
theorem level0_range :
    bulk_numer * correction0_denom >
    correction0_numer * bulk_denom + 1837 * bulk_denom * correction0_denom ∧
    bulk_numer * correction0_denom <
    correction0_numer * bulk_denom + 1840 * bulk_denom * correction0_denom :=
  r0_in_range
```
