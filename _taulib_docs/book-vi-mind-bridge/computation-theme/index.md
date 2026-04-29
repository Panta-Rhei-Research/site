---
{
  "projection_kind": "taulib_declaration",
  "title": "ComputationTheme",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/computation-theme/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::ComputationTheme",
  "declaration_slug": "computation-theme",
  "kind": "structure",
  "name": "ComputationTheme",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 118,
  "source_line_end": 125,
  "registry_ids": [
    "VI.R24"
  ],
  "related_registry_items": [
    {
      "id": "VI.R24",
      "title": "Computation Theme Across the Book",
      "url": "/registry/object/VI.R24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L118-L125",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/verify/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L118-L125",
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

- Module: [TauLib.BookVI.Mind.Bridge](/verify/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L118-L125)
- Source range: L118-L125
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.R24` — Computation Theme Across the Book

## Immediate Comment / Docstring

```lean
/-- [VI.R24] Computation Theme: recurring pattern across Book VI.
    The τ³ computer (VI.D52), PPAS optimizer (VI.D50), and
    ω-germ evaluator all instantiate the same Turing-complete
    computation theme at different enrichment levels. -/
```

## Source Excerpt

```lean
structure ComputationTheme where
  /-- Theme recurs across levels. -/
  recurring : Bool := true
  /-- Instances: τ³ computer, PPAS, evaluator. -/
  instance_count : Nat
  /-- At least 3 instances. -/
  count_eq : instance_count = 3
  deriving Repr
```
