---
{
  "projection_kind": "taulib_declaration",
  "title": "explosion_is_semantic",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/explosion-is-semantic/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::explosion_is_semantic",
  "declaration_slug": "explosion-is-semantic",
  "kind": "theorem",
  "name": "explosion_is_semantic",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 291,
  "source_line_end": 297,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L291-L297",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L291-L297",
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
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L291-L297)
- Source range: L291-L297
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The explosion barrier is about material implication, not lattice structure.
    Truth4 IS Boolean, but impl B F = N <> T.
    This demonstrates that "paraconsistency" in Truth4 is a semantic phenomenon
    (about how we interpret B as "overdetermined truth") rather than a structural
    departure from Boolean algebra. -/
```

## Source Excerpt

```lean
theorem explosion_is_semantic :
    -- Truth4 is Boolean (complement laws hold)
    (∀ a : Truth4, Truth4.meet a (Truth4.neg a) = F) ∧
    (∀ a : Truth4, Truth4.join a (Truth4.neg a) = T) ∧
    -- Yet the explosion barrier holds (impl B F <> T)
    (Truth4.impl B F ≠ T) := by
  exact ⟨Truth4.complement_meet, Truth4.complement_join, explosion_barrier⟩
```
