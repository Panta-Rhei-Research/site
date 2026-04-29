---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_mem",
  "permalink": "/verify/taulib/docs/book-i-sets-membership/tau-mem/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.Membership`.",
  "declaration_id": "TauLib.BookI.Sets.Membership::tau_mem",
  "declaration_slug": "tau-mem",
  "kind": "def",
  "name": "tau_mem",
  "module_name": "TauLib.BookI.Sets.Membership",
  "module_url": "/verify/taulib/docs/book-i-sets-membership/",
  "source_line_start": 49,
  "source_line_end": 49,
  "registry_ids": [
    "I.D31"
  ],
  "related_registry_items": [
    {
      "id": "I.D31",
      "title": "tau-Membership Relation",
      "url": "/registry/object/I.D31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L49-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Membership",
        "url": "/verify/taulib/docs/book-i-sets-membership/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L49-L49",
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

- Module: [TauLib.BookI.Sets.Membership](/verify/taulib/docs/book-i-sets-membership/)
- Source path: [`TauLib/BookI/Sets/Membership.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Membership.lean#L49-L49)
- Source range: L49-L49
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D31` — tau-Membership Relation

## Immediate Comment / Docstring

```lean
/-- [I.D31] τ-membership: a ∈_τ b iff a divides b.
    Every natural number IS its divisor set. -/
```

## Source Excerpt

```lean
def tau_mem (a b : TauIdx) : Prop := idx_divides a b
```
