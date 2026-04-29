---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_union_assoc",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/tau-union-assoc/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::tau_union_assoc",
  "declaration_slug": "tau-union-assoc",
  "kind": "theorem",
  "name": "tau_union_assoc",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 58,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L58-L60",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Operations",
        "url": "/verify/taulib/docs/book-i-sets-operations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L58-L60",
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

- Module: [TauLib.BookI.Sets.Operations](/verify/taulib/docs/book-i-sets-operations/)
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L58-L60)
- Source range: L58-L60
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- ASSOCIATIVITY
-- ============================================================
```

## Source Excerpt

```lean
theorem tau_union_assoc (a b c : TauIdx) :
    tau_union (tau_union a b) c = tau_union a (tau_union b c) :=
  Nat.lcm_assoc a b c
```
