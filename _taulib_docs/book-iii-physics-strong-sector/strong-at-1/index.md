---
{
  "projection_kind": "taulib_declaration",
  "title": "strong_at_1",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/strong-at-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::strong_at_1",
  "declaration_slug": "strong-at-1",
  "kind": "theorem",
  "name": "strong_at_1",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 214,
  "source_line_end": 215,
  "registry_ids": [
    "III.D43"
  ],
  "related_registry_items": [
    {
      "id": "III.D43",
      "title": "Strong Sector at E₁",
      "url": "/registry/object/III.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L214-L215",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L214-L215",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L214-L215)
- Source range: L214-L215
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D43` — Strong Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [III.D43] Structural: strong sector at depth 1 (only prime 2 = X). -/
```

## Source Excerpt

```lean
theorem strong_at_1 :
    strong_sector_at_level 1 = true := by native_decide
```
