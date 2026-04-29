---
{
  "projection_kind": "taulib_declaration",
  "title": "l3_template_extends",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/l3-template-extends/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.ExponentDerivation`.",
  "declaration_id": "TauLib.BookV.GravityField.ExponentDerivation::l3_template_extends",
  "declaration_slug": "l3-template-extends",
  "kind": "theorem",
  "name": "l3_template_extends",
  "module_name": "TauLib.BookV.GravityField.ExponentDerivation",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/",
  "source_line_start": 189,
  "source_line_end": 196,
  "registry_ids": [
    "V.P110"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L189-L196",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ExponentDerivation",
        "url": "/verify/taulib/docs/book-v-gravity-field-exponent-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L189-L196",
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

- Module: [TauLib.BookV.GravityField.ExponentDerivation](/verify/taulib/docs/book-v-gravity-field-exponent-derivation/)
- Source path: [`TauLib/BookV/GravityField/ExponentDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ExponentDerivation.lean#L189-L196)
- Source range: L189-L196
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P110] The L3 holonomy correction π³α² and the L5 exponent 18
    share the factor dim(τ³) = 3.

    L3: dim(τ³) → number of U(1) circles → π-exponent = 3
    L5: dim(τ³) → number of holonomy layers → one factor of 18 = 2×3×3

    The same structural invariant serves both roles. -/
```

## Source Excerpt

```lean
theorem l3_template_extends :
    -- L3: dim gives π exponent
    triple_holonomy.circle_count = 3 ∧
    -- L5: dim is one factor of the α exponent
    canonical_factors.dim_tau3 = 3 ∧
    -- They are the SAME 3
    triple_holonomy.circle_count = canonical_factors.dim_tau3 := by
  exact ⟨rfl, rfl, rfl⟩
```
