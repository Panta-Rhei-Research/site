---
{
  "projection_kind": "taulib_declaration",
  "title": "horizon_topology",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/horizon-topology/",
  "summary_short": "`def` declaration in `TauLib.BookVI.CosmicLife.BHDist`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.BHDist::horizon_topology",
  "declaration_slug": "horizon-topology",
  "kind": "def",
  "name": "horizon_topology",
  "module_name": "TauLib.BookVI.CosmicLife.BHDist",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/",
  "source_line_start": 40,
  "source_line_end": 40,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L40-L40",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.BHDist",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-bhdist/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L40-L40",
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

- Module: [TauLib.BookVI.CosmicLife.BHDist](/verify/taulib/docs/book-vi-cosmic-life-bhdist/)
- Source path: [`TauLib/BookVI/CosmicLife/BHDist.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/BHDist.lean#L40-L40)
- Source range: L40-L40
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The BH horizon has T² topology (torus), NOT S² (sphere).
    Authority: V.T109 (BH Toroidal Topology, Book V Chapter 50).
    The two S¹ cycles generate the torus QNM spectrum (V.D234). -/
```

## Source Excerpt

```lean
def horizon_topology : Nat := 2  -- T² = 2-dimensional torus
```
