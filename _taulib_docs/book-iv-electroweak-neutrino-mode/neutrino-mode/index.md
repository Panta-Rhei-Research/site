---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutrinoMode",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::NeutrinoMode",
  "declaration_slug": "neutrino-mode",
  "kind": "structure",
  "name": "NeutrinoMode",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 62,
  "source_line_end": 76,
  "registry_ids": [
    "IV.D124"
  ],
  "related_registry_items": [
    {
      "id": "IV.D124",
      "title": "Neutrino as Time-Eigenmode",
      "url": "/registry/object/IV.D124/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L62-L76",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L62-L76",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L62-L76)
- Source range: L62-L76
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D124` — Neutrino as Time-Eigenmode

## Immediate Comment / Docstring

```lean
/-- [IV.D124] A neutrino mode: a fiber-decoupled eigenmode on tau-cubed
    that couples ONLY to the A-sector (weak force). Neutrinos have
    zero B-sector (EM) and C-sector (Strong) coupling, because they
    carry no electric charge and no color charge.

    The mass suppression exponent encodes the neutrino mass scale
    relative to the electron: m_nu ~ m_e * iota_tau^exponent. -/
```

## Source Excerpt

```lean
structure NeutrinoMode where
  /-- Neutrino flavor. -/
  flavor : NeutrinoFlavor
  /-- Mass exponent: m_nu ~ m_e * iota_tau^exponent. -/
  mass_exponent : Nat
  /-- Couples only to weak force. -/
  weak_only : Bool
  weak_true : weak_only = true
  /-- No electric charge. -/
  charge : Int
  charge_zero : charge = 0
  /-- No color charge. -/
  color_neutral : Bool
  color_true : color_neutral = true
  deriving Repr
```
