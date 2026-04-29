---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_strict_mem",
  "permalink": "/verify/taulib/docs/book-i-sets-powerset/tau-strict-mem/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.Powerset`.",
  "declaration_id": "TauLib.BookI.Sets.Powerset::tau_strict_mem",
  "declaration_slug": "tau-strict-mem",
  "kind": "def",
  "name": "tau_strict_mem",
  "module_name": "TauLib.BookI.Sets.Powerset",
  "module_url": "/verify/taulib/docs/book-i-sets-powerset/",
  "source_line_start": 39,
  "source_line_end": 39,
  "registry_ids": [
    "I.D33"
  ],
  "related_registry_items": [
    {
      "id": "I.D33",
      "title": "Bounded Powerset",
      "url": "/registry/object/I.D33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L39-L39",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Powerset",
        "url": "/verify/taulib/docs/book-i-sets-powerset/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L39-L39",
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

- Module: [TauLib.BookI.Sets.Powerset](/verify/taulib/docs/book-i-sets-powerset/)
- Source path: [`TauLib/BookI/Sets/Powerset.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L39-L39)
- Source range: L39-L39
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D33` — Bounded Powerset

## Immediate Comment / Docstring

```lean
/-- [I.D33] Strict τ-membership: a properly divides b (a | b and a ≠ b). -/
```

## Source Excerpt

```lean
def tau_strict_mem (a b : TauIdx) : Prop := tau_mem a b ∧ a ≠ b
```
