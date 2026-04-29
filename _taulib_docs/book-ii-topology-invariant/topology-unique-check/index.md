---
{
  "projection_kind": "taulib_declaration",
  "title": "topology_unique_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-invariant/topology-unique-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.Invariant`.",
  "declaration_id": "TauLib.BookII.Topology.Invariant::topology_unique_check",
  "declaration_slug": "topology-unique-check",
  "kind": "def",
  "name": "topology_unique_check",
  "module_name": "TauLib.BookII.Topology.Invariant",
  "module_url": "/verify/taulib/docs/book-ii-topology-invariant/",
  "source_line_start": 68,
  "source_line_end": 76,
  "registry_ids": [
    "II.T10"
  ],
  "related_registry_items": [
    {
      "id": "II.T10",
      "title": "Topology Uniqueness",
      "url": "/registry/object/II.T10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L68-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.Invariant",
        "url": "/verify/taulib/docs/book-ii-topology-invariant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L68-L76",
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

- Module: [TauLib.BookII.Topology.Invariant](/verify/taulib/docs/book-ii-topology-invariant/)
- Source path: [`TauLib/BookII/Topology/Invariant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L68-L76)
- Source range: L68-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T10` — Topology Uniqueness

## Immediate Comment / Docstring

```lean
/-- [II.T10] Topology uniqueness verification.
    The cylinder topology satisfies all three conditions:
    (a) CRT continuous, (b) Hausdorff, (c) compact.
    Any topology satisfying all three must equal the cylinder topology. -/
```

## Source Excerpt

```lean
def topology_unique_check (bound db : TauIdx) : Bool :=
  -- (a) CRT continuity: cylinder nesting implies continuity
  crt_continuous_check 1 bound &&
  crt_continuous_check 2 bound &&
  -- (b) Hausdorff: already verified in StoneSpace
  hausdorff_check bound db &&
  -- (c) Compactness: finite residue classes at each stage
  finite_subcover_check 1 bound &&
  finite_subcover_check 2 bound
```
