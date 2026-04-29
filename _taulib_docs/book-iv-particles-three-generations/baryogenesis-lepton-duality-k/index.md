---
{
  "projection_kind": "taulib_declaration",
  "title": "baryogenesis_lepton_duality_k",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/baryogenesis-lepton-duality-k/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::baryogenesis_lepton_duality_k",
  "declaration_slug": "baryogenesis-lepton-duality-k",
  "kind": "theorem",
  "name": "baryogenesis_lepton_duality_k",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2094,
  "source_line_end": 2095,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2094-L2095",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2094-L2095",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2094-L2095)
- Source range: L2094-L2095
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D366` — k=15/2 Baryogenesis-Lepton Duality: Shared Exponent 15 = dim(τ³)·W₃(4)

## Immediate Comment / Docstring

```lean
/-- [IV.D366] k=15/2 Baryogenesis-Lepton Duality.
    k = dim(τ³)·W₃(4)/|lobes| = 3·5/2 = 15/2.
    Exponent 15 appears in both η_B (cosmo) and m_μ/m_e (leptonic). -/
```

## Source Excerpt

```lean
theorem baryogenesis_lepton_duality_k :
    3 * 5 / 2 = (15 : Nat) / 2 := by native_decide
```
