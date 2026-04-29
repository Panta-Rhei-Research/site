---
{
  "projection_kind": "taulib_declaration",
  "title": "is_color_charged",
  "permalink": "/verify/taulib/docs/book-iv-strong-color-holonomy/is-color-charged/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Strong.ColorHolonomy`.",
  "declaration_id": "TauLib.BookIV.Strong.ColorHolonomy::is_color_charged",
  "declaration_slug": "is-color-charged",
  "kind": "def",
  "name": "is_color_charged",
  "module_name": "TauLib.BookIV.Strong.ColorHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-strong-color-holonomy/",
  "source_line_start": 162,
  "source_line_end": 163,
  "registry_ids": [
    "IV.P90"
  ],
  "related_registry_items": [
    {
      "id": "IV.P90",
      "title": "Color-Charged Modes Have n \\neq 0 \\pmod{3",
      "url": "/registry/object/IV.P90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L162-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L162-L163",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Strong/ColorHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/ColorHolonomy.lean#L162-L163)
- Source range: L162-L163
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P90` — Color-Charged Modes Have n \neq 0 \pmod{3

## Immediate Comment / Docstring

```lean
/-- [IV.P90] A mode carries nontrivial color iff n not equiv 0 mod 3. -/
```

## Source Excerpt

```lean
def is_color_charged (eta_winding : Nat) : Bool :=
  eta_winding % 3 != 0
```
