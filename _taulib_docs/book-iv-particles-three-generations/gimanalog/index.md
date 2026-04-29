---
{
  "projection_kind": "taulib_declaration",
  "title": "GIMAnalog",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/gimanalog/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::GIMAnalog",
  "declaration_slug": "gimanalog",
  "kind": "structure",
  "name": "GIMAnalog",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 837,
  "source_line_end": 844,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L837-L844",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L837-L844",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L837-L844)
- Source range: L837-L844
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Uniform off-diagonal b = ι_τ^q in all three generations → Σ_gen b² = constant → FCNC suppressed.
    Numerical: neutrino sector b = ι_τ^4.8 = 0.005742, b² = 3.297e-5, 3b² = 9.892e-5 = const. -/
```

## Source Excerpt

```lean
structure GIMAnalog where
  /-- Number of generations with uniform off-diagonal b. -/
  n_uniform_generations : Nat := 3
  /-- Number of suppressed FCNC channels (Σb² = const). -/
  n_suppressed_fcnc : Nat := 3
  /-- Matrix symmetry rank from σ-equivariance (3×3 → 3 free entries). -/
  sigma_matrix_rank : Nat := 3
  deriving Repr
```
