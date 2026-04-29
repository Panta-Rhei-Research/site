---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutronNoDist",
  "permalink": "/verify/taulib/docs/book-vi-sectors-four-plus-one/neutron-no-dist/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Sectors.FourPlusOne`.",
  "declaration_id": "TauLib.BookVI.Sectors.FourPlusOne::NeutronNoDist",
  "declaration_slug": "neutron-no-dist",
  "kind": "structure",
  "name": "NeutronNoDist",
  "module_name": "TauLib.BookVI.Sectors.FourPlusOne",
  "module_url": "/verify/taulib/docs/book-vi-sectors-four-plus-one/",
  "source_line_start": 87,
  "source_line_end": 90,
  "registry_ids": [
    "VI.L05"
  ],
  "related_registry_items": [
    {
      "id": "VI.L05",
      "title": "Neutron NoDist",
      "url": "/registry/object/VI.L05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L87-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.FourPlusOne",
        "url": "/verify/taulib/docs/book-vi-sectors-four-plus-one/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L87-L90",
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

- Module: [TauLib.BookVI.Sectors.FourPlusOne](/verify/taulib/docs/book-vi-sectors-four-plus-one/)
- Source path: [`TauLib/BookVI/Sectors/FourPlusOne.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/FourPlusOne.lean#L87-L90)
- Source range: L87-L90
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L05` — Neutron NoDist

## Immediate Comment / Docstring

```lean
/-- [VI.L05] Neutron NoDist: free neutron fails 3/5 distinction conditions. -/
```

## Source Excerpt

```lean
structure NeutronNoDist where
  conditions_failed : Nat
  failed_eq : conditions_failed = 3
  deriving Repr
```
