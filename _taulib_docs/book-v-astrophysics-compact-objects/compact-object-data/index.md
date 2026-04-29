---
{
  "projection_kind": "taulib_declaration",
  "title": "CompactObjectData",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/compact-object-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::CompactObjectData",
  "declaration_slug": "compact-object-data",
  "kind": "structure",
  "name": "CompactObjectData",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 78,
  "source_line_end": 91,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L78-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L78-L91",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/verify/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L78-L91)
- Source range: L78-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Compact object data. -/
```

## Source Excerpt

```lean
structure CompactObjectData where
  /-- Object type. -/
  obj_type : CompactObjectType
  /-- Mass (scaled, 0.1 solar masses). -/
  mass_tenth_solar : Nat
  /-- Mass is positive. -/
  mass_pos : mass_tenth_solar > 0
  /-- Radius (scaled, km). -/
  radius_km : Nat
  /-- Radius positive. -/
  radius_pos : radius_km > 0
  /-- Surface magnetic field (scaled, log10 in Gauss). -/
  log_B_gauss : Nat
  deriving Repr
```
