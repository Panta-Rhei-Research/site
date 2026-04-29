---
{
  "projection_kind": "taulib_declaration",
  "title": "TwoHorizonConsistency",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/two-horizon-consistency/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::TwoHorizonConsistency",
  "declaration_slug": "two-horizon-consistency",
  "kind": "structure",
  "name": "TwoHorizonConsistency",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 283,
  "source_line_end": 292,
  "registry_ids": [
    "V.T195"
  ],
  "related_registry_items": [
    {
      "id": "V.T195",
      "title": "Two-Horizon Consistency from ι_τ",
      "url": "/registry/object/V.T195/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L283-L292",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CMBSpectrum",
        "url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L283-L292",
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

- Module: [TauLib.BookV.Cosmology.CMBSpectrum](/verify/taulib/docs/book-v-cosmology-cmbspectrum/)
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L283-L292)
- Source range: L283-L292
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T195` — Two-Horizon Consistency from ι_τ

## Immediate Comment / Docstring

```lean
/-- [V.T195] Two-Horizon Consistency from ι_τ.
    CMB (z_rec~1093), CνB (z_ν~5.8×10⁹), Mass (f_ν→ΔP/P).
    Three chains, zero free parameters. -/
```

## Source Excerpt

```lean
structure TwoHorizonConsistency where
  /-- Number of independent horizons. -/
  n_horizons : Nat
  /-- Three horizons. -/
  horizons_eq : n_horizons = 3
  /-- Number of free parameters. -/
  free_params : Nat := 0
  /-- Number of independent inputs (single ι_τ). -/
  n_inputs : Nat := 1
  deriving Repr
```
