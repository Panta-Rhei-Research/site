---
{
  "projection_kind": "taulib_declaration",
  "title": "spine_address_path",
  "permalink": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/spine-address-path/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.CoherenceConnectivity`.",
  "declaration_id": "TauLib.BookII.Topology.CoherenceConnectivity::spine_address_path",
  "declaration_slug": "spine-address-path",
  "kind": "def",
  "name": "spine_address_path",
  "module_name": "TauLib.BookII.Topology.CoherenceConnectivity",
  "module_url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/",
  "source_line_start": 108,
  "source_line_end": 109,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L108-L109",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.CoherenceConnectivity",
        "url": "/verify/taulib/docs/book-ii-topology-coherence-connectivity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L108-L109",
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

- Module: [TauLib.BookII.Topology.CoherenceConnectivity](/verify/taulib/docs/book-ii-topology-coherence-connectivity/)
- Source path: [`TauLib/BookII/Topology/CoherenceConnectivity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/CoherenceConnectivity.lean#L108-L109)
- Source range: L108-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Spine address path from X to Y: total peel steps via α₁. -/
```

## Source Excerpt

```lean
def spine_address_path (x y : TauIdx) : TauIdx :=
  spine_address_length x + spine_address_length y
```
