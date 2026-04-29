---
{
  "projection_kind": "taulib_declaration",
  "title": "fluid_data_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-fluid-data/fluid-data-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::fluid_data_check",
  "declaration_slug": "fluid-data-check",
  "kind": "def",
  "name": "fluid_data_check",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/verify/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 60,
  "source_line_end": 79,
  "registry_ids": [
    "III.D36"
  ],
  "related_registry_items": [
    {
      "id": "III.D36",
      "title": "τ-Admissible Fluid Data",
      "url": "/registry/object/III.D36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L60-L79",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L60-L79",
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
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L60-L79)
- Source range: L60-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D36` — τ-Admissible Fluid Data

## Immediate Comment / Docstring

```lean
/-- [III.D36] τ-admissibility check: each cylinder value has a valid BNF
    decomposition at this depth. -/
```

## Source Excerpt

```lean
def fluid_data_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let _fd := make_fluid_data k
      let pk := primorial k
      let valid := if pk > 0 then
        go_inner 0 pk k
      else true
      valid && go (k + 1) (fuel - 1)
  termination_by fuel
  go_inner (x pk k : Nat) : Bool :=
    if x >= pk then true
    else
      let nf := boundary_normal_form x k
      let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
      sum == x && go_inner (x + 1) pk k
```
