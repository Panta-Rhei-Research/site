---
{
  "projection_kind": "taulib_declaration",
  "title": "vert_comp",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/vert-comp/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::vert_comp",
  "declaration_slug": "vert-comp",
  "kind": "def",
  "name": "vert_comp",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 65,
  "source_line_end": 66,
  "registry_ids": [
    "II.D55"
  ],
  "related_registry_items": [
    {
      "id": "II.D55",
      "title": "2-Category Structure",
      "url": "/registry/object/II.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L65-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L65-L66",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L65-L66)
- Source range: L65-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D55` — 2-Category Structure

## Immediate Comment / Docstring

```lean
/-- [II.D55] Vertical composition of 2-cells:
    (eta₂ ∘_v eta₁)(x, k) = eta₂(eta₁(x, k), k).
    If eta₁ : f => g and eta₂ : g => h, then eta₂ ∘_v eta₁ : f => h. -/
```

## Source Excerpt

```lean
def vert_comp (eta₂ eta₁ : TwoCell) : TwoCell :=
  fun n k => eta₂ (eta₁ n k) k
```
