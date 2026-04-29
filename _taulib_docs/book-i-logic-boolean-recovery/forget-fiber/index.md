---
{
  "projection_kind": "taulib_declaration",
  "title": "forget_fiber",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget-fiber/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::forget_fiber",
  "declaration_slug": "forget-fiber",
  "kind": "theorem",
  "name": "forget_fiber",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 163,
  "source_line_end": 176,
  "registry_ids": [
    "I.D41"
  ],
  "related_registry_items": [
    {
      "id": "I.D41",
      "title": "Subobject Classifier Preview",
      "url": "/registry/object/I.D41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L163-L176",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L163-L176",
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
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L163-L176)
- Source range: L163-L176
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D41` — Subobject Classifier Preview

## Immediate Comment / Docstring

```lean
/-- The key information-loss theorem: forget loses exactly the B/N distinction.
    Two values have the same forget image iff they agree on "B-sector truth". -/
```

## Source Excerpt

```lean
theorem forget_fiber (a b : Truth4) :
    forget a = forget b ↔
    (a = b ∨ (a = T ∧ b = B) ∨ (a = B ∧ b = T) ∨
     (a = F ∧ b = N) ∨ (a = N ∧ b = F)) := by
  cases a <;> cases b <;> simp [forget]

-- ============================================================
-- SUBOBJECT CLASSIFIER PREVIEW [I.D41]
-- ============================================================

/-- [I.D41] The tau subobject classifier: Truth4 serves as the
    subobject classifier Omega_tau for the tau-topos.
    Full development deferred to TauLib.Topos. -/
abbrev Omega_tau := Truth4
```
