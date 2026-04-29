---
{
  "projection_kind": "taulib_declaration",
  "title": "HermeticTruth",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/hermetic-truth/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::HermeticTruth",
  "declaration_slug": "hermetic-truth",
  "kind": "structure",
  "name": "HermeticTruth",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 195,
  "source_line_end": 212,
  "registry_ids": [
    "V.T143"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L195-L212",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.BridgeToLife",
        "url": "/verify/taulib/docs/book-v-coda-bridge-to-life/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L195-L212",
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

- Module: [TauLib.BookV.Coda.BridgeToLife](/verify/taulib/docs/book-v-coda-bridge-to-life/)
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L195-L212)
- Source range: L195-L212
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T143] The Hermetic Truth:

    H_partial[omega] = H_partial^base[alpha,pi]
                        ⊗_{H_partial^cross}
                        H_partial^fiber[gamma,eta,omega]

    is exact. Every E1 observable is a character on this tensor product.

    base = temporal = {alpha, pi} = {Gravity, Weak}
    fiber = spatial = {gamma, eta, omega} = {EM, Strong, Higgs}
    crossing = Higgs/omega sector (lobe junction point)

    The crossing sector omega = gamma ∩ eta mediates between
    base and fiber. Without the crossing, the tensor product
    would decouple into independent temporal and spatial physics. -/
```

## Source Excerpt

```lean
structure HermeticTruth where
  /-- Number of base generators. -/
  base_generators : Nat
  /-- 2 base generators (alpha, pi). -/
  base_eq : base_generators = 2
  /-- Number of fiber generators. -/
  fiber_generators : Nat
  /-- 3 fiber generators (gamma, eta, omega). -/
  fiber_eq : fiber_generators = 3
  /-- Total generators. -/
  total : Nat
  /-- 2 + 3 = 5. -/
  total_eq : total = base_generators + fiber_generators
  /-- Tensor product is exact. -/
  tensor_exact : Bool := true
  /-- Crossing sector mediates. -/
  crossing_mediates : Bool := true
  deriving Repr
```
