---
{
  "projection_kind": "taulib_declaration",
  "title": "inner_product_linearity_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/inner-product-linearity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::inner_product_linearity_check",
  "declaration_slug": "inner-product-linearity-check",
  "kind": "def",
  "name": "inner_product_linearity_check",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 68,
  "source_line_end": 73,
  "registry_ids": [
    "II.D82"
  ],
  "related_registry_items": [
    {
      "id": "II.D82",
      "title": "L² Inner Product",
      "url": "/registry/object/II.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L68-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L68-L73",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L68-L73)
- Source range: L68-L73
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D82` — L² Inner Product

## Immediate Comment / Docstring

```lean
/-- [II.D82] Linearity check: ⟨af₁ + bf₂, g⟩ = a⟨f₁,g⟩ + b⟨f₂,g⟩. -/
```

## Source Excerpt

```lean
def inner_product_linearity_check (a b : Int) (f1 f2 g : Nat → Int)
    (k : Nat) : Bool :=
  let lhs := l2_inner_product (fun x => a * f1 x + b * f2 x) g k
  let rhs_1 := l2_inner_product f1 g k
  let rhs_2 := l2_inner_product f2 g k
  lhs.numerator == a * rhs_1.numerator + b * rhs_2.numerator
```
