---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_assignment_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/cylinder-assignment-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::cylinder_assignment_check",
  "declaration_slug": "cylinder-assignment-check",
  "kind": "def",
  "name": "cylinder_assignment_check",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 94,
  "source_line_end": 108,
  "registry_ids": [
    "III.D37"
  ],
  "related_registry_items": [
    {
      "id": "III.D37",
      "title": "Clopen Cylinder Domain",
      "url": "/registry/object/III.D37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L94-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L94-L108",
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
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L94-L108)
- Source range: L94-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D37` — Clopen Cylinder Domain

## Immediate Comment / Docstring

```lean
/-- [III.D37] Cylinder assignment check: every cylinder has a valid
    BNF that sums correctly. -/
```

## Source Excerpt

```lean
def cylinder_assignment_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let nf := cylinder_assignment x k
      let pk := primorial k
      let ok := if pk > 0 then
        (nf.b_part + nf.c_part + nf.x_part) % pk == x % pk
      else true
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
