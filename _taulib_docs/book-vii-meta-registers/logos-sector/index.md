---
{
  "projection_kind": "taulib_declaration",
  "title": "LogosSector",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/logos-sector/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::LogosSector",
  "declaration_slug": "logos-sector",
  "kind": "structure",
  "name": "LogosSector",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 293,
  "source_line_end": 300,
  "registry_ids": [
    "VII.D11"
  ],
  "related_registry_items": [
    {
      "id": "VII.D11",
      "title": "Logos Sector S_L",
      "url": "/registry/object/VII.D11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L293-L300",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L293-L300",
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
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L293-L300)
- Source range: L293-L300
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D11` — Logos Sector S_L

## Immediate Comment / Docstring

```lean
/-- [VII.D11] Logos Sector S_L: mixed sector where Reg_D and Reg_C coincide.
    Universal property: unique locus where proof-validity = stance-stability. -/
```

## Source Excerpt

```lean
structure LogosSector where
  id : SectorId
  id_eq : id = .sl
  /-- D-C coincidence: proof-validity = stance-stability. -/
  dc_coincidence : Bool := true
  /-- Unique crossing mediator. -/
  unique_mediator : Bool := true
  deriving Repr
```
