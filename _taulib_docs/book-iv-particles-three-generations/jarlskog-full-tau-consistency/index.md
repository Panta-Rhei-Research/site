---
{
  "projection_kind": "taulib_declaration",
  "title": "jarlskog_full_tau_consistency",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/jarlskog-full-tau-consistency/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::jarlskog_full_tau_consistency",
  "declaration_slug": "jarlskog-full-tau-consistency",
  "kind": "def",
  "name": "jarlskog_full_tau_consistency",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2057,
  "source_line_end": 2059,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2057-L2059",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2057-L2059",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2057-L2059)
- Source range: L2057-L2059
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P203` — Jarlskog J Full-τ Consistency: J_τ = A_τ²·λ_τ⁶·η̄_τ

## Immediate Comment / Docstring

```lean
/-- [IV.P203] Jarlskog J Full-τ Consistency.
    All 4 Wolfenstein params now τ-effective. J = A²λ_C⁶η̄. -/
```

## Source Excerpt

```lean
def jarlskog_full_tau_consistency : String :=
  "All 4 Wolfenstein: λ_C=ι_τ(1−ι_τ) at −2327, A=1−(3/2)ι_τ² at −887, " ++
  "ρ̄=1/(2π) at +975, η̄=ι_τ^{−1/4}κ_D^{5/4}/√5 at −2285 ppm."
```
