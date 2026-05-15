---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_penrose",
  "permalink": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/remark-penrose/",
  "summary_short": "`def` declaration in `TauLib.BookIV.ManyBody.FluidRegimes`.",
  "declaration_id": "TauLib.BookIV.ManyBody.FluidRegimes::remark_penrose",
  "declaration_slug": "remark-penrose",
  "kind": "def",
  "name": "remark_penrose",
  "module_name": "TauLib.BookIV.ManyBody.FluidRegimes",
  "module_url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/",
  "source_line_start": 313,
  "source_line_end": 315,
  "registry_ids": [
    "IV.R176"
  ],
  "related_registry_items": [
    {
      "id": "IV.R176",
      "title": "Penrose tilings on the torus",
      "url": "/registry/object/IV.R176/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L313-L315",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.FluidRegimes",
        "url": "/corpus/taulib/docs/book-iv-many-body-fluid-regimes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L313-L315",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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

- Module: [TauLib.BookIV.ManyBody.FluidRegimes](/corpus/taulib/docs/book-iv-many-body-fluid-regimes/)
- Source path: [`TauLib/BookIV/ManyBody/FluidRegimes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/FluidRegimes.lean#L313-L315)
- Source range: L313-L315
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `IV.R176` — Penrose tilings on the torus

## Immediate Comment / Docstring

```lean
/-- [IV.R176] (Metaphorical) Penrose tilings arise as a special case of
    incommensurate torus windings: the projection angle is arctan(w_gamma/w_eta).
    Scope: metaphorical (suggestive, not derived). -/
```

## Source Excerpt

```lean
def remark_penrose : String :=
  "[metaphorical] Penrose tilings from incommensurate torus windings; " ++
  "projection angle = arctan(w_gamma/w_eta)"
```
