---
{
  "projection_kind": "taulib_declaration",
  "title": "idemp_decomp_recovery",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/idemp-decomp-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::idemp_decomp_recovery",
  "declaration_slug": "idemp-decomp-recovery",
  "kind": "theorem",
  "name": "idemp_decomp_recovery",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 311,
  "source_line_end": 314,
  "registry_ids": [
    "II.D59"
  ],
  "related_registry_items": [
    {
      "id": "II.D59",
      "title": "Idempotent-Supported Character",
      "url": "/registry/object/II.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L311-L314",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L311-L314",
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
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L311-L314)
- Source range: L311-L314
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D59` — Idempotent-Supported Character

## Immediate Comment / Docstring

```lean
/-- [II.D59] Idempotent decomposition is always valid:
    e_plus * sp + e_minus * sp = sp for any SectorPair sp.
    This is the algebraic core of idempotent support. -/
```

## Source Excerpt

```lean
theorem idemp_decomp_recovery (sp : SectorPair) :
    SectorPair.add (SectorPair.mul e_plus_sector sp)
                   (SectorPair.mul e_minus_sector sp) = sp := by
  simp [SectorPair.add, SectorPair.mul, e_plus_sector, e_minus_sector]
```
