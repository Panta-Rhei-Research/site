---
{
  "projection_kind": "taulib_declaration",
  "title": "stagefun_comp_assoc",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/stagefun-comp-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::stagefun_comp_assoc",
  "declaration_slug": "stagefun-comp-assoc",
  "kind": "theorem",
  "name": "stagefun_comp_assoc",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 175,
  "source_line_end": 177,
  "registry_ids": [
    "I.P24"
  ],
  "related_registry_items": [
    {
      "id": "I.P24",
      "title": "HolFun Associativity",
      "url": "/registry/object/I.P24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L175-L177",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L175-L177",
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
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L175-L177)
- Source range: L175-L177
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P24` — HolFun Associativity

## Immediate Comment / Docstring

```lean
/-- [I.P24] Composition of stagewise functions is associative. -/
```

## Source Excerpt

```lean
theorem stagefun_comp_assoc (f₁ f₂ f₃ : StageFun) :
    (f₁.comp f₂).comp f₃ = f₁.comp (f₂.comp f₃) := by
  simp [StageFun.comp]
```
