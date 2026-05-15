---
{
  "projection_kind": "taulib_declaration",
  "title": "lobe_distribution",
  "permalink": "/corpus/taulib/docs/book-ii-topology-boundary-minimality/lobe-distribution/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.BoundaryMinimality`.",
  "declaration_id": "TauLib.BookII.Topology.BoundaryMinimality::lobe_distribution",
  "declaration_slug": "lobe-distribution",
  "kind": "def",
  "name": "lobe_distribution",
  "module_name": "TauLib.BookII.Topology.BoundaryMinimality",
  "module_url": "/corpus/taulib/docs/book-ii-topology-boundary-minimality/",
  "source_line_start": 63,
  "source_line_end": 74,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L63-L74",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.BoundaryMinimality",
        "url": "/corpus/taulib/docs/book-ii-topology-boundary-minimality/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L63-L74",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookII.Topology.BoundaryMinimality](/corpus/taulib/docs/book-ii-topology-boundary-minimality/)
- Source path: [`TauLib/BookII/Topology/BoundaryMinimality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L63-L74)
- Source range: L63-L74
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Count B-dominant, C-dominant, and balanced points in range. -/
```

## Source Excerpt

```lean
def lobe_distribution (bound : TauIdx) :
    Nat × Nat × Nat :=
  go 2 (bound + 1) 0 0 0
where
  go (x fuel b_ct c_ct bal : Nat) : Nat × Nat × Nat :=
    if fuel = 0 then (b_ct, c_ct, bal)
    else if x > bound then (b_ct, c_ct, bal)
    else match lobe_class x with
      | .b_dominant => go (x + 1) (fuel - 1) (b_ct + 1) c_ct bal
      | .c_dominant => go (x + 1) (fuel - 1) b_ct (c_ct + 1) bal
      | .balanced   => go (x + 1) (fuel - 1) b_ct c_ct (bal + 1)
  termination_by fuel
```
