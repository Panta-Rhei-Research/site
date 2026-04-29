---
{
  "projection_kind": "taulib_declaration",
  "title": "AbsorbingPattern",
  "permalink": "/verify/taulib/docs/book-v-cosmology-global-finiteness/absorbing-pattern/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.GlobalFiniteness`.",
  "declaration_id": "TauLib.BookV.Cosmology.GlobalFiniteness::AbsorbingPattern",
  "declaration_slug": "absorbing-pattern",
  "kind": "structure",
  "name": "AbsorbingPattern",
  "module_name": "TauLib.BookV.Cosmology.GlobalFiniteness",
  "module_url": "/verify/taulib/docs/book-v-cosmology-global-finiteness/",
  "source_line_start": 201,
  "source_line_end": 212,
  "registry_ids": [
    "V.D180"
  ],
  "related_registry_items": [
    {
      "id": "V.D180",
      "title": "Absorbing pattern",
      "url": "/registry/object/V.D180/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L201-L212",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L201-L212",
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
- Source path: [`TauLib/BookV/Cosmology/GlobalFiniteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/GlobalFiniteness.lean#L201-L212)
- Source range: L201-L212
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D180` — Absorbing pattern

## Immediate Comment / Docstring

```lean
/-- [V.D180] Absorbing pattern P_∞: assigns to each point its
    limiting eternal motif.

    Properties:
    - ρ-invariant: P_∞ ∘ ρ = P_∞
    - Vacuum outside excisions: P_∞ = vacuum on tau³ \ BH
    - BH inside excisions: P_∞ = eternal BH motif within excisions
    - Unique: there is exactly one absorbing pattern -/
```

## Source Excerpt

```lean
structure AbsorbingPattern where
  /-- Number of distinct eternal motifs. -/
  num_eternal_motifs : Nat
  /-- Finite count. -/
  finite_motifs : num_eternal_motifs > 0
  /-- Whether ρ-invariant. -/
  rho_invariant : Bool := true
  /-- Whether vacuum outside excisions. -/
  vacuum_outside : Bool := true
  /-- Whether unique. -/
  is_unique : Bool := true
  deriving Repr
```
