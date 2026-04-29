---
{
  "projection_kind": "taulib_declaration",
  "title": "MassSuppression",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/mass-suppression/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::MassSuppression",
  "declaration_slug": "mass-suppression",
  "kind": "structure",
  "name": "MassSuppression",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 134,
  "source_line_end": 144,
  "registry_ids": [
    "IV.T58"
  ],
  "related_registry_items": [
    {
      "id": "IV.T58",
      "title": "Spectral Gap Exponent",
      "url": "/registry/object/IV.T58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L134-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L134-L144",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L134-L144)
- Source range: L134-L144
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T58` — Spectral Gap Exponent

## Immediate Comment / Docstring

```lean
/-- [IV.T58] The neutrino mass suppression exponent is 8 = 2 x 4:
    two spectral gaps of iota_tau^4 each.

    The first gap (iota_tau^4) comes from the EM spectral gap
    (the same exponent that gives alpha ~ (8/15)*iota_tau^4).
    The second gap (another iota_tau^4) comes from the fiber
    decoupling: neutrinos do not participate in fiber T^2 modes.

    Combined: the mass suppression from the electron mass scale
    to the neutrino mass scale is iota_tau^8 = (iota_tau^4)^2.
    The total exponent from m_e: m_nu ~ m_e * iota_tau^(7+8) = iota_tau^15
    where 7 is the electron mass bulk exponent.

    NOTE: The equal-spacing model (8 = 2×4) is superseded by the σ-polarity
    recurrence model (NeutrinoRecurrence). The 2×4 factorization remains
    as the approximate overall suppression scale, but the detailed mass
    spectrum requires the σ-equivariant matrix structure. -/
```

## Source Excerpt

```lean
structure MassSuppression where
  /-- Number of spectral gaps. -/
  num_gaps : Nat
  gaps_eq : num_gaps = 2
  /-- Exponent per gap. -/
  exponent_per_gap : Nat
  exp_eq : exponent_per_gap = 4
  /-- Total suppression exponent (additional beyond electron). -/
  total_exponent : Nat
  total_eq : total_exponent = num_gaps * exponent_per_gap
  deriving Repr
```
