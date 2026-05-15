---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_ingredient_spectral",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-global-hartogs/hartogs-ingredient-spectral/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.GlobalHartogs`.",
  "declaration_id": "TauLib.BookI.Holomorphy.GlobalHartogs::hartogs_ingredient_spectral",
  "declaration_slug": "hartogs-ingredient-spectral",
  "kind": "theorem",
  "name": "hartogs_ingredient_spectral",
  "module_name": "TauLib.BookI.Holomorphy.GlobalHartogs",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-global-hartogs/",
  "source_line_start": 86,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L86-L90",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.GlobalHartogs",
        "url": "/corpus/taulib/docs/book-i-holomorphy-global-hartogs/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L86-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Holomorphy.GlobalHartogs](/corpus/taulib/docs/book-i-holomorphy-global-hartogs/)
- Source path: [`TauLib/BookI/Holomorphy/GlobalHartogs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L86-L90)
- Source range: L86-L90
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ingredient 1: Spectral coefficients determine the function (I.T29). -/
```

## Source Excerpt

```lean
theorem hartogs_ingredient_spectral :
    ∀ f₁ f₂ : StageFun,
    (∀ n k, spectral_of f₁ n k = spectral_of f₂ n k) →
    f₁ = f₂ :=
  spectral_determines
```
