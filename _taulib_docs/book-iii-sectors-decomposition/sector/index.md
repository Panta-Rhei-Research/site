---
{
  "projection_kind": "taulib_declaration",
  "title": "Sector",
  "permalink": "/verify/taulib/docs/book-iii-sectors-decomposition/sector/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Sectors.Decomposition`.",
  "declaration_id": "TauLib.BookIII.Sectors.Decomposition::Sector",
  "declaration_slug": "sector",
  "kind": "inductive",
  "name": "Sector",
  "module_name": "TauLib.BookIII.Sectors.Decomposition",
  "module_url": "/verify/taulib/docs/book-iii-sectors-decomposition/",
  "source_line_start": 40,
  "source_line_end": 46,
  "registry_ids": [
    "III.D13"
  ],
  "related_registry_items": [
    {
      "id": "III.D13",
      "title": "4+1 Sector Decomposition",
      "url": "/registry/object/III.D13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L40-L46",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.Decomposition",
        "url": "/verify/taulib/docs/book-iii-sectors-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L40-L46",
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

- Module: [TauLib.BookIII.Sectors.Decomposition](/verify/taulib/docs/book-iii-sectors-decomposition/)
- Source path: [`TauLib/BookIII/Sectors/Decomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/Decomposition.lean#L40-L46)
- Source range: L40-L46
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `III.D13` — 4+1 Sector Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.D13] The five sectors induced by the ABCD decomposition.
    Four primitive sectors (one per generator) plus one coupling sector. -/
```

## Source Excerpt

```lean
inductive Sector where
  | D : Sector  -- α-generator, radial/gravity
  | A : Sector  -- π-generator, weak/gauge
  | B : Sector  -- γ-generator, electromagnetic
  | C : Sector  -- η-generator, strong
  | Omega : Sector  -- ω-coupling, Higgs/mass
  deriving Repr, DecidableEq, BEq, Inhabited
```
