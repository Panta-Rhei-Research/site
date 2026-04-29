---
{
  "projection_kind": "taulib_declaration",
  "title": "book3_prerequisites_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/book3-prerequisites-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.DiffGeoAgenda`.",
  "declaration_id": "TauLib.BookII.Closure.DiffGeoAgenda::book3_prerequisites_check",
  "declaration_slug": "book3-prerequisites-check",
  "kind": "def",
  "name": "book3_prerequisites_check",
  "module_name": "TauLib.BookII.Closure.DiffGeoAgenda",
  "module_url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/",
  "source_line_start": 99,
  "source_line_end": 104,
  "registry_ids": [
    "II.R22"
  ],
  "related_registry_items": [
    {
      "id": "II.R22",
      "title": "Enrichment Ladder Forward Declaration",
      "url": "/registry/object/II.R22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L99-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.DiffGeoAgenda",
        "url": "/verify/taulib/docs/book-ii-closure-diff-geo-agenda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L99-L104",
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

- Module: [TauLib.BookII.Closure.DiffGeoAgenda](/verify/taulib/docs/book-ii-closure-diff-geo-agenda/)
- Source path: [`TauLib/BookII/Closure/DiffGeoAgenda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/DiffGeoAgenda.lean#L99-L104)
- Source range: L99-L104
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.R22` — Enrichment Ladder Forward Declaration

## Immediate Comment / Docstring

```lean
/-- [II.R22] Full prerequisites check for Book III:
    1. E1 layer is complete
    2. Central Theorem verified
    3. Categoricity verified
    4. tau-manifold structure verified
    5. Diff-geo structures are correctly marked as NOT earned -/
```

## Source Excerpt

```lean
def book3_prerequisites_check (db bound k_max : TauIdx) : Bool :=
  e1_complete_for_book3 bound db k_max &&
  central_theorem_check db bound &&
  categoricity_check db bound &&
  tau_manifold_check db bound &&
  diffgeo_not_yet_earned
```
