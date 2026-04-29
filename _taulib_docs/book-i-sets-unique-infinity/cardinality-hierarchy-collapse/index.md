---
{
  "projection_kind": "taulib_declaration",
  "title": "cardinality_hierarchy_collapse",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/cardinality-hierarchy-collapse/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::cardinality_hierarchy_collapse",
  "declaration_slug": "cardinality-hierarchy-collapse",
  "kind": "theorem",
  "name": "cardinality_hierarchy_collapse",
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 230,
  "source_line_end": 240,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L230-L240",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.UniqueInfinity",
        "url": "/verify/taulib/docs/book-i-sets-unique-infinity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L230-L240",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Sets.UniqueInfinity](/verify/taulib/docs/book-i-sets-unique-infinity/)
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L230-L240)
- Source range: L230-L240
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The cardinality hierarchy collapses: since omega is the unique infinity
    and the diagonal argument is inapplicable, there is exactly one
    infinite cardinal in tau (witnessed by the countable object set). -/
```

## Source Excerpt

```lean
theorem cardinality_hierarchy_collapse :
    -- Part 1: exactly one infinity object (up to seed)
    (forall (x y : TauObj), InfinityObject x -> InfinityObject y ->
      x.seed = y.seed) /\
    -- Part 2: the universe is countable
    (exists (f : TauObj -> Nat), Function.Injective f) /\
    -- Part 3: no apparatus for producing larger infinities
    (¬ exists (_ : CantorDiagonalApparatus), True) := by
  refine ⟨?_, tauObj_countable, cantor_inapplicable⟩
  intro x y hx hy
  rw [unique_infinity x hx, unique_infinity y hy]
```
