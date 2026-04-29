---
{
  "projection_kind": "taulib_declaration",
  "title": "ClosingIdentityData",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/closing-identity-data/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::ClosingIdentityData",
  "declaration_slug": "closing-identity-data",
  "kind": "structure",
  "name": "ClosingIdentityData",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 95,
  "source_line_end": 115,
  "registry_ids": [
    "V.D81"
  ],
  "related_registry_items": [
    {
      "id": "V.D81",
      "title": "Gravitational Closing Identity --- V.D11",
      "url": "/registry/object/V.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L95-L115",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.ClosingIdentity",
        "url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L95-L115",
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

- Module: [TauLib.BookV.GravityField.ClosingIdentity](/verify/taulib/docs/book-v-gravity-field-closing-identity/)
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L95-L115)
- Source range: L95-L115
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D81` — Gravitational Closing Identity --- V.D11

## Immediate Comment / Docstring

```lean
/-- [V.D81] Gravitational closing identity:
    alpha_G = alpha^18 * (chi * kn / 2).

    This connects the gravitational and electromagnetic coupling
    constants through the co-rotor coupling distance kn on T^2.

    alpha_G = G * m_n^2 / (hbar * c)

    The exponent 18 = 2 * 9 comes from: alpha_G/alpha ~ (m_n/m_P)^2
    and m_n/m_P ~ alpha^9 from the calibration cascade. -/
```

## Source Excerpt

```lean
structure ClosingIdentityData where
  /-- The alpha exponent (always 18). -/
  alpha_exponent : Nat
  /-- Exponent is 18. -/
  exp_is_18 : alpha_exponent = 18
  /-- chi factor numerator (= 1 at tree level). -/
  chi_numer : Nat
  /-- chi factor denominator. -/
  chi_denom : Nat
  /-- chi denominator positive. -/
  chi_denom_pos : chi_denom > 0
  /-- kn numerator (co-rotor coupling). -/
  kn_numer : Nat
  /-- kn denominator. -/
  kn_denom : Nat
  /-- kn denominator positive. -/
  kn_denom_pos : kn_denom > 0
  /-- Scope: the identity structure is tau-effective,
      the specific kn value is conjectural. -/
  scope : String := "conjectural"
  deriving Repr
```
