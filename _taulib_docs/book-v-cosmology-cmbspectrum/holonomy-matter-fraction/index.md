---
{
  "projection_kind": "taulib_declaration",
  "title": "HolonomyMatterFraction",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/holonomy-matter-fraction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::HolonomyMatterFraction",
  "declaration_slug": "holonomy-matter-fraction",
  "kind": "structure",
  "name": "HolonomyMatterFraction",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 81,
  "source_line_end": 88,
  "registry_ids": [
    "V.D248"
  ],
  "related_registry_items": [
    {
      "id": "V.D248",
      "title": "Boundary Holonomy Matter Fraction",
      "url": "/registry/object/V.D248/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L81-L88",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L81-L88",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L81-L88)
- Source range: L81-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D248` — Boundary Holonomy Matter Fraction

## Immediate Comment / Docstring

```lean
/-- [V.D248] Boundary Holonomy Matter Fraction.
    ω_m/ω_b = 1 + (1−ι_τ)/ι_τ² = 6.655.
    Boundary holonomy mass is topological, gravitates like CDM. -/
```

## Source Excerpt

```lean
structure HolonomyMatterFraction where
  /-- Origin type: 1 = topological (not particulate). -/
  origin_type : Nat := 1
  /-- Number of dark sectors (gravitates like CDM). -/
  n_dark_sectors : Nat := 1
  /-- Source chapter. -/
  source_chapter : Nat := 45
  deriving Repr
```
