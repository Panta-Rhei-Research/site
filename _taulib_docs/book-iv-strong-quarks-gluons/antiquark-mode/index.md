---
{
  "projection_kind": "taulib_declaration",
  "title": "AntiquarkMode",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/antiquark-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::AntiquarkMode",
  "declaration_slug": "antiquark-mode",
  "kind": "structure",
  "name": "AntiquarkMode",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 130,
  "source_line_end": 139,
  "registry_ids": [
    "IV.D188"
  ],
  "related_registry_items": [
    {
      "id": "IV.D188",
      "title": "Antiquark mode",
      "url": "/registry/object/IV.D188/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L130-L139",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L130-L139",
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
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L130-L139)
- Source range: L130-L139
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D188` — Antiquark mode

## Immediate Comment / Docstring

```lean
/-- [IV.D188] Antiquark: conjugate mode bar{chi}_{m,n} = chi_{-m,-n}
    with reversed color class and reversed electric charge. -/
```

## Source Excerpt

```lean
structure AntiquarkMode where
  /-- Reversed gamma-winding. -/
  gamma_winding : Int
  /-- Reversed eta-winding. -/
  eta_winding : Int
  /-- Anti-quark type (opposite of quark). -/
  anti_type : QuarkType
  /-- Generation (same as the quark). -/
  generation : Nat
  deriving Repr
```
