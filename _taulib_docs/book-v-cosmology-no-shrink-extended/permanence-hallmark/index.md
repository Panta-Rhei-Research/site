---
{
  "projection_kind": "taulib_declaration",
  "title": "PermanenceHallmark",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/permanence-hallmark/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::PermanenceHallmark",
  "declaration_slug": "permanence-hallmark",
  "kind": "structure",
  "name": "PermanenceHallmark",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 193,
  "source_line_end": 204,
  "registry_ids": [
    "V.D174"
  ],
  "related_registry_items": [
    {
      "id": "V.D174",
      "title": "Permanence Hallmark",
      "url": "/registry/object/V.D174/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L193-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L193-L204",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L193-L204)
- Source range: L193-L204
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D174` — Permanence Hallmark

## Immediate Comment / Docstring

```lean
/-- [V.D174] Permanence hallmark: a structural property P of a
    coherent instance in τ³ such that:
    1. P is acquired at finite depth (onset)
    2. P is ρ-invariant beyond onset
    3. P is irreversible (no τ-admissible path can undo P)

    Black holes have the permanence hallmark: once formed, they
    persist forever. This is the structural concept exported to
    Book VI for the "alive" predicate. -/
```

## Source Excerpt

```lean
structure PermanenceHallmark where
  /-- Onset depth. -/
  onset_depth : Nat
  /-- Onset is finite and positive. -/
  onset_pos : onset_depth > 0
  /-- ρ-invariant beyond onset. -/
  rho_invariant : Bool := true
  /-- Irreversible. -/
  irreversible : Bool := true
  /-- All conditions met. -/
  all_conditions : Bool := true
  deriving Repr
```
