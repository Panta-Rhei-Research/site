---
{
  "projection_kind": "taulib_declaration",
  "title": "GluonVertices",
  "permalink": "/verify/taulib/docs/book-iv-strong-quarks-gluons/gluon-vertices/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.QuarksGluons`.",
  "declaration_id": "TauLib.BookIV.Strong.QuarksGluons::GluonVertices",
  "declaration_slug": "gluon-vertices",
  "kind": "structure",
  "name": "GluonVertices",
  "module_name": "TauLib.BookIV.Strong.QuarksGluons",
  "module_url": "/verify/taulib/docs/book-iv-strong-quarks-gluons/",
  "source_line_start": 241,
  "source_line_end": 248,
  "registry_ids": [
    "IV.P116"
  ],
  "related_registry_items": [
    {
      "id": "IV.P116",
      "title": "Gluon self-interaction vertices",
      "url": "/registry/object/IV.P116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L241-L248",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L241-L248",
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
- Source path: [`TauLib/BookIV/Strong/QuarksGluons.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/QuarksGluons.lean#L241-L248)
- Source range: L241-L248
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P116` — Gluon self-interaction vertices

## Immediate Comment / Docstring

```lean
/-- [IV.P116] Two self-interaction vertices from non-abelian field strength:
    - Three-gluon vertex: proportional to g_s f_{abc}
    - Four-gluon vertex: proportional to g_s^2 f_{abe} f_{cde}
    These produce jet events and are the structural origin of confinement. -/
```

## Source Excerpt

```lean
structure GluonVertices where
  /-- Three-gluon vertex (from [A_mu, A_nu] commutator). -/
  three_vertex : Bool := true
  /-- Four-gluon vertex (from [A,A]^2 term). -/
  four_vertex : Bool := true
  /-- Total self-interaction vertex types. -/
  vertex_types : Nat := 2
  deriving Repr
```
