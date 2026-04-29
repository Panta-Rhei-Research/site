---
{
  "projection_kind": "taulib_declaration",
  "title": "ChandrasekharThreshold",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/chandrasekhar-threshold/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVStarBuilder`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVStarBuilder::ChandrasekharThreshold",
  "declaration_slug": "chandrasekhar-threshold",
  "kind": "structure",
  "name": "ChandrasekharThreshold",
  "module_name": "TauLib.BookV.GravityField.TOVStarBuilder",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/",
  "source_line_start": 254,
  "source_line_end": 265,
  "registry_ids": [
    "V.D74"
  ],
  "related_registry_items": [
    {
      "id": "V.D74",
      "title": "Chandrasekhar threshold",
      "url": "/registry/object/V.D74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L254-L265",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVStarBuilder",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovstar-builder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L254-L265",
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

- Module: [TauLib.BookV.GravityField.TOVStarBuilder](/verify/taulib/docs/book-v-gravity-field-tovstar-builder/)
- Source path: [`TauLib/BookV/GravityField/TOVStarBuilder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVStarBuilder.lean#L254-L265)
- Source range: L254-L265
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D74` — Chandrasekhar threshold

## Immediate Comment / Docstring

```lean
/-- [V.D74] Chandrasekhar threshold M_Ch: the critical mass above
    which electron degeneracy pressure cannot support the star.

    M_Ch ~ 1.4 M_sun.

    In the tau-framework, this is the minimal mass at which the
    torus vacuum topology T^2 first becomes available. -/
```

## Source Excerpt

```lean
structure ChandrasekharThreshold where
  /-- Threshold mass numerator (in solar masses). -/
  mass_numer : Nat
  /-- Threshold mass denominator. -/
  mass_denom : Nat
  /-- Denominator positive. -/
  denom_pos : mass_denom > 0
  /-- Mass is positive. -/
  mass_positive : mass_numer > 0
  /-- Scope. -/
  scope : String := "tau-effective"
  deriving Repr
```
