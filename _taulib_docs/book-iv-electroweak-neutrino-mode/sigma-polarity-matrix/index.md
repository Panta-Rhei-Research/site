---
{
  "projection_kind": "taulib_declaration",
  "title": "SigmaPolarityMatrix",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-polarity-matrix/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::SigmaPolarityMatrix",
  "declaration_slug": "sigma-polarity-matrix",
  "kind": "structure",
  "name": "SigmaPolarityMatrix",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 375,
  "source_line_end": 381,
  "registry_ids": [
    "V.D233"
  ],
  "related_registry_items": [
    {
      "id": "V.D233",
      "title": "sigma-Polarity Neutrino Mass Matrix",
      "url": "/registry/object/V.D233/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L375-L381",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L375-L381",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L375-L381)
- Source range: L375-L381
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D233` — sigma-Polarity Neutrino Mass Matrix

## Immediate Comment / Docstring

```lean
/-- [V.D233] The sigma-equivariant 3×3 neutrino mass matrix.
    M = [[a, b, 0], [b, c, b], [0, b, a]]
    with a = ι_τ^p (lobe self-coupling), b = ι_τ^q (lobe-mediator,
    most suppressed), c = ι_τ^r (crossing self-coupling).

    The (1,3) and (3,1) entries vanish structurally: winding classes
    (1,0) and (0,1) on T² have no direct off-diagonal coupling because
    they lie on orthogonal torus cycles; only the mixed class (1,1) mediates.

    Best-fit (Sprint 3): p = 3.7, q = 4.8, r = 2.8.
    Shape parameters: Δpq = q − p ≈ 14/13, Δpr = p − r ≈ 12/13 (CF-motivated).
    Ratio Δm²₃₁/Δm²₂₁ = 32.82 (PDG: 32.58, 0.75%).
    Σmν = 0.089 eV < 0.12 eV (Planck 2018). -/
```

## Source Excerpt

```lean
structure SigmaPolarityMatrix where
  /-- Diagonal lobe exponent: a = ι_τ^p. -/
  p : Float
  /-- Off-diagonal mediator exponent: b = ι_τ^q (most suppressed). -/
  q : Float
  /-- Central crossing exponent: c = ι_τ^r (strongest). -/
  r : Float
```
