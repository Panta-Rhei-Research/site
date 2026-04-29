---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_functional",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/defect-functional/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::defect_functional",
  "declaration_slug": "defect-functional",
  "kind": "def",
  "name": "defect_functional",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 165,
  "source_line_end": 175,
  "registry_ids": [
    "III.D39"
  ],
  "related_registry_items": [
    {
      "id": "III.D39",
      "title": "Defect Functional Δ",
      "url": "/registry/object/III.D39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L165-L175",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.FluidData",
        "url": "/verify/taulib/docs/book-iii-physics-fluid-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L165-L175",
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

- Module: [TauLib.BookIII.Physics.FluidData](/verify/taulib/docs/book-iii-physics-fluid-data/)
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L165-L175)
- Source range: L165-L175
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D39` — Defect Functional Δ

## Immediate Comment / Docstring

```lean
/-- [III.D39] Defect functional at primorial level k: maximum defect
    over all cylinders. -/
```

## Source Excerpt

```lean
def defect_functional (k : TauIdx) : TauIdx :=
  let pk := primorial k
  if pk == 0 then 0
  else go 0 pk k 0
where
  go (x pk k max_def : Nat) : TauIdx :=
    if x >= pk then max_def
    else
      let d := cylinder_defect x k
      let new_max := if d > max_def then d else max_def
      go (x + 1) pk k new_max
```
