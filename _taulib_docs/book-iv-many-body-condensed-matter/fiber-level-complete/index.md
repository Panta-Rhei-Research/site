---
{
  "projection_kind": "taulib_declaration",
  "title": "FiberLevelComplete",
  "permalink": "/verify/taulib/docs/book-iv-many-body-condensed-matter/fiber-level-complete/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.CondensedMatter`.",
  "declaration_id": "TauLib.BookIV.ManyBody.CondensedMatter::FiberLevelComplete",
  "declaration_slug": "fiber-level-complete",
  "kind": "structure",
  "name": "FiberLevelComplete",
  "module_name": "TauLib.BookIV.ManyBody.CondensedMatter",
  "module_url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/",
  "source_line_start": 192,
  "source_line_end": 203,
  "registry_ids": [
    "IV.P144"
  ],
  "related_registry_items": [
    {
      "id": "IV.P144",
      "title": "Fiber-level physics is complete",
      "url": "/registry/object/IV.P144/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L192-L203",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.CondensedMatter",
        "url": "/verify/taulib/docs/book-iv-many-body-condensed-matter/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L192-L203",
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

- Module: [TauLib.BookIV.ManyBody.CondensedMatter](/verify/taulib/docs/book-iv-many-body-condensed-matter/)
- Source path: [`TauLib/BookIV/ManyBody/CondensedMatter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/CondensedMatter.lean#L192-L203)
- Source range: L192-L203
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P144` — Fiber-level physics is complete

## Immediate Comment / Docstring

```lean
/-- [IV.P144] At the close of Part VII, every tau-admissible phenomenon
    on the fiber T^2 is classified:

    - Single particles (Part VI): quark/lepton spectrum, generations
    - Quantum mechanics (Part III): uncertainty, measurement, energy/entropy
    - Mass derivation (Part III): R = m_n/m_e, 10-link chain
    - Electroweak forces (Part IV): EM, weak, Weinberg mixing, Higgs
    - Strong force (Part V): confinement, mass gap, quarks/gluons
    - Many-body (Part VII): 10 regimes, phase transitions, magnetism, NFL theorem

    Nothing on the fiber T^2 remains unclassified. Book V addresses
    the base tau^1 (gravity, cosmology, temporal structure). -/
```

## Source Excerpt

```lean
structure FiberLevelComplete where
  /-- All fiber phenomena classified. -/
  all_classified : Bool := true
  /-- Number of Parts covering fiber. -/
  num_parts : Nat := 5
  /-- Parts: III (QM), IV (EW), V (Strong), VI (Particles), VII (Many-body). -/
  parts : List String := ["III (QM)", "IV (EW)", "V (Strong)", "VI (Particles)", "VII (Many-body)"]
  /-- Book V handles the base. -/
  book_v_handles_base : Bool := true
  /-- Export contract to Book V. -/
  export_to_book_v : Bool := true
  deriving Repr
```
