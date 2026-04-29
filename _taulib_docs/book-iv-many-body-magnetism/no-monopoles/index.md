---
{
  "projection_kind": "taulib_declaration",
  "title": "NoMonopoles",
  "permalink": "/verify/taulib/docs/book-iv-many-body-magnetism/no-monopoles/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.Magnetism`.",
  "declaration_id": "TauLib.BookIV.ManyBody.Magnetism::NoMonopoles",
  "declaration_slug": "no-monopoles",
  "kind": "structure",
  "name": "NoMonopoles",
  "module_name": "TauLib.BookIV.ManyBody.Magnetism",
  "module_url": "/verify/taulib/docs/book-iv-many-body-magnetism/",
  "source_line_start": 131,
  "source_line_end": 144,
  "registry_ids": [
    "IV.T208"
  ],
  "related_registry_items": [
    {
      "id": "IV.T208",
      "title": "No Magnetic Monopoles on T²",
      "url": "/registry/object/IV.T208/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L131-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.Magnetism",
        "url": "/verify/taulib/docs/book-iv-many-body-magnetism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L131-L144",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.ManyBody.Magnetism](/verify/taulib/docs/book-iv-many-body-magnetism/)
- Source path: [`TauLib/BookIV/ManyBody/Magnetism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/Magnetism.lean#L131-L144)
- Source range: L131-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T208` — No Magnetic Monopoles on T²

## Immediate Comment / Docstring

```lean
/-- [IV.T208] **No Magnetic Monopoles on T².**
    χ(T²) = 0 ⟹ ∇·B = 0 identically.

    Proof: A monopole charge g at point p ∈ T² would require
    ∮_{T²} B·dA = g ≠ 0. By Gauss-Bonnet, this integral equals
    2π·χ(T²) = 0 for any curvature 2-form. Hence g = 0.

    This is the electric-magnetic duality in τ³:
    - Electric charge = boundary obstruction (∂T² via L, nontrivial)
    - Magnetic charge = Euler obstruction (χ(T²) = 0, trivial)

    No monopoles exist — not as empirical fact, but as topological necessity. -/
```

## Source Excerpt

```lean
structure NoMonopoles where
  /-- Euler characteristic of T² is zero. -/
  euler_char_zero : Bool := true
  /-- χ(T²) = 0 by genus-1 surface. -/
  genus_one : Nat := 1
  /-- Gauss-Bonnet gives total charge zero. -/
  gauss_bonnet_zero : Bool := true
  /-- Electric charge: boundary obstruction (nontrivial). -/
  electric_boundary : Bool := true
  /-- Magnetic charge: Euler obstruction (trivial). -/
  magnetic_euler : Bool := true
  /-- Topological necessity, not empirical. -/
  topological_necessity : Bool := true
  deriving Repr
```
