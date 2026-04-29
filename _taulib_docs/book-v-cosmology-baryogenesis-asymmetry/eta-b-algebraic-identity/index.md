---
{
  "projection_kind": "taulib_declaration",
  "title": "eta_B_algebraic_identity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/eta-b-algebraic-identity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::eta_B_algebraic_identity",
  "declaration_slug": "eta-b-algebraic-identity",
  "kind": "theorem",
  "name": "eta_B_algebraic_identity",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 143,
  "source_line_end": 144,
  "registry_ids": [
    "V.T172"
  ],
  "related_registry_items": [
    {
      "id": "V.T172",
      "title": "Primary Baryogenesis Formula: η_B = α·ι_τ¹⁵·(5/6)",
      "url": "/registry/object/V.T172/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L143-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L143-L144",
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
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L143-L144)
- Source range: L143-L144
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T172` — Primary Baryogenesis Formula: η_B = α·ι_τ¹⁵·(5/6)

## Immediate Comment / Docstring

```lean
/-- Algebraic identity: (121/270) = (121/225) × (5/6). [V.T172]

    This verifies that α_τ·ι_τ¹⁵·(5/6) = (121/270)·ι_τ¹⁹:
    the α_τ factor (= (121/225)·ι_τ⁴) absorbs into the ι_τ tower
    to give a purely algebraic expression. -/
```

## Source Excerpt

```lean
theorem eta_B_algebraic_identity : (121 : Rat) / 270 = 121 / 225 * (5 / 6) := by
  norm_num
```
