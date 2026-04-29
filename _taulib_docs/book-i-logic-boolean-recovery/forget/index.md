---
{
  "projection_kind": "taulib_declaration",
  "title": "forget",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/forget/",
  "summary_short": "`def` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::forget",
  "declaration_slug": "forget",
  "kind": "def",
  "name": "forget",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 49,
  "source_line_end": 53,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L49-L53",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L49-L53",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.Logic.BooleanRecovery](/verify/taulib/docs/book-i-logic-boolean-recovery/)
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L49-L53)
- Source range: L49-L53
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P13` — Boolean Recovery

## Immediate Comment / Docstring

```lean
/-- [I.P13] Forgetful map from Truth4 to Bool.
    "Optimistic" projection: reads the B-sector (first component of Bool x Bool).
    T -> true, B -> true, N -> false, F -> false. -/
```

## Source Excerpt

```lean
def forget : Truth4 -> Bool
  | T => true
  | B => true
  | N => false
  | F => false
```
