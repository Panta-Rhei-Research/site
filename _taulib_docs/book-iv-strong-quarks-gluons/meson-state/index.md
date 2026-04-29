---
{
  "projection_kind": "taulib_declaration",
  "title": "MesonState",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/meson-state/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::MesonState",
  "declaration_slug": "meson-state",
  "kind": "structure",
  "name": "MesonState",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 304,
  "source_line_end": 315,
  "registry_ids": [
    "IV.D190"
  ],
  "related_registry_items": [
    {
      "id": "IV.D190",
      "title": "Meson state",
      "url": "/registry/object/IV.D190/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L304-L315",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.QuarksGluons",
        "url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L304-L315",
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

- Module: [TauLib.BookIV.Strong.QuarksGluons](/verify/taulib/docs/book-iv-strong-quarks-gluons/)
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L304-L315)
- Source range: L304-L315
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D190` — Meson state

## Immediate Comment / Docstring

```lean
/-- [IV.D190] A meson: composite |q qbar> with total color 0 mod 3.
    Minimal mesonic singlet: one quark + one antiquark. -/
```

## Source Excerpt

```lean
structure MesonState where
  /-- Quark flavor. -/
  quark_flavor : String
  /-- Antiquark flavor. -/
  antiquark_flavor : String
  /-- Quark color class. -/
  quark_color : Nat
  /-- Antiquark color class (must complement quark). -/
  antiquark_color : Nat
  /-- Color singlet condition. -/
  is_singlet : Bool
  deriving Repr
```
