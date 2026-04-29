---
{
  "projection_kind": "taulib_declaration",
  "title": "layer_conflation_category_error",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/layer-conflation-category-error/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::layer_conflation_category_error",
  "declaration_slug": "layer-conflation-category-error",
  "kind": "theorem",
  "name": "layer_conflation_category_error",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 337,
  "source_line_end": 341,
  "registry_ids": [
    "VII.T48"
  ],
  "related_registry_items": [
    {
      "id": "VII.T48",
      "title": "Layer-Conflation as Category Error",
      "url": "/registry/object/VII.T48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L337-L341",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L337-L341",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L337-L341)
- Source range: L337-L341
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T48` — Layer-Conflation as Category Error

## Immediate Comment / Docstring

```lean
/-- [VII.T48] Layer-Conflation as Category Error (ch128). Conflating
    enrichment layers is a category error: applying E_n concepts at
    E_m (n ≠ m) produces systematic misattributions. Examples:
    applying E₀ logic to E₂ life (mechanistic biology),
    applying E₃ ethics to E₁ physics (moralized nature). -/
```

## Source Excerpt

```lean
theorem layer_conflation_category_error :
    generative_switch.layer_transition = true ∧
    generative_switch.complexity_threshold = true ∧
    generative_switch.structural = true :=
  ⟨rfl, rfl, rfl⟩
```
