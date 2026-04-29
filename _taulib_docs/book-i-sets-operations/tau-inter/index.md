---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_inter",
  "permalink": "/verify/taulib/docs/book-i-sets-operations/tau-inter/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.Operations`.",
  "declaration_id": "TauLib.BookI.Sets.Operations::tau_inter",
  "declaration_slug": "tau-inter",
  "kind": "def",
  "name": "tau_inter",
  "module_name": "TauLib.BookI.Sets.Operations",
  "module_url": "/verify/taulib/docs/book-i-sets-operations/",
  "source_line_start": 42,
  "source_line_end": 42,
  "registry_ids": [
    "I.D32"
  ],
  "related_registry_items": [
    {
      "id": "I.D32",
      "title": "Set-Theoretic Operations",
      "url": "/registry/object/I.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L42-L42",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L42-L42",
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

- Module: [TauLib.BookI.Sets.Operations](/verify/taulib/docs/book-i-sets-operations/)
- Source path: [`TauLib/BookI/Sets/Operations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Operations.lean#L42-L42)
- Source range: L42-L42
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D32` — Set-Theoretic Operations

## Immediate Comment / Docstring

```lean
/-- [I.D32] τ-intersection: gcd encodes set intersection under divisibility membership. -/
```

## Source Excerpt

```lean
def tau_inter (a b : TauIdx) : TauIdx := idx_gcd a b
```
