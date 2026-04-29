---
{
  "projection_kind": "taulib_declaration",
  "title": "DecelerationParameter",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/deceleration-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CMBSpectrum`.",
  "declaration_id": "TauLib.BookV.Cosmology.CMBSpectrum::DecelerationParameter",
  "declaration_slug": "deceleration-parameter",
  "kind": "structure",
  "name": "DecelerationParameter",
  "module_name": "TauLib.BookV.Cosmology.CMBSpectrum",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cmbspectrum/",
  "source_line_start": 1074,
  "source_line_end": 1081,
  "registry_ids": [
    "V.D271"
  ],
  "related_registry_items": [
    {
      "id": "V.D271",
      "title": "Deceleration Parameter q₀",
      "url": "/registry/object/V.D271/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1074-L1081",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1074-L1081",
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
- Source path: [`TauLib/BookV/Cosmology/CMBSpectrum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CMBSpectrum.lean#L1074-L1081)
- Source range: L1074-L1081
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D271` — Deceleration Parameter q₀

## Immediate Comment / Docstring

```lean
/-- [V.D271] Deceleration Parameter q₀.
    q₀ = Ω_m/2 − Ω_Λ ≈ −0.527.
    Negative → accelerating expansion. -/
```

## Source Excerpt

```lean
structure DecelerationParameter where
  /-- q₀ × 1000 = −527. Encoded as sign + magnitude. -/
  q0_magnitude_x1000 : Nat := 527
  /-- Sign: 0 = negative (accelerating). -/
  q0_negative : Nat := 0
  /-- Matches Planck to < 0.1%. -/
  planck_match_ppm : Nat := 524
  deriving Repr
```
