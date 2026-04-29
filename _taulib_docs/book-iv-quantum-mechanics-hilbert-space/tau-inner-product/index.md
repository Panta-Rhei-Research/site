---
{
  "projection_kind": "taulib_declaration",
  "title": "TauInnerProduct",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/tau-inner-product/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::TauInnerProduct",
  "declaration_slug": "tau-inner-product",
  "kind": "structure",
  "name": "TauInnerProduct",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 89,
  "source_line_end": 99,
  "registry_ids": [
    "IV.D61"
  ],
  "related_registry_items": [
    {
      "id": "IV.D61",
      "title": "Canonical Inner Product",
      "url": "/registry/object/IV.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L89-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L89-L99",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L89-L99)
- Source range: L89-L99
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D61` — Canonical Inner Product

## Immediate Comment / Docstring

```lean
/-- [IV.D61] The canonical inner product on CR(tau^3):
    <f, g> = integral f_bar * g d_mu over tau^3.
    Inherits Hermitian, sesquilinear, positive-definite properties
    from the CR-structure + Haar measure on T^2. -/
```

## Source Excerpt

```lean
structure TauInnerProduct where
  /-- Sesquilinear in f, g. -/
  is_sesquilinear : Bool
  sesq_true : is_sesquilinear = true
  /-- Hermitian: <f,g> = conjugate(<g,f>). -/
  is_hermitian : Bool
  herm_true : is_hermitian = true
  /-- Positive definite: <f,f> > 0 for f != 0. -/
  is_positive_definite : Bool
  posdef_true : is_positive_definite = true
  deriving Repr
```
