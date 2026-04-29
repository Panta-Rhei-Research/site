---
{
  "projection_kind": "taulib_declaration",
  "title": "Tracelessness",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/tracelessness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::Tracelessness",
  "declaration_slug": "tracelessness",
  "kind": "structure",
  "name": "Tracelessness",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 195,
  "source_line_end": 202,
  "registry_ids": [
    "IV.P92"
  ],
  "related_registry_items": [
    {
      "id": "IV.P92",
      "title": "Tracelessness from Color-Neutral Vacuum",
      "url": "/registry/object/IV.P92/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L195-L202",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.ColorHolonomy",
        "url": "/verify/taulib/docs/book-iv-strong-color-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L195-L202",
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

- Module: [TauLib.BookIV.Strong.ColorHolonomy](/verify/taulib/docs/book-iv-strong-color-holonomy/)
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L195-L202)
- Source range: L195-L202
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P92` — Tracelessness from Color-Neutral Vacuum

## Immediate Comment / Docstring

```lean
/-- [IV.P92] The strong vacuum is color-neutral (total holonomy 0 mod 3),
    so only det U = 1 transformations preserve it: U(3) -> SU(3). -/
```

## Source Excerpt

```lean
structure Tracelessness where
  /-- Vacuum is color-neutral. -/
  vacuum_neutral : Bool := true
  /-- Tracelessness condition: det = 1. -/
  traceless : Bool := true
  /-- Reduces U(3) to SU(3). -/
  u3_to_su3 : Bool := true
  deriving Repr
```
