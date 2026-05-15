---
{
  "projection_kind": "taulib_declaration",
  "title": "Gen5",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-mode-census/gen5/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Sectors.ModeCensus`.",
  "declaration_id": "TauLib.BookIV.Sectors.ModeCensus::Gen5",
  "declaration_slug": "gen5",
  "kind": "inductive",
  "name": "Gen5",
  "module_name": "TauLib.BookIV.Sectors.ModeCensus",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-mode-census/",
  "source_line_start": 45,
  "source_line_end": 51,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L45-L51",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.ModeCensus",
        "url": "/corpus/taulib/docs/book-iv-sectors-mode-census/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L45-L51",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Sectors.ModeCensus](/corpus/taulib/docs/book-iv-sectors-mode-census/)
- Source path: [`TauLib/BookIV/Sectors/ModeCensus.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/ModeCensus.lean#L45-L51)
- Source range: L45-L51
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 5 generators of Category τ (local copy for census). -/
```

## Source Excerpt

```lean
inductive Gen5 where
  | alpha  -- gravity (D-sector)
  | pi_    -- weak (A-sector)
  | gamma  -- EM (B-sector)
  | eta    -- strong (C-sector)
  | omega  -- Higgs/mass (B∩C crossing)
  deriving Repr, DecidableEq, BEq
```
