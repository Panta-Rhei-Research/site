---
{
  "projection_kind": "taulib_declaration",
  "title": "LawvereTierneyOperator",
  "permalink": "/verify/taulib/docs/book-vii-meta-archetypes/lawvere-tierney-operator/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::LawvereTierneyOperator",
  "declaration_slug": "lawvere-tierney-operator",
  "kind": "structure",
  "name": "LawvereTierneyOperator",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/verify/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 42,
  "source_line_end": 49,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L42-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Archetypes",
        "url": "/verify/taulib/docs/book-vii-meta-archetypes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L42-L49",
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

- Module: [TauLib.BookVII.Meta.Archetypes](/verify/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L42-L49)
- Source range: L42-L49
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Lawvere-Tierney closure operator j : Ω → Ω on [τ^op, τ].
    Three axioms: (LT1) j ∘ true = true, (LT2) j ∘ j = j, (LT3) j ∘ ∧ = ∧ ∘ (j × j). -/
```

## Source Excerpt

```lean
structure LawvereTierneyOperator where
  /-- (LT1) Truth-closed: j preserves truth. -/
  lt1_truth_closed : Bool := true
  /-- (LT2) Idempotent: j ∘ j = j. -/
  lt2_idempotent : Bool := true
  /-- (LT3) Commutes with meet: j ∘ ∧ = ∧ ∘ (j × j). -/
  lt3_meet_commute : Bool := true
  deriving Repr
```
