---
{
  "projection_kind": "taulib_declaration",
  "title": "bhs_is_topological",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/bhs-is-topological/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.BipolarHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.BipolarHolonomy::bhs_is_topological",
  "declaration_slug": "bhs-is-topological",
  "kind": "theorem",
  "name": "bhs_is_topological",
  "module_name": "TauLib.BookV.GravityField.BipolarHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/",
  "source_line_start": 154,
  "source_line_end": 161,
  "registry_ids": [
    "V.R170"
  ],
  "related_registry_items": [
    {
      "id": "V.R170",
      "title": "Conjectural scope",
      "url": "/registry/object/V.R170/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L154-L161",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.BipolarHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L154-L161",
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

- Module: [TauLib.BookV.GravityField.BipolarHolonomy](/verify/taulib/docs/book-v-gravity-field-bipolar-holonomy/)
- Source path: [`TauLib/BookV/GravityField/BipolarHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L154-L161)
- Source range: L154-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R170` — Conjectural scope

## Immediate Comment / Docstring

```lean
/-- [V.R170] The BHS dimension depends only on (co)homological data.

    All three inputs (b₁_arena, b1_arena, b₁_boundary) are topological
    invariants — they are unchanged by smooth deformations of τ³ or L.
    The dimension 18 is therefore a topological invariant of the pair (τ³, L). -/
```

## Source Excerpt

```lean
theorem bhs_is_topological :
    -- All three Betti numbers are standard topological invariants
    canonical_bhs.b₁_arena = 3 ∧
    canonical_bhs.b1_arena = 3 ∧
    canonical_bhs.b₁_boundary = 2 ∧
    -- The dimension is their product (Künneth-type formula)
    canonical_bhs.dim = canonical_bhs.b₁_arena * canonical_bhs.b1_arena * canonical_bhs.b₁_boundary := by
  exact ⟨rfl, rfl, rfl, rfl⟩
```
