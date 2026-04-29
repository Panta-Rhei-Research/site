---
{
  "projection_kind": "taulib_declaration",
  "title": "NecessityResult",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/necessity-result/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::NecessityResult",
  "declaration_slug": "necessity-result",
  "kind": "structure",
  "name": "NecessityResult",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 577,
  "source_line_end": 584,
  "registry_ids": [
    "VII.P08"
  ],
  "related_registry_items": [
    {
      "id": "VII.P08",
      "title": "Each Requirement Independently Necessary",
      "url": "/registry/object/VII.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L577-L584",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L577-L584",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L577-L584)
- Source range: L577-L584
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.P08` — Each Requirement Independently Necessary

## Immediate Comment / Docstring

```lean
/-- [VII.P08] Each Requirement Independently Necessary (ch29).
    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-B4).

    Dropping any single requirement allows non-τ solutions:
    Drop OR1: haecceity categories (non-trivial automorphisms)
    Drop OR2: ZFC (infinitely axiomatized)
    Drop OR3: naive set theory (diagonal paradoxes)
    Drop OR4: non-constructive categories (axiom of choice)
    Drop OR5: purely combinatorial categories (no analytic continuation)
    Drop OR6: non-self-adjoint operator algebras (incomplete spectrum) -/
```

## Source Excerpt

```lean
structure NecessityResult where
  /-- Six counterexamples, one per dropped requirement. -/
  counterexample_count : Nat := 6
  /-- Each counterexample satisfies exactly 5 of 6 requirements. -/
  each_satisfies_five : Bool := true
  /-- No counterexample is equivalent to τ. -/
  none_is_tau : Bool := true
  deriving Repr
```
