---
{
  "projection_kind": "taulib_declaration",
  "title": "FiniteMotifBound",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/finite-motif-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::FiniteMotifBound",
  "declaration_slug": "finite-motif-bound",
  "kind": "structure",
  "name": "FiniteMotifBound",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 119,
  "source_line_end": 132,
  "registry_ids": [
    "V.T116"
  ],
  "related_registry_items": [
    {
      "id": "V.T116",
      "title": "Finite Motif Theorem",
      "url": "/registry/object/V.T116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L119-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.GlobalFiniteness",
        "url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L119-L132",
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

- Module: [TauLib.BookV.Cosmology.GlobalFiniteness](/verify/taulib/docs/book-v-cosmology-global-finiteness/)
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L119-L132)
- Source range: L119-L132
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T116` — Finite Motif Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T116] Finite motif theorem: the number of distinct stable
    irreducible topological motifs is finite at every depth.

    N_motif(n) ≤ 2⁴ · p_n³

    where p_n is the n-th prime. The 2⁴ = 16 comes from the
    4-component defect tuple (each binary: above/below threshold).
    The p_n³ comes from the primorial structure at depth n.

    This precisely excludes fractal cosmologies and infinite
    hierarchies of self-similar patterns. -/
```

## Source Excerpt

```lean
structure FiniteMotifBound where
  /-- Refinement depth. -/
  depth : Nat
  /-- Depth positive. -/
  depth_pos : depth > 0
  /-- Bound on motif count at this depth. -/
  motif_bound : Nat
  /-- Bound is positive. -/
  bound_pos : motif_bound > 0
  /-- Actual count at this depth. -/
  actual_count : Nat
  /-- Actual count is below bound. -/
  count_below_bound : actual_count ≤ motif_bound
  deriving Repr
```
