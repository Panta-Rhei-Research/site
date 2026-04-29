---
{
  "projection_kind": "taulib_declaration",
  "title": "BHBasinLawCode",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/bhbasin-law-code/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::BHBasinLawCode",
  "declaration_slug": "bhbasin-law-code",
  "kind": "structure",
  "name": "BHBasinLawCode",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 242,
  "source_line_end": 249,
  "registry_ids": [
    "VII.L01"
  ],
  "related_registry_items": [
    {
      "id": "VII.L01",
      "title": "BH Basin Law-Code",
      "url": "/registry/object/VII.L01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L242-L249",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L242-L249",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L242-L249)
- Source range: L242-L249
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.L01` — BH Basin Law-Code

## Immediate Comment / Docstring

```lean
/-- [VII.L01] BH Basin Law-Code: black-hole basin is canonical E₃ carrier
    satisfying SelfDesc². Internal law-code includes description of
    boundary conditions. Constructive witness for E₃ non-emptiness. -/
```

## Source Excerpt

```lean
structure BHBasinLawCode where
  /-- SelfDesc satisfied: code Λ describes itself. -/
  selfdesc : Bool := true
  /-- SelfDesc²: holonomy structure includes representation of holonomy-as-holonomy. -/
  selfdesc_squared : Bool := true
  /-- Canonical: unique minimal carrier at E₃. -/
  canonical : Bool := true
  deriving Repr
```
