---
{
  "projection_kind": "taulib_declaration",
  "title": "truth4_is_boolean",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/truth4-is-boolean/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::truth4_is_boolean",
  "declaration_slug": "truth4-is-boolean",
  "kind": "theorem",
  "name": "truth4_is_boolean",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 270,
  "source_line_end": 280,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L270-L280",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.BooleanRecovery",
        "url": "/verify/taulib/docs/book-i-logic-boolean-recovery/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L270-L280",
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

- Module: [TauLib.BookI.Logic.BooleanRecovery](/verify/taulib/docs/book-i-logic-boolean-recovery/)
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L270-L280)
- Source range: L270-L280
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Truth4 is a Boolean algebra: it has complement laws (complement_meet,
    complement_join), distributivity (meet_distrib_join, join_distrib_meet),
    and excluded middle. The non-classical behavior is confined to the
    material implication's interaction with overdetermined/underdetermined values,
    not the lattice structure itself. -/
```

## Source Excerpt

```lean
theorem truth4_is_boolean :
    -- Complement laws
    (∀ a : Truth4, Truth4.meet a (Truth4.neg a) = F) ∧
    (∀ a : Truth4, Truth4.join a (Truth4.neg a) = T) ∧
    -- Distributivity
    (∀ a b c : Truth4,
      Truth4.meet a (Truth4.join b c) = Truth4.join (Truth4.meet a b) (Truth4.meet a c)) ∧
    -- Double negation
    (∀ a : Truth4, Truth4.neg (Truth4.neg a) = a) := by
  exact ⟨Truth4.complement_meet, Truth4.complement_join,
         Truth4.meet_distrib_join, Truth4.neg_involutive⟩
```
