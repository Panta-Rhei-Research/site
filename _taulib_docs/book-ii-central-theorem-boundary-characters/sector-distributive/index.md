---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_distributive",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/sector-distributive/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::sector_distributive",
  "declaration_slug": "sector-distributive",
  "kind": "theorem",
  "name": "sector_distributive",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 350,
  "source_line_end": 354,
  "registry_ids": [
    "II.P14"
  ],
  "related_registry_items": [
    {
      "id": "II.P14",
      "title": "Character Algebra Ring Structure",
      "url": "/registry/object/II.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L350-L354",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
        "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L350-L354",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L350-L354)
- Source range: L350-L354
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.P14` — Character Algebra Ring Structure

## Immediate Comment / Docstring

```lean
/-- [II.P14] Distributivity of sector multiplication over addition. -/
```

## Source Excerpt

```lean
theorem sector_distributive (a b c : SectorPair) :
    SectorPair.mul a (SectorPair.add b c) =
    SectorPair.add (SectorPair.mul a b) (SectorPair.mul a c) := by
  simp [SectorPair.mul, SectorPair.add, SectorPair.mk.injEq]
  constructor <;> ring
```
