---
{
  "projection_kind": "taulib_declaration",
  "title": "CouplingEntry",
  "permalink": "/corpus/taulib/docs/book-iv-arena-five-sectors/coupling-entry/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::CouplingEntry",
  "declaration_slug": "coupling-entry",
  "kind": "structure",
  "name": "CouplingEntry",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/corpus/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 59,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D265"
  ],
  "related_registry_items": [
    {
      "id": "IV.D265",
      "title": "Coupling Ledger",
      "url": "/registry/object/IV.D265/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L59-L69",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L59-L69",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/corpus/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L59-L69)
- Source range: L59-L69
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.D265` — Coupling Ledger

## Immediate Comment / Docstring

```lean
/-- [IV.D265] A coupling entry in the ledger: self or cross coupling. -/
```

## Source Excerpt

```lean
structure CouplingEntry where
  /-- Source sector. -/
  sector1 : Sector
  /-- Target sector (same for self-coupling). -/
  sector2 : Sector
  /-- Coupling numerator (scaled). -/
  numer : Nat
  /-- Coupling denominator (scaled). -/
  denom : Nat
  denom_pos : denom > 0
  deriving Repr
```
