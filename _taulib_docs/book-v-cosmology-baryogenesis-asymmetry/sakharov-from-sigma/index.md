---
{
  "projection_kind": "taulib_declaration",
  "title": "SakharovFromSigma",
  "permalink": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/sakharov-from-sigma/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BaryogenesisAsymmetry`.",
  "declaration_id": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry::SakharovFromSigma",
  "declaration_slug": "sakharov-from-sigma",
  "kind": "structure",
  "name": "SakharovFromSigma",
  "module_name": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
  "module_url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/",
  "source_line_start": 211,
  "source_line_end": 222,
  "registry_ids": [
    "V.T187"
  ],
  "related_registry_items": [
    {
      "id": "V.T187",
      "title": "Sakharov Conditions from τ³ σ-Involution",
      "url": "/registry/object/V.T187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L211-L222",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BaryogenesisAsymmetry",
        "url": "/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L211-L222",
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

- Module: [TauLib.BookV.Cosmology.BaryogenesisAsymmetry](/verify/taulib/docs/book-v-cosmology-baryogenesis-asymmetry/)
- Source path: [`TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BaryogenesisAsymmetry.lean#L211-L222)
- Source range: L211-L222
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T187` — Sakharov Conditions from τ³ σ-Involution

## Immediate Comment / Docstring

```lean
/-- [V.T187] Sakharov Conditions from τ³ σ-Involution.
    All 3 Sakharov conditions satisfied structurally. -/
```

## Source Excerpt

```lean
structure SakharovFromSigma where
  /-- B-violation: pre-confinement baryogenesis window depth. -/
  baryogenesis_depth_start : Nat := 2
  /-- B-violation: baryogenesis window depth end. -/
  baryogenesis_depth_end : Nat := 3
  /-- CP violation: number of generations enabling Jarlskog invariant J_τ ≠ 0. -/
  n_generations_for_cp : Nat := 3
  /-- Out-of-equilibrium: directed α-orbit ensures cooling monotone. -/
  n_conditions : Nat := 3
  /-- Window is non-empty (depth_start < depth_end). -/
  window_nonempty : baryogenesis_depth_start < baryogenesis_depth_end
  deriving Repr
```
