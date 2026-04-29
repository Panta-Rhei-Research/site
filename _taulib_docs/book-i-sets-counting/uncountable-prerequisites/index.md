---
{
  "projection_kind": "taulib_declaration",
  "title": "UncountablePrerequisites",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/uncountable-prerequisites/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::UncountablePrerequisites",
  "declaration_slug": "uncountable-prerequisites",
  "kind": "structure",
  "name": "UncountablePrerequisites",
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 114,
  "source_line_end": 125,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L114-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Counting",
        "url": "/verify/taulib/docs/book-i-sets-counting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L114-L125",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.Sets.Counting](/verify/taulib/docs/book-i-sets-counting/)
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L114-L125)
- Source range: L114-L125
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- An uncountability argument requires three structural prerequisites.
    This record witnesses the absence of each from K0-K6. -/
```

## Source Excerpt

```lean
structure UncountablePrerequisites where
  /-- P1: Impredicative powerset -- would require collecting ALL subsets
      of an infinite set, but tau-sets are divisor sets (always finite for
      nonzero indices). -/
  no_impredicative_powerset : Prop
  /-- P2: Unrestricted comprehension -- would require
      Sep : (TauIdx -> Prop) -> TauIdx, but no such separator exists. -/
  no_comprehension : Prop
  /-- P3: Free Cartesian diagonal -- would require
      Delta : TauIdx -> TauIdx x TauIdx as an earned morphism,
      but self-pairing is not in the program monoid. -/
  no_free_diagonal : Prop
```
