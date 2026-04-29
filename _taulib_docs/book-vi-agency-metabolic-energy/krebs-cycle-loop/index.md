---
{
  "projection_kind": "taulib_declaration",
  "title": "KrebsCycleLoop",
  "permalink": "/verify/taulib/docs/book-vi-agency-metabolic-energy/krebs-cycle-loop/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.MetabolicEnergy`.",
  "declaration_id": "TauLib.BookVI.Agency.MetabolicEnergy::KrebsCycleLoop",
  "declaration_slug": "krebs-cycle-loop",
  "kind": "structure",
  "name": "KrebsCycleLoop",
  "module_name": "TauLib.BookVI.Agency.MetabolicEnergy",
  "module_url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/",
  "source_line_start": 133,
  "source_line_end": 142,
  "registry_ids": [
    "VI.P11"
  ],
  "related_registry_items": [
    {
      "id": "VI.P11",
      "title": "Krebs Cycle as Loop_L Instantiation",
      "url": "/registry/object/VI.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L133-L142",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L133-L142",
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
- Source path: [`TauLib/BookVI/Agency/MetabolicEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L133-L142)
- Source range: L133-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P11` — Krebs Cycle as Loop_L Instantiation

## Immediate Comment / Docstring

```lean
/-- [VI.P11] Krebs Cycle as Loop_L instantiation.
    The citric acid cycle is a Poincaré circulation (Book III, Part II)
    that instantiates the Life Loop Class at the metabolic level.
    8-step cycle: acetyl-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP → return. -/
```

## Source Excerpt

```lean
structure KrebsCycleLoop where
  /-- Number of cycle steps. -/
  steps : Nat
  /-- Exactly 8 steps. -/
  steps_eq : steps = 8
  /-- Is a Poincaré circulation (Book III, Part II). -/
  poincare_circulation : Bool := true
  /-- Instantiates Life Loop Class. -/
  life_loop_instance : Bool := true
  deriving Repr
```
