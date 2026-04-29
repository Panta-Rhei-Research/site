---
{
  "projection_kind": "taulib_declaration",
  "title": "PotencyRestriction",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/potency-restriction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::PotencyRestriction",
  "declaration_slug": "potency-restriction",
  "kind": "structure",
  "name": "PotencyRestriction",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 137,
  "source_line_end": 146,
  "registry_ids": [
    "VI.D81"
  ],
  "related_registry_items": [
    {
      "id": "VI.D81",
      "title": "Potency Restriction",
      "url": "/registry/object/VI.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L137-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L137-L146",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L137-L146)
- Source range: L137-L146
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D81` — Potency Restriction

## Immediate Comment / Docstring

```lean
/-- [VI.D81] Potency Restriction.
    More restrictive chromatin partition ↔ lower potency level.
    The 5 potency levels (totipotent, pluripotent, multipotent, oligopotent,
    unipotent) from VI.P18 correspond to monotonically increasing chromatin
    restriction.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure PotencyRestriction where
  /-- Number of potency levels in the hierarchy. -/
  potency_levels : Nat
  /-- Exactly 5 levels. -/
  levels_eq : potency_levels = 5
  /-- Restriction is monotone: higher level → more heterochromatin. -/
  monotone_restriction : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
