---
{
  "projection_kind": "taulib_declaration",
  "title": "ScopeDistribution",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/scope-distribution/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.ElectronMass`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.ElectronMass::ScopeDistribution",
  "declaration_slug": "scope-distribution",
  "kind": "structure",
  "name": "ScopeDistribution",
  "module_name": "TauLib.BookIV.MassDerivation.ElectronMass",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-electron-mass/",
  "source_line_start": 72,
  "source_line_end": 78,
  "registry_ids": [
    "IV.P172"
  ],
  "related_registry_items": [
    {
      "id": "IV.P172",
      "title": "All Links tau-Effective --- IV.P07",
      "url": "/registry/object/IV.P172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L72-L78",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L72-L78",
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
- Source path: [`TauLib/BookIV/MassDerivation/ElectronMass.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/ElectronMass.lean#L72-L78)
- Source range: L72-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P172` — All Links tau-Effective --- IV.P07

## Immediate Comment / Docstring

```lean
/-- [IV.P172] 3 established + 7 tau-effective + 0 conjectural. -/
```

## Source Excerpt

```lean
structure ScopeDistribution where
  established : Nat
  tau_effective : Nat
  conjectural : Nat
  total_eq : established + tau_effective + conjectural = 10
  no_conjectural : conjectural = 0
  deriving Repr
```
