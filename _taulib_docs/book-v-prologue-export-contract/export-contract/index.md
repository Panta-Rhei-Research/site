---
{
  "projection_kind": "taulib_declaration",
  "title": "ExportContract",
  "permalink": "/verify/taulib/docs/book-v-prologue-export-contract/export-contract/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Prologue.ExportContract`.",
  "declaration_id": "TauLib.BookV.Prologue.ExportContract::ExportContract",
  "declaration_slug": "export-contract",
  "kind": "structure",
  "name": "ExportContract",
  "module_name": "TauLib.BookV.Prologue.ExportContract",
  "module_url": "/verify/taulib/docs/book-v-prologue-export-contract/",
  "source_line_start": 71,
  "source_line_end": 88,
  "registry_ids": [
    "V.D12"
  ],
  "related_registry_items": [
    {
      "id": "V.D12",
      "title": "Book~IV to Book~V Export Contract",
      "url": "/registry/object/V.D12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L71-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Prologue.ExportContract",
        "url": "/verify/taulib/docs/book-v-prologue-export-contract/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L71-L88",
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

- Module: [TauLib.BookV.Prologue.ExportContract](/verify/taulib/docs/book-v-prologue-export-contract/)
- Source path: [`TauLib/BookV/Prologue/ExportContract.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Prologue/ExportContract.lean#L71-L88)
- Source range: L71-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D12` — Book~IV to Book~V Export Contract

## Immediate Comment / Docstring

```lean
/-- [V.D12] The 10-item export contract from Book IV (Microcosm) to
    Book V (Macrocosm). Each item is a structural entity fully
    earned at E₁ and handed off hermetically.

    Items: arena, sectors, couplings, carrier types, primary invariants,
    defect bundle, mass-energy, Planck character, defect functional,
    mass ratio R. -/
```

## Source Excerpt

```lean
structure ExportContract where
  /-- Number of items in the contract. -/
  item_count : Nat
  /-- Must be exactly 10. -/
  count_eq : item_count = 10
  /-- Number of sector items. -/
  sector_count : Nat
  /-- 5 sectors. -/
  sector_eq : sector_count = 5
  /-- Number of coupling items. -/
  coupling_count : Nat
  /-- 5 self-couplings (cross-couplings derived). -/
  coupling_eq : coupling_count = 5
  /-- Number of primary invariants. -/
  invariant_count : Nat
  /-- 5 primary invariants. -/
  invariant_eq : invariant_count = 5
  deriving Repr
```
