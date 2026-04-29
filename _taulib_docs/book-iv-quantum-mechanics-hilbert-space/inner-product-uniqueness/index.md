---
{
  "projection_kind": "taulib_declaration",
  "title": "InnerProductUniqueness",
  "permalink": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/inner-product-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.QuantumMechanics.HilbertSpace`.",
  "declaration_id": "TauLib.BookIV.QuantumMechanics.HilbertSpace::InnerProductUniqueness",
  "declaration_slug": "inner-product-uniqueness",
  "kind": "structure",
  "name": "InnerProductUniqueness",
  "module_name": "TauLib.BookIV.QuantumMechanics.HilbertSpace",
  "module_url": "/verify/taulib/docs/book-iv-quantum-mechanics-hilbert-space/",
  "source_line_start": 131,
  "source_line_end": 138,
  "registry_ids": [
    "IV.P18"
  ],
  "related_registry_items": [
    {
      "id": "IV.P18",
      "title": "Inner Product Uniqueness",
      "url": "/registry/object/IV.P18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L131-L138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L131-L138",
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
- Source path: [`TauLib/BookIV/QuantumMechanics/HilbertSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/QuantumMechanics/HilbertSpace.lean#L131-L138)
- Source range: L131-L138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P18` — Inner Product Uniqueness

## Immediate Comment / Docstring

```lean
/-- [IV.P18] Inner product uniqueness: the canonical inner product is
    the UNIQUE inner product on CR(tau^3) that is simultaneously
    sigma-equivariant (respects bipolar involution) and
    rho-compatible (respects refinement tower).
    Formalized structurally: uniqueness = both constraints hold. -/
```

## Source Excerpt

```lean
structure InnerProductUniqueness where
  /-- sigma-equivariant (respects lobe swap). -/
  sigma_equivariant : Bool
  sigma_true : sigma_equivariant = true
  /-- rho-compatible (respects refinement). -/
  rho_compatible : Bool
  rho_true : rho_compatible = true
  deriving Repr
```
