---
{
  "projection_kind": "taulib_declaration",
  "title": "MatterCharField",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/matter-char-field/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TauEinsteinEq`.",
  "declaration_id": "TauLib.BookV.GravityField.TauEinsteinEq::MatterCharField",
  "declaration_slug": "matter-char-field",
  "kind": "structure",
  "name": "MatterCharField",
  "module_name": "TauLib.BookV.GravityField.TauEinsteinEq",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/",
  "source_line_start": 116,
  "source_line_end": 131,
  "registry_ids": [
    "V.D50"
  ],
  "related_registry_items": [
    {
      "id": "V.D50",
      "title": "Matter character --- V.D03",
      "url": "/registry/object/V.D50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L116-L131",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauEinsteinEq",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L116-L131",
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

- Module: [TauLib.BookV.GravityField.TauEinsteinEq](/verify/taulib/docs/book-v-gravity-field-tau-einstein-eq/)
- Source path: [`TauLib/BookV/GravityField/TauEinsteinEq.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauEinsteinEq.lean#L116-L131)
- Source range: L116-L131
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D50` — Matter character --- V.D03

## Immediate Comment / Docstring

```lean
/-- [V.D50] Matter character T^mat in the gravitational field context.

    T^mat = T^EM ⊕ T^wk ⊕ T^s (direct sum of 3 spatial sectors).
    Gravity (D) is NOT included — it appears on the curvature side.

    Each sector contribution is tracked separately:
    - EM (B-sector): electromagnetic field energy
    - Weak (A-sector): weak interaction energy
    - Strong (C-sector): strong interaction energy -/
```

## Source Excerpt

```lean
structure MatterCharField where
  /-- EM sector contribution numerator. -/
  em_numer : Nat
  /-- Weak sector contribution numerator. -/
  weak_numer : Nat
  /-- Strong sector contribution numerator. -/
  strong_numer : Nat
  /-- Common denominator. -/
  denom : Nat
  /-- Denominator positive. -/
  denom_pos : denom > 0
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  deriving Repr
```
