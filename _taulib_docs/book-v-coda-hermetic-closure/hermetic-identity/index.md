---
{
  "projection_kind": "taulib_declaration",
  "title": "HermeticIdentity",
  "permalink": "/verify/taulib/docs/book-v-coda-hermetic-closure/hermetic-identity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.HermeticClosure`.",
  "declaration_id": "TauLib.BookV.Coda.HermeticClosure::HermeticIdentity",
  "declaration_slug": "hermetic-identity",
  "kind": "structure",
  "name": "HermeticIdentity",
  "module_name": "TauLib.BookV.Coda.HermeticClosure",
  "module_url": "/verify/taulib/docs/book-v-coda-hermetic-closure/",
  "source_line_start": 78,
  "source_line_end": 91,
  "registry_ids": [
    "V.T159"
  ],
  "related_registry_items": [
    {
      "id": "V.T159",
      "title": "The Hermetic Identity",
      "url": "/registry/object/V.T159/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L78-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.HermeticClosure",
        "url": "/verify/taulib/docs/book-v-coda-hermetic-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L78-L91",
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

- Module: [TauLib.BookV.Coda.HermeticClosure](/verify/taulib/docs/book-v-coda-hermetic-closure/)
- Source path: [`TauLib/BookV/Coda/HermeticClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/HermeticClosure.lean#L78-L91)
- Source range: L78-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T159` — The Hermetic Identity

## Immediate Comment / Docstring

```lean
/-- [V.T159] The Hermetic Identity:
    H_∂[ω] = H_∂^base[α,π] ⊗_{cross} H_∂^fiber[γ,η,ω]

    ι_τ appears identically in both factors. The crossing sector ω
    mediates between base and fiber. The identity is exact: no
    information is lost in the tensor decomposition. -/
```

## Source Excerpt

```lean
structure HermeticIdentity where
  /-- Base generators (α, π). -/
  base_gens : Nat
  /-- Two base generators. -/
  base_eq : base_gens = 2
  /-- Fiber generators (γ, η, ω). -/
  fiber_gens : Nat
  /-- Three fiber generators. -/
  fiber_eq : fiber_gens = 3
  /-- ι_τ appears in both factors. -/
  iota_in_both : Bool := true
  /-- Tensor decomposition is exact. -/
  decomp_exact : Bool := true
  deriving Repr
```
