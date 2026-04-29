---
{
  "projection_kind": "taulib_declaration",
  "title": "WolfensteinRhoBar",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/wolfenstein-rho-bar-l896/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::WolfensteinRhoBar",
  "declaration_slug": "wolfenstein-rho-bar-l896",
  "kind": "structure",
  "name": "WolfensteinRhoBar",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 896,
  "source_line_end": 903,
  "registry_ids": [
    "IV.P190"
  ],
  "related_registry_items": [
    {
      "id": "IV.P190",
      "title": "Wolfenstein Parameters: ρ̄=1/(2π) at +974 ppm (τ-effective); A and η̄ open",
      "url": "/registry/object/IV.P190/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L896-L903",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L896-L903",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L896-L903)
- Source range: L896-L903
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P190` — Wolfenstein Parameters: ρ̄=1/(2π) at +974 ppm (τ-effective); A and η̄ open

## Immediate Comment / Docstring

```lean
/-- [IV.P190] Wolfenstein ρ̄ = 1/(2π) structure (formalized). -/
```

## Source Excerpt

```lean
structure WolfensteinRhoBar where
  /-- Denominator multiplier: 1/(2π), multiplier = 2. -/
  denom_multiplier : Nat := 2
  /-- Deviation from PDG in ppm. -/
  deviation_ppm : Nat := 974
  /-- τ-effective threshold in ppm. -/
  tau_eff_threshold_ppm : Nat := 5000
  deriving Repr
```
