---
{
  "projection_kind": "taulib_declaration",
  "title": "totally_disconnected_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-stone-space/totally-disconnected-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.StoneSpace`.",
  "declaration_id": "TauLib.BookII.Topology.StoneSpace::totally_disconnected_check",
  "declaration_slug": "totally-disconnected-check",
  "kind": "def",
  "name": "totally_disconnected_check",
  "module_name": "TauLib.BookII.Topology.StoneSpace",
  "module_url": "/verify/taulib/docs/book-ii-topology-stone-space/",
  "source_line_start": 69,
  "source_line_end": 81,
  "registry_ids": [
    "II.T09"
  ],
  "related_registry_items": [
    {
      "id": "II.T09",
      "title": "Total Disconnectedness",
      "url": "/registry/object/II.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L69-L81",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L69-L81",
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
- Source path: [`TauLib/BookII/Topology/StoneSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L69-L81)
- Source range: L69-L81
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T09` — Total Disconnectedness

## Immediate Comment / Docstring

```lean
/-- [II.T09] Total disconnectedness: for x ≠ y, there exists a
    clopen set containing x but not y (the separating cylinder).
    Check: for all x ≠ y, verify the separating cylinder works. -/
```

## Source Excerpt

```lean
def totally_disconnected_check (bound db : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      let ok := x == y || (
        let k := separating_stage x y db
        cylinder_mem k x x && !cylinder_mem k x y)
      ok && go x (y + 1) (fuel - 1)
  termination_by fuel
```
