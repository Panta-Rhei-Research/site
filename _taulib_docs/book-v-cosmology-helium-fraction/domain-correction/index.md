---
{
  "projection_kind": "taulib_declaration",
  "title": "DomainCorrection",
  "permalink": "/verify/taulib/docs/book-v-cosmology-helium-fraction/domain-correction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.HeliumFraction`.",
  "declaration_id": "TauLib.BookV.Cosmology.HeliumFraction::DomainCorrection",
  "declaration_slug": "domain-correction",
  "kind": "structure",
  "name": "DomainCorrection",
  "module_name": "TauLib.BookV.Cosmology.HeliumFraction",
  "module_url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/",
  "source_line_start": 132,
  "source_line_end": 143,
  "registry_ids": [
    "V.D194"
  ],
  "related_registry_items": [
    {
      "id": "V.D194",
      "title": "Domain-Wall Correction Factor",
      "url": "/registry/object/V.D194/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L132-L143",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.HeliumFraction",
        "url": "/verify/taulib/docs/book-v-cosmology-helium-fraction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L132-L143",
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

- Module: [TauLib.BookV.Cosmology.HeliumFraction](/verify/taulib/docs/book-v-cosmology-helium-fraction/)
- Source path: [`TauLib/BookV/Cosmology/HeliumFraction.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/HeliumFraction.lean#L132-L143)
- Source range: L132-L143
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D194` — Domain-Wall Correction Factor

## Immediate Comment / Docstring

```lean
/-- [V.D194] Domain-wall correction factor = 5/6.
    Decomposition: 5/6 = 1 − (1/2)(1/3).
    - 1/3 = P(face conflict), proved
    - 1/2 = boundary fraction, self-consistent with 6-threshold structure -/
```

## Source Excerpt

```lean
structure DomainCorrection where
  /-- Numerator. -/
  corr_num : Nat := 5
  /-- Denominator. -/
  corr_den : Nat := 6
  /-- Number of clean thresholds. -/
  clean_thresholds : Nat := 5
  /-- Total thresholds. -/
  total_thresholds : Nat := 6
  /-- Correction = clean/total. -/
  corr_eq : corr_num = clean_thresholds ∧ corr_den = total_thresholds
  deriving Repr
```
