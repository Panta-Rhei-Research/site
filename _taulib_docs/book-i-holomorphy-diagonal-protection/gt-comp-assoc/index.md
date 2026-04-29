---
{
  "projection_kind": "taulib_declaration",
  "title": "gt_comp_assoc",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/gt-comp-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::gt_comp_assoc",
  "declaration_slug": "gt-comp-assoc",
  "kind": "theorem",
  "name": "gt_comp_assoc",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 191,
  "source_line_end": 204,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L191-L204",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L191-L204",
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/verify/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L191-L204)
- Source range: L191-L204
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- GermTransformer composition is associative. -/
```

## Source Excerpt

```lean
theorem gt_comp_assoc (gt₁ gt₂ gt₃ : GermTransformer) :
    (gt₁.comp gt₂).comp gt₃ = gt₁.comp (gt₂.comp gt₃) := by
  simp [GermTransformer.comp, sector_comp_assoc, stagefun_comp_assoc, Nat.min_assoc]

-- ============================================================
-- HOLFUN MONOID STRUCTURE
-- ============================================================

/-- HolFun forms a monoid under composition:
    - Identity: id_holfun
    - Binary operation: holfun_comp_rf (for reduce-form functions)
    - Associativity: from stagefun_comp_assoc

    The monoid structure is the substrate for the earned category Cat_τ (Part XIII). -/
```
