---
{
  "projection_kind": "taulib_declaration",
  "title": "CurrencyUniqueness",
  "permalink": "/verify/taulib/docs/book-vi-agency-metabolic-energy/currency-uniqueness/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Agency.MetabolicEnergy`.",
  "declaration_id": "TauLib.BookVI.Agency.MetabolicEnergy::CurrencyUniqueness",
  "declaration_slug": "currency-uniqueness",
  "kind": "structure",
  "name": "CurrencyUniqueness",
  "module_name": "TauLib.BookVI.Agency.MetabolicEnergy",
  "module_url": "/verify/taulib/docs/book-vi-agency-metabolic-energy/",
  "source_line_start": 65,
  "source_line_end": 78,
  "registry_ids": [
    "VI.T19"
  ],
  "related_registry_items": [
    {
      "id": "VI.T19",
      "title": "Universal Currency Uniqueness",
      "url": "/registry/object/VI.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L65-L78",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L65-L78",
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
- Source path: [`TauLib/BookVI/Agency/MetabolicEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Agency/MetabolicEnergy.lean#L65-L78)
- Source range: L65-L78
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T19` — Universal Currency Uniqueness

## Immediate Comment / Docstring

```lean
/-- [VI.T19] Universal Currency Uniqueness Theorem.
    ATP is the unique energy currency satisfying:
    (i) Life Loop closure (metabolic cycle returns to initial state)
    (ii) Coupling constraint (energy quantum matches phosphate bond)
    (iii) Topological constraint (adenine-ribose-triphosphate topology) -/
```

## Source Excerpt

```lean
structure CurrencyUniqueness where
  /-- Number of uniqueness constraints. -/
  constraint_count : Nat
  /-- Exactly 3 constraints. -/
  count_eq : constraint_count = 3
  /-- (i) Life Loop closure. -/
  loop_closure : Bool := true
  /-- (ii) Coupling constraint. -/
  coupling : Bool := true
  /-- (iii) Topological constraint. -/
  topological : Bool := true
  /-- Result: ATP is unique. -/
  unique_currency : String := "ATP"
  deriving Repr
```
