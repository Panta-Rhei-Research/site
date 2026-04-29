---
{
  "projection_kind": "taulib_declaration",
  "title": "stabilized_germ",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/stabilized-germ/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::stabilized_germ",
  "declaration_slug": "stabilized-germ",
  "kind": "def",
  "name": "stabilized_germ",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 108,
  "source_line_end": 111,
  "registry_ids": [
    "III.D42"
  ],
  "related_registry_items": [
    {
      "id": "III.D42",
      "title": "Stabilized ω-Germ",
      "url": "/registry/object/III.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L108-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/verify/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L108-L111",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L108-L111)
- Source range: L108-L111
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D42` — Stabilized ω-Germ

## Immediate Comment / Docstring

```lean
/-- [III.D42] Stabilized germ: the BNF at the maximum available depth.
    In the finite tower, stabilization occurs at the top level. -/
```

## Source Excerpt

```lean
def stabilized_germ (x db : TauIdx) : BoundaryNF :=
  let pk := primorial db
  if pk == 0 then ⟨0, 0, 0, db⟩
  else boundary_normal_form (x % pk) db
```
