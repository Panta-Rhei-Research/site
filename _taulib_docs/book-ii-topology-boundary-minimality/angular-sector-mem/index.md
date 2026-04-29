---
{
  "projection_kind": "taulib_declaration",
  "title": "angular_sector_mem",
  "permalink": "/verify/taulib/docs/book-ii-topology-boundary-minimality/angular-sector-mem/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.BoundaryMinimality`.",
  "declaration_id": "TauLib.BookII.Topology.BoundaryMinimality::angular_sector_mem",
  "declaration_slug": "angular-sector-mem",
  "kind": "def",
  "name": "angular_sector_mem",
  "module_name": "TauLib.BookII.Topology.BoundaryMinimality",
  "module_url": "/verify/taulib/docs/book-ii-topology-boundary-minimality/",
  "source_line_start": 50,
  "source_line_end": 51,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L50-L51",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L50-L51",
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
- Source path: [`TauLib/BookII/Topology/BoundaryMinimality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/BoundaryMinimality.lean#L50-L51)
- Source range: L50-L51
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Combined angular sector membership. -/
```

## Source Excerpt

```lean
def angular_sector_mem (k b_val c_val x : TauIdx) : Bool :=
  angular_b_sector x k == b_val && angular_c_sector x k == c_val
```
