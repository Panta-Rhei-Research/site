---
{
  "projection_kind": "taulib_declaration",
  "title": "T2ShadowCorrection",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/t2-shadow-correction/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::T2ShadowCorrection",
  "declaration_slug": "t2-shadow-correction",
  "kind": "structure",
  "name": "T2ShadowCorrection",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 263,
  "source_line_end": 275,
  "registry_ids": [
    "V.D241"
  ],
  "related_registry_items": [
    {
      "id": "V.D241",
      "title": "T² Quadrupole Shadow Correction Factor: f = 1 + ι_τ²/4",
      "url": "/registry/object/V.D241/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L263-L275",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L263-L275",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L263-L275)
- Source range: L263-L275
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D241` — T² Quadrupole Shadow Correction Factor: f = 1 + ι_τ²/4

## Immediate Comment / Docstring

```lean
/-- [V.D241] Structure capturing the T² quadrupole shadow correction.
    Quadrupole order ℓ=2 gives denominator ℓ²=4 in correction f = 1+ι_τ²/4. -/
```

## Source Excerpt

```lean
structure T2ShadowCorrection where
  /-- Quadrupole order ℓ = 2. -/
  quadrupole_order : Nat := 2
  /-- Denominator = ℓ² = 4. -/
  denominator : Nat := 4
  /-- Shadow enlargement is approximately 3% over GR. -/
  enlargement_approx_3pct : Bool := true
  /-- Correction is positive (shadow larger than GR). -/
  correction_positive : Bool := true
  deriving Repr

/-- Canonical T² shadow correction data. -/
instance : Inhabited T2ShadowCorrection := ⟨{}⟩
```
