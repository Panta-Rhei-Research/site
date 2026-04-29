---
{
  "projection_kind": "taulib_declaration",
  "title": "jarlskog_invariant_tau",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/jarlskog-invariant-tau/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::jarlskog_invariant_tau",
  "declaration_slug": "jarlskog-invariant-tau",
  "kind": "def",
  "name": "jarlskog_invariant_tau",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1433,
  "source_line_end": 1435,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1433-L1435",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1433-L1435",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1433-L1435)
- Source range: L1433-L1435
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- J = A²·λ_C^6·η̄ from τ-parameters: J_τ = 3.060×10^-5 at -6479 ppm from PDG 3.08×10^-5.
    Inverted: η̄ = J_PDG/(A_τ²·λ_τ^6) = 0.3503 at +6522 ppm. Self-consistent at 0.65%. -/
```

## Source Excerpt

```lean
def jarlskog_invariant_tau : String :=
  "J_τ = A_τ²·λ_τ^6·η̄_PDG = 3.060e-5 at -6479 ppm (PDG 3.08e-5). " ++
  "A_τ=0.82527, λ_τ=0.22482. Inverse: η̄_from_J=0.3503 at +6522 ppm."
```
