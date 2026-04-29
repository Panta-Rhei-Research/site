---
{
  "projection_kind": "taulib_declaration",
  "title": "BaryogenesisLeptonDuality",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/baryogenesis-lepton-duality/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::BaryogenesisLeptonDuality",
  "declaration_slug": "baryogenesis-lepton-duality",
  "kind": "structure",
  "name": "BaryogenesisLeptonDuality",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2098,
  "source_line_end": 2107,
  "registry_ids": [
    "IV.D366"
  ],
  "related_registry_items": [
    {
      "id": "IV.D366",
      "title": "k=15/2 Baryogenesis-Lepton Duality: Shared Exponent 15 = dim(τ³)·W₃(4)",
      "url": "/registry/object/IV.D366/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2098-L2107",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2098-L2107",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2098-L2107)
- Source range: L2098-L2107
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D366` — k=15/2 Baryogenesis-Lepton Duality: Shared Exponent 15 = dim(τ³)·W₃(4)

## Immediate Comment / Docstring

```lean
/-- [IV.D366] Baryogenesis-lepton duality structure (formalized). -/
```

## Source Excerpt

```lean
structure BaryogenesisLeptonDuality where
  /-- Shared exponent: 15. -/
  shared_exponent : Nat := 15
  /-- dim(τ³) = 3. -/
  dim_tau3 : Nat := 3
  /-- W₃(4) = 5. -/
  w3_4 : Nat := 5
  /-- Number of lobes. -/
  n_lobes : Nat := 2
  deriving Repr
```
