---
{
  "projection_kind": "taulib_declaration",
  "title": "absorption_trough_z17_mK",
  "permalink": "/verify/taulib/docs/book-v-cosmology-reionization/absorption-trough-z17-m-k/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.Reionization`.",
  "declaration_id": "TauLib.BookV.Cosmology.Reionization::absorption_trough_z17_mK",
  "declaration_slug": "absorption-trough-z17-m-k",
  "kind": "def",
  "name": "absorption_trough_z17_mK",
  "module_name": "TauLib.BookV.Cosmology.Reionization",
  "module_url": "/verify/taulib/docs/book-v-cosmology-reionization/",
  "source_line_start": 77,
  "source_line_end": 77,
  "registry_ids": [
    "V.T271"
  ],
  "related_registry_items": [
    {
      "id": "V.T271",
      "title": "21cm Absorption Trough from tau-Native Inputs",
      "url": "/registry/object/V.T271/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L77-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.Reionization",
        "url": "/verify/taulib/docs/book-v-cosmology-reionization/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L77-L77",
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

- Module: [TauLib.BookV.Cosmology.Reionization](/verify/taulib/docs/book-v-cosmology-reionization/)
- Source path: [`TauLib/BookV/Cosmology/Reionization.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/Reionization.lean#L77-L77)
- Source range: L77-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T271` — 21cm Absorption Trough from tau-Native Inputs

## Immediate Comment / Docstring

```lean
/-- Absorption trough at z = 17 from τ-native inputs [V.T271].
    T₂₁(z=17) ≈ −209 mK.
    Scope: conjectural (depends on spin coupling model). -/
```

## Source Excerpt

```lean
def absorption_trough_z17_mK : Int := -209
```
