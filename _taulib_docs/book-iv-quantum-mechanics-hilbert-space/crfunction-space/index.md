---
{
  "projection_kind": "taulib_declaration",
  "title": "CRFunctionSpace",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/crfunction-space/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::CRFunctionSpace",
  "declaration_slug": "crfunction-space",
  "kind": "structure",
  "name": "CRFunctionSpace",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 48,
  "source_line_end": 58,
  "registry_ids": [
    "IV.D60"
  ],
  "related_registry_items": [
    {
      "id": "IV.D60",
      "title": "Space of CR-Functions",
      "url": "/registry/object/IV.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L48-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
        "url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L48-L58",
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

- Module: [TauLib.BookIV.QuantumMechanics.HilbertSpace](/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/)
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L48-L58)
- Source range: L48-L58
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D60` — Space of CR-Functions

## Immediate Comment / Docstring

```lean
/-- [IV.D60] CR(tau^3) = {f : tau^3 -> C | dbar_b f = 0}: the space of
    CR-holomorphic functions on the arena. These are the "physical states"
    before Hilbert space completion.

    Properties:
    - Complex vector space (linearity of dbar_b)
    - Commutative algebra (pointwise multiplication)
    - Infinite-dimensional (one basis element per admissible address) -/
```

## Source Excerpt

```lean
structure CRFunctionSpace where
  /-- Complex vector space. -/
  is_vector_space : Bool
  vec_true : is_vector_space = true
  /-- Commutative algebra under pointwise multiplication. -/
  is_algebra : Bool
  alg_true : is_algebra = true
  /-- Infinite-dimensional (admissible lattice is infinite). -/
  is_infinite_dim : Bool
  inf_true : is_infinite_dim = true
  deriving Repr
```
