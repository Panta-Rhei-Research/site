---
{
  "projection_kind": "taulib_declaration",
  "title": "PresentSurface",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/present-surface/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::PresentSurface",
  "declaration_slug": "present-surface",
  "kind": "structure",
  "name": "PresentSurface",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 232,
  "source_line_end": 241,
  "registry_ids": [
    "V.D59"
  ],
  "related_registry_items": [
    {
      "id": "V.D59",
      "title": "Present surface",
      "url": "/registry/object/V.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L232-L241",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L232-L241",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L232-L241)
- Source range: L232-L241
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D59` — Present surface

## Immediate Comment / Docstring

```lean
/-- [V.D59] Present surface: the now-hypersurface at NF iteration
    depth k.

    The present surface separates resolved (past, steps 0..k) from
    unresolved (future, steps k+1..) boundary data. It advances
    with each NF iteration step.

    This is the τ-native notion of "now" — not a coordinate choice
    but a resolution boundary in the iteration. -/
```

## Source Excerpt

```lean
structure PresentSurface where
  /-- NF iteration depth defining this surface. -/
  iteration_depth : Nat
  /-- Must have at least one resolved step. -/
  depth_pos : iteration_depth > 0
  /-- Dimension of the surface (= 3 for spatial slicing). -/
  dimension : Nat := 3
  /-- Surface is 3-dimensional. -/
  dim_is_three : dimension = 3 := by rfl
  deriving Repr
```
