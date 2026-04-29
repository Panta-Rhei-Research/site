---
{
  "projection_kind": "taulib_declaration",
  "title": "baryogenesis_threshold_placement",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/baryogenesis-threshold-placement/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::baryogenesis_threshold_placement",
  "declaration_slug": "baryogenesis-threshold-placement",
  "kind": "def",
  "name": "baryogenesis_threshold_placement",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 269,
  "source_line_end": 271,
  "registry_ids": [
    "V.P133"
  ],
  "related_registry_items": [
    {
      "id": "V.P133",
      "title": "Baryogenesis Threshold Placement: n_EW < n_B < n_N",
      "url": "/registry/object/V.P133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L269-L271",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L269-L271",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L269-L271)
- Source range: L269-L271
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P133` — Baryogenesis Threshold Placement: n_EW < n_B < n_N

## Immediate Comment / Docstring

```lean
/-- [V.P133] Baryogenesis Threshold Placement.
    n_EW < n_B=15 < n_BBN. E_B ~ m_Pl·ι_τ¹⁵ ~ 10¹² GeV. -/
```

## Source Excerpt

```lean
def baryogenesis_threshold_placement : String :=
  "n_EW < n_B=15 < n_BBN. SA-i hierarchy: " ++
  "mod-3 → ι_τ⁹ → θ_QCD=0 (exact); mod-5 → ι_τ¹⁵ → η_B (τ-effective)."
```
