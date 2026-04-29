---
{
  "projection_kind": "taulib_declaration",
  "title": "SupernovaType",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/supernova-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::SupernovaType",
  "declaration_slug": "supernova-type",
  "kind": "inductive",
  "name": "SupernovaType",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 69,
  "source_line_end": 78,
  "registry_ids": [
    "V.D126"
  ],
  "related_registry_items": [
    {
      "id": "V.D126",
      "title": "Topological Channel --- V.D59",
      "url": "/registry/object/V.D126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L69-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L69-L78",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L69-L78)
- Source range: L69-L78
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D126` — Topological Channel --- V.D59

## Immediate Comment / Docstring

```lean
/-- [V.D126] Supernova type classification. -/
```

## Source Excerpt

```lean
inductive SupernovaType where
  /-- Type Ia: thermonuclear white dwarf explosion. -/
  | TypeIa
  /-- Type II: core collapse of massive star with H envelope. -/
  | TypeII
  /-- Type Ib: core collapse, H-stripped. -/
  | TypeIb
  /-- Type Ic: core collapse, H and He stripped. -/
  | TypeIc
  deriving Repr, DecidableEq, BEq
```
