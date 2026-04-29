---
{
  "projection_kind": "taulib_declaration",
  "title": "Truth4.heyting_impl",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/heyting-impl/",
  "summary_short": "`def` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::Truth4.heyting_impl",
  "declaration_slug": "heyting-impl",
  "kind": "def",
  "name": "Truth4.heyting_impl",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 204,
  "source_line_end": 214,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L204-L214",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L204-L214",
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
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L204-L214)
- Source range: L204-L214
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Heyting implication: a => b = sup{c : meet(a,c) <= b}.

    For Truth4 (which is Boolean), this coincides with material implication.
    The table is computed by hand:
      a\b |  T   F   B   N
      ----+----------------
       T  |  T   F   B   N
       F  |  T   T   T   T
       B  |  T   N   T   N
       N  |  T   B   B   T  -/
```

## Source Excerpt

```lean
def Truth4.heyting_impl : Truth4 -> Truth4 -> Truth4
  | T, b => b
  | F, _ => T
  | B, T => T
  | B, F => N
  | B, B => T
  | B, N => N
  | N, T => T
  | N, F => B
  | N, B => B
  | N, N => T
```
