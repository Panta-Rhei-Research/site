---
{
  "projection_kind": "taulib_declaration",
  "title": "GlobalFinitenessStatement",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/global-finiteness-statement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::GlobalFinitenessStatement",
  "declaration_slug": "global-finiteness-statement",
  "kind": "structure",
  "name": "GlobalFinitenessStatement",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 285,
  "source_line_end": 294,
  "registry_ids": [
    "V.C20"
  ],
  "related_registry_items": [
    {
      "id": "V.C20",
      "title": "Global Finiteness",
      "url": "/registry/object/V.C20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L285-L294",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L285-L294",
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
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L285-L294)
- Source range: L285-L294
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.C20` — Global Finiteness

## Immediate Comment / Docstring

```lean
/-- [V.C20] Global finiteness: τ³ is globally finite, structured,
    and closed.

    1. Finite temporal extent: t_∞ = Σ p_k⁻¹ converges
    2. Finite motif types: N_motif bounded at each depth
    3. Finite saturation radius: R_sat < ∞
    4. Unique absorbing pattern: convergent, no infinite hierarchy

    This is the four-theorem chain:
    V.T116 → V.T117 → V.T118 → V.C20 -/
```

## Source Excerpt

```lean
structure GlobalFinitenessStatement where
  /-- Finite motif count. -/
  finite_motifs : FiniteMotifBound
  /-- Finite saturation radius. -/
  finite_radius : SaturationRadius
  /-- Unique absorbing pattern. -/
  absorbing : AbsorbingPattern
  /-- Chain complete: all four components present. -/
  chain_length : Nat := 4
  deriving Repr
```
