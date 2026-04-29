---
{
  "projection_kind": "taulib_declaration",
  "title": "AcousticScaleCrosscheck",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/acoustic-scale-crosscheck/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::AcousticScaleCrosscheck",
  "declaration_slug": "acoustic-scale-crosscheck",
  "kind": "structure",
  "name": "AcousticScaleCrosscheck",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 160,
  "source_line_end": 165,
  "registry_ids": [
    "V.P135"
  ],
  "related_registry_items": [
    {
      "id": "V.P135",
      "title": "Structural Acoustic Scale ι_τ⁻⁵ Cross-Check",
      "url": "/registry/object/V.P135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L160-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L160-L165",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L160-L165)
- Source range: L160-L165
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P135` — Structural Acoustic Scale ι_τ⁻⁵ Cross-Check

## Immediate Comment / Docstring

```lean
/-- [V.P135] Structural Acoustic Scale ι_τ⁻⁵ Cross-Check.
    ι_τ⁻⁵ = ((π+e)/2)⁵ = 215.92. Exponent −5 = −(dim+lobes) = −(3+2). -/
```

## Source Excerpt

```lean
structure AcousticScaleCrosscheck where
  /-- Exponent: dim + lobes. -/
  exponent : Nat
  /-- 5 = 3 + 2. -/
  exp_eq : exponent = 3 + 2
  deriving Repr
```
