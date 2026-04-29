---
{
  "projection_kind": "taulib_declaration",
  "title": "Hypercharge",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/hypercharge/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::Hypercharge",
  "declaration_slug": "hypercharge",
  "kind": "structure",
  "name": "Hypercharge",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 67,
  "source_line_end": 76,
  "registry_ids": [
    "IV.D127"
  ],
  "related_registry_items": [
    {
      "id": "IV.D127",
      "title": "τ-Hypercharge",
      "url": "/registry/object/IV.D127/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L67-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L67-L76",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L67-L76)
- Source range: L67-L76
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D127` — τ-Hypercharge

## Immediate Comment / Docstring

```lean
/-- [IV.D127] Hypercharge quantum number Y: the U(1)_Y charge
    determined by the boundary character's projection onto the
    B-sector (electromagnetic) component. In the τ-framework,
    Y is a derived quantity from the sector decomposition, NOT
    postulated independently.

    Y = 2(Q − T₃) where Q is electric charge and T₃ is weak isospin. -/
```

## Source Excerpt

```lean
structure Hypercharge where
  /-- Particle or state label. -/
  label : String
  /-- Hypercharge value, as integer (in units of 1/3 for quarks). -/
  y_numer : Int
  /-- Denominator for fractional hypercharges. -/
  y_denom : Nat
  /-- Denominator positive. -/
  denom_pos : y_denom > 0 := by omega
  deriving Repr
```
