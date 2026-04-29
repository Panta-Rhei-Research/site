---
{
  "projection_kind": "taulib_declaration",
  "title": "radial_solenoidal_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-dimension-four/radial-solenoidal-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.DimensionFour`.",
  "declaration_id": "TauLib.BookII.Topology.DimensionFour::radial_solenoidal_check",
  "declaration_slug": "radial-solenoidal-check",
  "kind": "def",
  "name": "radial_solenoidal_check",
  "module_name": "TauLib.BookII.Topology.DimensionFour",
  "module_url": "/verify/taulib/docs/book-ii-topology-dimension-four/",
  "source_line_start": 101,
  "source_line_end": 113,
  "registry_ids": [
    "II.D16"
  ],
  "related_registry_items": [
    {
      "id": "II.D16",
      "title": "Radial-Solenoidal Split",
      "url": "/registry/object/II.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L101-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.DimensionFour",
        "url": "/verify/taulib/docs/book-ii-topology-dimension-four/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L101-L113",
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

- Module: [TauLib.BookII.Topology.DimensionFour](/verify/taulib/docs/book-ii-topology-dimension-four/)
- Source path: [`TauLib/BookII/Topology/DimensionFour.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L101-L113)
- Source range: L101-L113
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D16` — Radial-Solenoidal Split

## Immediate Comment / Docstring

```lean
/-- [II.D16] The 1+3 split: D is radial (remainder after extraction),
    A,B,C are solenoidal (tower features).

    Asymmetry evidence:
    - D ranges over [0, M_k) (super-exponential growth)
    - A,B,C bounded by prime at each stage
    - Constraint C3 couples D to A (not conversely) -/
```

## Source Excerpt

```lean
def radial_solenoidal_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      -- D can be large (remainder grows); A is always prime or 1
      let d_radial := constraint_C1 p.a  -- A must be prime/1 (solenoidal)
      let d_coupled := constraint_C3 p.d p.a  -- D coupled to A (radial)
      d_radial && d_coupled && go (x + 1) (fuel - 1)
  termination_by fuel
```
