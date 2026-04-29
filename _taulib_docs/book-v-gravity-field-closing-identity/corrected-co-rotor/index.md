---
{
  "projection_kind": "taulib_declaration",
  "title": "CorrectedCoRotor",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-closing-identity/corrected-co-rotor/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.ClosingIdentity`.",
  "declaration_id": "TauLib.BookV.GravityField.ClosingIdentity::CorrectedCoRotor",
  "declaration_slug": "corrected-co-rotor",
  "kind": "structure",
  "name": "CorrectedCoRotor",
  "module_name": "TauLib.BookV.GravityField.ClosingIdentity",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-closing-identity/",
  "source_line_start": 141,
  "source_line_end": 156,
  "registry_ids": [
    "V.D82"
  ],
  "related_registry_items": [
    {
      "id": "V.D82",
      "title": "Corrected Co-Rotor Coupling --- V.D10",
      "url": "/registry/object/V.D82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L141-L156",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L141-L156",
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
- Source path: [`TauLib/BookV/GravityField/ClosingIdentity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/ClosingIdentity.lean#L141-L156)
- Source range: L141-L156
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D82` — Corrected Co-Rotor Coupling --- V.D10

## Immediate Comment / Docstring

```lean
/-- [V.D82] Corrected co-rotor coupling with c1 = 3/pi.

    chi * kn / 2 = sqrt(3) * (1 - c1 * alpha)

    Tree-level: kn = 2*sqrt(3) = 3.4641
    Corrected: kn = 2*sqrt(3) * (1 - (3/pi)*alpha) = 3.4400

    The correction c1 = 3/pi comes from:
    3 lemniscate sectors * (1/pi) holonomy = 3/pi. -/
```

## Source Excerpt

```lean
structure CorrectedCoRotor where
  /-- The underlying co-rotor coupling. -/
  base_coupling : CoRotorCoupling
  /-- c1 value: 3/pi. -/
  c1_numer : Nat
  /-- c1 denominator. -/
  c1_denom : Nat
  /-- c1 denominator positive. -/
  c1_denom_pos : c1_denom > 0
  /-- Corrected kn numerator (kn * (1 - c1*alpha)). -/
  corrected_kn_numer : Nat
  /-- Corrected kn denominator. -/
  corrected_kn_denom : Nat
  /-- Corrected denominator positive. -/
  corrected_denom_pos : corrected_kn_denom > 0
  deriving Repr
```
