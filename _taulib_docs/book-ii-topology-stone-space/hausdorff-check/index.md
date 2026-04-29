---
{
  "projection_kind": "taulib_declaration",
  "title": "hausdorff_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-stone-space/hausdorff-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.StoneSpace`.",
  "declaration_id": "TauLib.BookII.Topology.StoneSpace::hausdorff_check",
  "declaration_slug": "hausdorff-check",
  "kind": "def",
  "name": "hausdorff_check",
  "module_name": "TauLib.BookII.Topology.StoneSpace",
  "module_url": "/verify/taulib/docs/book-ii-topology-stone-space/",
  "source_line_start": 41,
  "source_line_end": 55,
  "registry_ids": [
    "II.T08"
  ],
  "related_registry_items": [
    {
      "id": "II.T08",
      "title": "Hausdorff Property",
      "url": "/registry/object/II.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L41-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.StoneSpace",
        "url": "/verify/taulib/docs/book-ii-topology-stone-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L41-L55",
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

- Module: [TauLib.BookII.Topology.StoneSpace](/verify/taulib/docs/book-ii-topology-stone-space/)
- Source path: [`TauLib/BookII/Topology/StoneSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L41-L55)
- Source range: L41-L55
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T08` — Hausdorff Property

## Immediate Comment / Docstring

```lean
/-- [II.T08] Hausdorff: distinct points have disjoint cylinder
    neighborhoods. For x ≠ y with δ(x,y) = k, the cylinders
    C_{k+1}(x) and C_{k+1}(y) are disjoint.
    Check: for all x ≠ y, find separating stage. -/
```

## Source Excerpt

```lean
def hausdorff_check (bound db : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      -- x = y trivially separated; x ≠ y needs separating stage
      let ok := x == y || (
        let k := disagree_depth x y db
        k < db + 1 &&  -- they actually disagree somewhere
        !cylinder_mem (k + 1) x y)  -- disjoint at stage k+1
      ok && go x (y + 1) (fuel - 1)
  termination_by fuel
```
