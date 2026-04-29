---
{
  "projection_kind": "taulib_declaration",
  "title": "lobes_exhaustive_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-boundary-minimality/lobes-exhaustive-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.BoundaryMinimality`.",
  "declaration_id": "TauLib.BookII.Topology.BoundaryMinimality::lobes_exhaustive_check",
  "declaration_slug": "lobes-exhaustive-check",
  "kind": "def",
  "name": "lobes_exhaustive_check",
  "module_name": "TauLib.BookII.Topology.BoundaryMinimality",
  "module_url": "/verify/taulib/docs/book-ii-topology-boundary-minimality/",
  "source_line_start": 82,
  "source_line_end": 95,
  "registry_ids": [
    "II.P05"
  ],
  "related_registry_items": [
    {
      "id": "II.P05",
      "title": "Lobes as Clopen Sets",
      "url": "/registry/object/II.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L82-L95",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.BoundaryMinimality",
        "url": "/verify/taulib/docs/book-ii-topology-boundary-minimality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L82-L95",
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

- Module: [TauLib.BookII.Topology.BoundaryMinimality](/verify/taulib/docs/book-ii-topology-boundary-minimality/)
- Source path: [`TauLib/BookII/Topology/BoundaryMinimality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L82-L95)
- Source range: L82-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P05` — Lobes as Clopen Sets

## Immediate Comment / Docstring

```lean
/-- [II.P05] Lobes are complementary: every point is B-dominant,
    C-dominant, or balanced (no other possibility). -/
```

## Source Excerpt

```lean
def lobes_exhaustive_check (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let _ := match p.fiber_dominance with
        | .b_dominant => true
        | .c_dominant => true
        | .balanced   => true
      go (x + 1) (fuel - 1)
  termination_by fuel
```
