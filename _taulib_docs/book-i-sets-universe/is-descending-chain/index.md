---
{
  "projection_kind": "taulib_declaration",
  "title": "is_descending_chain",
  "permalink": "/corpus/taulib/docs/book-i-sets-universe/is-descending-chain/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.Universe`.",
  "declaration_id": "TauLib.BookI.Sets.Universe::is_descending_chain",
  "declaration_slug": "is-descending-chain",
  "kind": "def",
  "name": "is_descending_chain",
  "module_name": "TauLib.BookI.Sets.Universe",
  "module_url": "/corpus/taulib/docs/book-i-sets-universe/",
  "source_line_start": 92,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L92-L93",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Universe",
        "url": "/corpus/taulib/docs/book-i-sets-universe/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L92-L93",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Sets.Universe](/corpus/taulib/docs/book-i-sets-universe/)
- Source path: [`TauLib/BookI/Sets/Universe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L92-L93)
- Source range: L92-L93
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A descending chain is a function f : Nat → TauIdx such that
    f(n+1) is a strict nonzero member of f(n) for all n. -/
```

## Source Excerpt

```lean
def is_descending_chain (f : Nat → TauIdx) : Prop :=
  ∀ n : Nat, tau_strict_mem_nz (f (n + 1)) (f n)
```
