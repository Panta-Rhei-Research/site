---
{
  "projection_kind": "taulib_declaration",
  "title": "JarlskogFullTau",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/jarlskog-full-tau/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::JarlskogFullTau",
  "declaration_slug": "jarlskog-full-tau",
  "kind": "structure",
  "name": "JarlskogFullTau",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2062,
  "source_line_end": 2073,
  "registry_ids": [
    "IV.P203"
  ],
  "related_registry_items": [
    {
      "id": "IV.P203",
      "title": "Jarlskog J Full-τ Consistency: J_τ = A_τ²·λ_τ⁶·η̄_τ",
      "url": "/registry/object/IV.P203/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2062-L2073",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2062-L2073",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2062-L2073)
- Source range: L2062-L2073
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P203` — Jarlskog J Full-τ Consistency: J_τ = A_τ²·λ_τ⁶·η̄_τ

## Immediate Comment / Docstring

```lean
/-- [IV.P203] Full Jarlskog τ-consistency structure (formalized). -/
```

## Source Excerpt

```lean
structure JarlskogFullTau where
  /-- Number of Wolfenstein parameters derived from τ. -/
  n_wolfenstein_from_tau : Nat := 4
  /-- λ_C deviation from PDG in ppm. -/
  lambda_deviation_ppm : Nat := 2327
  /-- ρ̄ deviation from PDG in ppm. -/
  rho_deviation_ppm : Nat := 975
  /-- A deviation from PDG in ppm. -/
  a_deviation_ppm : Nat := 887
  /-- η̄ deviation from PDG in ppm. -/
  eta_deviation_ppm : Nat := 2285
  deriving Repr
```
