---
{
  "projection_kind": "taulib_declaration",
  "title": "EtaBExponentResolution",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/eta-bexponent-resolution/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::EtaBExponentResolution",
  "declaration_slug": "eta-bexponent-resolution",
  "kind": "structure",
  "name": "EtaBExponentResolution",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 842,
  "source_line_end": 855,
  "registry_ids": [
    "V.R387"
  ],
  "related_registry_items": [
    {
      "id": "V.R387",
      "title": "η_B Exponent Resolution: 15 vs 20 (Effective 19 = W₅(3))",
      "url": "/registry/object/V.R387/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L842-L855",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L842-L855",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L842-L855)
- Source range: L842-L855
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R387` — η_B Exponent Resolution: 15 vs 20 (Effective 19 = W₅(3))

## Immediate Comment / Docstring

```lean
/-- [V.R387] η_B Exponent Resolution: 15 vs 20.

    2nd Ed: η_B = α_τ · ι_τ¹⁵ · (5/6)
    1st Ed: η_B = q_B · ι_τ²⁰ where q_B ≈ 1.313

    Resolution: expanding α_τ = (121/225)·ι_τ⁴ gives
    η_B = (121/270) · ι_τ¹⁹. The effective exponent is 19.
    The 1st Ed absorbed one factor ι_τ into q_B = (121/270)/ι_τ.

    Key coincidence: 19 = W₅(3), the same window number that
    determines N_e/dim(τ³) = 57/3 = 19. Both the inflationary
    duration and baryon asymmetry are governed by the [5,3] CF window. -/
```

## Source Excerpt

```lean
structure EtaBExponentResolution where
  /-- 2nd Ed apparent exponent. -/
  exponent_2nd : Nat := 15
  /-- 1st Ed apparent exponent. -/
  exponent_1st : Nat := 20
  /-- True effective exponent. -/
  effective_exponent : Nat := 19
  /-- W₅(3) = 19 coincidence. -/
  w53_match : effective_exponent = 19
  /-- Prefactor numerator (121). -/
  prefactor_numer : Nat := 121
  /-- Prefactor denominator (270 = 225 × 6/5). -/
  prefactor_denom : Nat := 270
  deriving Repr
```
