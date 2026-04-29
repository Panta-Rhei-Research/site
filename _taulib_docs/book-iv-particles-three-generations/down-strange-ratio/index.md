---
{
  "projection_kind": "taulib_declaration",
  "title": "DownStrangeRatio",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/down-strange-ratio/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::DownStrangeRatio",
  "declaration_slug": "down-strange-ratio",
  "kind": "structure",
  "name": "DownStrangeRatio",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2538,
  "source_line_end": 2549,
  "registry_ids": [
    "IV.P219"
  ],
  "related_registry_items": [
    {
      "id": "IV.P219",
      "title": "m_d/m_s Prediction at −1921 ppm",
      "url": "/registry/object/IV.P219/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2538-L2549",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2538-L2549",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2538-L2549)
- Source range: L2538-L2549
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P219` — m_d/m_s Prediction at −1921 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.P219] m_d/m_s prediction.
    m_d/m_s = ι_τ^(64/23) = 0.05022.
    Exponent: 64/23 = lobes^6 / (a₃ + 2·W₃(4)) = 2⁶/23.
    At -1921 ppm from PDG 0.05032. -/
```

## Source Excerpt

```lean
structure DownStrangeRatio where
  /-- Exponent numerator: lobes^(2·dim) = 2⁶ = 64. -/
  exp_num : Nat := 64
  /-- Exponent denominator: a₃ + 2·W₃(4) = 23. -/
  exp_den : Nat := 23
  /-- Deviation in ppm. -/
  deviation_ppm : Int := -1921
  /-- Numerator = 2⁶. -/
  num_is_lobe_power : exp_num = 2 ^ 6
  /-- Same denominator as charm exponent. -/
  den_shared : exp_den = 13 + 2 * 5
  deriving Repr
```
