---
{
  "projection_kind": "taulib_declaration",
  "title": "non_contradiction",
  "permalink": "/verify/taulib/docs/book-i-logic-boolean-recovery/non-contradiction/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Logic.BooleanRecovery`.",
  "declaration_id": "TauLib.BookI.Logic.BooleanRecovery::non_contradiction",
  "declaration_slug": "non-contradiction",
  "kind": "theorem",
  "name": "non_contradiction",
  "module_name": "TauLib.BookI.Logic.BooleanRecovery",
  "module_url": "/verify/taulib/docs/book-i-logic-boolean-recovery/",
  "source_line_start": 258,
  "source_line_end": 259,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L258-L259",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L258-L259",
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
- Source path: [`TauLib/BookI/Logic/BooleanRecovery.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/BooleanRecovery.lean#L258-L259)
- Source range: L258-L259
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Non-contradiction: meet v (neg v) = F for all v. -/
```

## Source Excerpt

```lean
theorem non_contradiction (v : Truth4) : Truth4.meet v (Truth4.neg v) = F :=
  Truth4.complement_meet v
```
