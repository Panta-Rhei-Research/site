---
{
  "projection_kind": "taulib_declaration",
  "title": "necessary_bipolarity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/necessary-bipolarity/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BHBipolarFusion`.",
  "declaration_id": "TauLib.BookV.Cosmology.BHBipolarFusion::necessary_bipolarity",
  "declaration_slug": "necessary-bipolarity",
  "kind": "theorem",
  "name": "necessary_bipolarity",
  "module_name": "TauLib.BookV.Cosmology.BHBipolarFusion",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/",
  "source_line_start": 82,
  "source_line_end": 83,
  "registry_ids": [
    "V.T111"
  ],
  "related_registry_items": [
    {
      "id": "V.T111",
      "title": "Necessary Bipolarity",
      "url": "/registry/object/V.T111/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L82-L83",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BHBipolarFusion",
        "url": "/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L82-L83",
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

- Module: [TauLib.BookV.Cosmology.BHBipolarFusion](/verify/taulib/docs/book-v-cosmology-bhbipolar-fusion/)
- Source path: [`TauLib/BookV/Cosmology/BHBipolarFusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BHBipolarFusion.lean#L82-L83)
- Source range: L82-L83
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T111` — Necessary Bipolarity

## Immediate Comment / Docstring

```lean
/-- [V.T111] Necessary bipolarity: every BH in Category τ is bipolar.
    Unipolar BHs (χ⁺ = 0 or χ⁻ = 0) do not exist.

    Proof: the lemniscate L = S¹ ∨ S¹ has two lobes. The linking
    class must wind around both. Therefore both χ⁺ and χ⁻ are
    necessarily nonzero. -/
```

## Source Excerpt

```lean
theorem necessary_bipolarity (bp : BHBipolarity) :
    bp.chi_plus > 0 ∧ bp.chi_minus > 0 := ⟨bp.plus_pos, bp.minus_pos⟩
```
