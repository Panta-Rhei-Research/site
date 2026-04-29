---
{
  "projection_kind": "taulib_declaration",
  "title": "boolean_recovery",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/boolean-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::boolean_recovery",
  "declaration_slug": "boolean-recovery",
  "kind": "theorem",
  "name": "boolean_recovery",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 143,
  "source_line_end": 145,
  "registry_ids": [
    "I.P13"
  ],
  "related_registry_items": [
    {
      "id": "I.P13",
      "title": "Boolean Recovery",
      "url": "/registry/object/I.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L143-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L143-L145",
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
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L143-L145)
- Source range: L143-L145
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P13` — Boolean Recovery

## Immediate Comment / Docstring

```lean
/-- [I.P13] Boolean recovery: a Truth4 value is classical (T or F) if and only if
    both sector projections agree.

    For classical values: forget T = true = forget_pessimistic T, forget F = false = forget_pessimistic F.
    For non-classical: forget B = true but forget_pessimistic B = false (sectors disagree). -/
```

## Source Excerpt

```lean
theorem boolean_recovery (v : Truth4) :
    (v = T ∨ v = F) ↔ (forget v = forget_pessimistic v) := by
  cases v <;> simp [forget, forget_pessimistic]
```
