---
{
  "projection_kind": "taulib_declaration",
  "title": "MembraneAsLemniscate",
  "permalink": "/verify/taulib/docs/book-vi-agency-metabolic-energy/membrane-as-lemniscate/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.MetabolicEnergy`.",
  "declaration_id": "TauLib.BookVI.Agency.MetabolicEnergy::MembraneAsLemniscate",
  "declaration_slug": "membrane-as-lemniscate",
  "kind": "structure",
  "name": "MembraneAsLemniscate",
  "module_name": "TauLib.BookVI.Agency.MetabolicEnergy",
  "module_url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/",
  "source_line_start": 100,
  "source_line_end": 113,
  "registry_ids": [
    "VI.D33"
  ],
  "related_registry_items": [
    {
      "id": "VI.D33",
      "title": "Membrane as Lemniscate Boundary",
      "url": "/registry/object/VI.D33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L100-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Agency.MetabolicEnergy",
        "url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L100-L113",
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

- Module: [TauLib.BookVI.Agency.MetabolicEnergy](/verify/taulib/docs/book-vi-agency-metabolic-energy/)
- Source path: [`TauLib/BookVI/Agency/MetabolicEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L100-L113)
- Source range: L100-L113
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D33` — Membrane as Lemniscate Boundary

## Immediate Comment / Docstring

```lean
/-- [VI.D33] Membrane as Lemniscate Boundary: L = S¹ ∨ S¹.
    Lipid bilayer = two leaflets (outer/inner) sharing hydrophobic core.
    Topologically: L = S¹_outer ∨ S¹_inner.
    Authority: Book II, Part III (L construction); Book II, Ch 44 (Central Theorem).
    The membrane IS the τ-Distinction boundary realized physically. -/
```

## Source Excerpt

```lean
structure MembraneAsLemniscate where
  /-- Number of leaflets. -/
  leaflet_count : Nat
  /-- Exactly 2 leaflets. -/
  leaflets_eq : leaflet_count = 2
  /-- Outer leaflet = S¹. -/
  outer_leaflet : String := "S1_outer"
  /-- Inner leaflet = S¹. -/
  inner_leaflet : String := "S1_inner"
  /-- Wedge point = hydrophobic core. -/
  wedge_point : String := "hydrophobic_core"
  /-- Realizes τ-Distinction boundary. -/
  realizes_distinction : Bool := true
  deriving Repr
```
