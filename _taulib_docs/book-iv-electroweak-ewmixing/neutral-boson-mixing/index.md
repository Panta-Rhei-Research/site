---
{
  "projection_kind": "taulib_declaration",
  "title": "NeutralBosonMixing",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/neutral-boson-mixing/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::NeutralBosonMixing",
  "declaration_slug": "neutral-boson-mixing",
  "kind": "structure",
  "name": "NeutralBosonMixing",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 258,
  "source_line_end": 271,
  "registry_ids": [
    "IV.T60"
  ],
  "related_registry_items": [
    {
      "id": "IV.T60",
      "title": "Neutral Boson Mixing",
      "url": "/registry/object/IV.T60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L258-L271",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L258-L271",
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
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L258-L271)
- Source range: L258-L271
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T60` — Neutral Boson Mixing

## Immediate Comment / Docstring

```lean
/-- [IV.T60] Neutral boson mixing: the physical photon γ and Z boson
    arise from an orthogonal rotation of the neutral W³ and B bosons.

    γ = B cos(θ_W) + W³ sin(θ_W)
    Z = -B sin(θ_W) + W³ cos(θ_W)

    The rotation matrix is orthogonal (SO(2)), preserving the sum
    of squared couplings. -/
```

## Source Excerpt

```lean
structure NeutralBosonMixing where
  /-- Input: neutral weak boson W³. -/
  input_W3 : String := "W3"
  /-- Input: hypercharge boson B. -/
  input_B : String := "B"
  /-- Output: photon. -/
  output_photon : String := "photon"
  /-- Output: Z boson. -/
  output_Z : String := "Z"
  /-- Mixing is an orthogonal (SO(2)) rotation. -/
  orthogonal : Bool := true
  /-- Number of input bosons equals output bosons. -/
  in_out_match : Bool := true
  deriving Repr
```
