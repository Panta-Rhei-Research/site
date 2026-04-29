---
{
  "projection_kind": "taulib_declaration",
  "title": "exponent_15_unique_factorization",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/exponent-15-unique-factorization/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::exponent_15_unique_factorization",
  "declaration_slug": "exponent-15-unique-factorization",
  "kind": "theorem",
  "name": "exponent_15_unique_factorization",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 85,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L85-L90",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L85-L90",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L85-L90)
- Source range: L85-L90
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Factor pairs of 15: (1,15), (3,5), (5,3), (15,1).
    Only (3,5) matches (dim(τ³), |generators|). -/
```

## Source Excerpt

```lean
theorem exponent_15_unique_factorization :
    -- 15 = 3 × 5, and
    tau3_dim = 3 ∧ [TauGenerator.alpha, .pi, .gamma, .eta, .omega].length = 5 ∧
    -- Alternative factors don't match:
    tau3_dim ≠ 1 ∧ tau3_dim ≠ 5 ∧ tau3_dim ≠ 15 := by
  unfold tau3_dim; exact ⟨rfl, rfl, by omega, by omega, by omega⟩
```
