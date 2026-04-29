---
{
  "projection_kind": "taulib_declaration",
  "title": "koide_angle",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/koide-angle/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::koide_angle",
  "declaration_slug": "koide-angle",
  "kind": "def",
  "name": "koide_angle",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 513,
  "source_line_end": 513,
  "registry_ids": [
    "IV.D345"
  ],
  "related_registry_items": [
    {
      "id": "IV.D345",
      "title": "Koide Angle delta=2/9",
      "url": "/registry/object/IV.D345/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L513-L513",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L513-L513",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L513-L513)
- Source range: L513-L513
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D345` — Koide Angle delta=2/9

## Immediate Comment / Docstring

```lean
/-- [IV.D345] The Koide angle δ = 2/9 (radians).
    - Numerator 2 = lobes of L = S¹ ∨ S¹
    - Denominator 9 = dim(τ³)² (3 × 3)
    Encodes all three lepton masses via: m_k = M·(1+√2·cos(δ+2πk/3))²
    Verified: binary search gives delta_fit = 0.222222046 vs 2/9 = 0.222222222,
    difference -1.76e-7 rad = -0.001 per-mille. -/
```

## Source Excerpt

```lean
def koide_angle : Float := 2.0 / 9.0
```
