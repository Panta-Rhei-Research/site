---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_strict_mem_nz",
  "permalink": "/verify/taulib/docs/book-i-sets-powerset/tau-strict-mem-nz/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.Powerset`.",
  "declaration_id": "TauLib.BookI.Sets.Powerset::tau_strict_mem_nz",
  "declaration_slug": "tau-strict-mem-nz",
  "kind": "def",
  "name": "tau_strict_mem_nz",
  "module_name": "TauLib.BookI.Sets.Powerset",
  "module_url": "/verify/taulib/docs/book-i-sets-powerset/",
  "source_line_start": 83,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L83-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L83-L83",
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
- Source path: [`TauLib/BookI/Sets/Powerset.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Powerset.lean#L83-L83)
- Source range: L83-L83
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The "nonzero strict membership" relation: a strictly divides b and b ≠ 0. -/
```

## Source Excerpt

```lean
def tau_strict_mem_nz (a b : TauIdx) : Prop := tau_strict_mem a b ∧ b ≠ 0
```
