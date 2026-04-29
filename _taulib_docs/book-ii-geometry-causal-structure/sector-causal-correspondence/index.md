---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_causal_correspondence",
  "permalink": "/verify/taulib/docs/book-ii-geometry-causal-structure/sector-causal-correspondence/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.CausalStructure`.",
  "declaration_id": "TauLib.BookII.Geometry.CausalStructure::sector_causal_correspondence",
  "declaration_slug": "sector-causal-correspondence",
  "kind": "def",
  "name": "sector_causal_correspondence",
  "module_name": "TauLib.BookII.Geometry.CausalStructure",
  "module_url": "/verify/taulib/docs/book-ii-geometry-causal-structure/",
  "source_line_start": 160,
  "source_line_end": 166,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L160-L166",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.CausalStructure",
        "url": "/verify/taulib/docs/book-ii-geometry-causal-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L160-L166",
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

- Module: [TauLib.BookII.Geometry.CausalStructure](/verify/taulib/docs/book-ii-geometry-causal-structure/)
- Source path: [`TauLib/BookII/Geometry/CausalStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/CausalStructure.lean#L160-L166)
- Source range: L160-L166
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The two null directions correspond to the two bipolar sectors.
    e₊-direction (B-channel): ξ = x+y = const → null
    e₋-direction (C-channel): ζ = x-y = const → null
    Sectors are the "light-cone edges" of the causal structure. -/
```

## Source Excerpt

```lean
def sector_causal_correspondence : Bool :=
  -- e₊ sector pair: (1, 0) → split-complex (1/2)(1+j) → displacement along (1,1) → null
  e_plus_null &&
  -- e₋ sector pair: (0, 1) → split-complex (1/2)(1-j) → displacement along (1,-1) → null
  e_minus_null &&
  -- orthogonality: e₊ · e₋ = 0 (sectors are on opposite null rays)
  SectorPair.mul e_plus_sector e_minus_sector == ⟨0, 0⟩
```
