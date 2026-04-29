---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyNLOScan",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/holonomy-nloscan/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::HolonomyNLOScan",
  "declaration_slug": "holonomy-nloscan",
  "kind": "structure",
  "name": "HolonomyNLOScan",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 250,
  "source_line_end": 255,
  "registry_ids": [
    "V.T193"
  ],
  "related_registry_items": [
    {
      "id": "V.T193",
      "title": "Holonomy Matter NLO Correction Scan",
      "url": "/registry/object/V.T193/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L250-L255",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L250-L255",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L250-L255)
- Source range: L250-L255
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T193` — Holonomy Matter NLO Correction Scan

## Immediate Comment / Docstring

```lean
/-- [V.T193] Holonomy Matter NLO Correction Scan.
    Best: δ = ι_τ³ at −386 ppm on ratio, but ℓ₁ worsens to +8655 ppm. -/
```

## Source Excerpt

```lean
structure HolonomyNLOScan where
  /-- Best NLO exponent (ι_τ³ → 3). -/
  best_exponent : Nat := 3
  /-- NLO deviation in ppm (cancellation broken). -/
  nlo_deviation_ppm : Nat := 8655
  deriving Repr
```
