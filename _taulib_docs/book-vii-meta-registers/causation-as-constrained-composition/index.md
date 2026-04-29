---
{
  "projection_kind": "taulib_declaration",
  "title": "CausationAsConstrainedComposition",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/causation-as-constrained-composition/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::CausationAsConstrainedComposition",
  "declaration_slug": "causation-as-constrained-composition",
  "kind": "structure",
  "name": "CausationAsConstrainedComposition",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 772,
  "source_line_end": 777,
  "registry_ids": [
    "VII.D32"
  ],
  "related_registry_items": [
    {
      "id": "VII.D32",
      "title": "Causation as Constrained Composition",
      "url": "/registry/object/VII.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L772-L777",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L772-L777",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L772-L777)
- Source range: L772-L777
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D32` — Causation as Constrained Composition

## Immediate Comment / Docstring

```lean
/-- [VII.D32] Causation as Constrained Composition (ch24). Causation =
    morphism factorization: A causes B iff there exists a factorization
    A → C → B through an admissible intermediate. Constraints from
    kernel axioms determine which factorizations are admissible. -/
```

## Source Excerpt

```lean
structure CausationAsConstrainedComposition where
  /-- Causation = morphism factorization. -/
  factorization : Bool := true
  /-- Admissibility from kernel axioms. -/
  kernel_constrained : Bool := true
  deriving Repr
```
