---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_minimal_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-boundary-minimality/boundary-minimal-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.BoundaryMinimality`.",
  "declaration_id": "TauLib.BookII.Topology.BoundaryMinimality::boundary_minimal_check",
  "declaration_slug": "boundary-minimal-check",
  "kind": "def",
  "name": "boundary_minimal_check",
  "module_name": "TauLib.BookII.Topology.BoundaryMinimality",
  "module_url": "/verify/taulib/docs/book-ii-topology-boundary-minimality/",
  "source_line_start": 121,
  "source_line_end": 132,
  "registry_ids": [
    "II.T12"
  ],
  "related_registry_items": [
    {
      "id": "II.T12",
      "title": "Boundary Minimality",
      "url": "/registry/object/II.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L121-L132",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L121-L132",
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
- Source path: [`TauLib/BookII/Topology/BoundaryMinimality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L121-L132)
- Source range: L121-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T12` — Boundary Minimality

## Immediate Comment / Docstring

```lean
/-- [II.T12] Boundary minimality evidence:
    Two independent channels (B and C) cannot be collapsed to one.
    Check: there exist points varying B with C fixed, and vice versa. -/
```

## Source Excerpt

```lean
def boundary_minimal_check : Bool :=
  -- B varies independently: 2=(2,1,1,1) and 8=(2,3,1,1) differ in B only
  let p2 := from_tau_idx 2
  let p8 := from_tau_idx 8
  (p2.b != p8.b && p2.a == p8.a && p2.c == p8.c) &&
  -- C varies independently: 8=(2,3,1,1) and 64=(2,3,2,1) differ in C only
  let p64 := from_tau_idx 64
  (p8.c != p64.c && p8.a == p64.a && p8.b == p64.b) &&
  -- Both channels survive to boundary:
  -- B-dominant and C-dominant points both exist
  let (b_ct, c_ct, _) := lobe_distribution 100
  b_ct > 0 && c_ct > 0
```
