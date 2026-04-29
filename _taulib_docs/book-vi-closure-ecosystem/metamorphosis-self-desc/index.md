---
{
  "projection_kind": "taulib_declaration",
  "title": "MetamorphosisSelfDesc",
  "permalink": "/verify/taulib/docs/book-vi-closure-ecosystem/metamorphosis-self-desc/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Closure.Ecosystem`.",
  "declaration_id": "TauLib.BookVI.Closure.Ecosystem::MetamorphosisSelfDesc",
  "declaration_slug": "metamorphosis-self-desc",
  "kind": "structure",
  "name": "MetamorphosisSelfDesc",
  "module_name": "TauLib.BookVI.Closure.Ecosystem",
  "module_url": "/verify/taulib/docs/book-vi-closure-ecosystem/",
  "source_line_start": 122,
  "source_line_end": 129,
  "registry_ids": [
    "VI.P17"
  ],
  "related_registry_items": [
    {
      "id": "VI.P17",
      "title": "Metamorphosis Preserves SelfDesc",
      "url": "/registry/object/VI.P17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L122-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Closure.Ecosystem",
        "url": "/verify/taulib/docs/book-vi-closure-ecosystem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L122-L129",
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

- Module: [TauLib.BookVI.Closure.Ecosystem](/verify/taulib/docs/book-vi-closure-ecosystem/)
- Source path: [`TauLib/BookVI/Closure/Ecosystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Closure/Ecosystem.lean#L122-L129)
- Source range: L122-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.P17` — Metamorphosis Preserves SelfDesc

## Immediate Comment / Docstring

```lean
/-- [VI.P17] Metamorphosis Preserves SelfDesc.
    ω-germ codes are identical in larva and adult;
    SelfDesc holds at every instant of metamorphosis.
    The code is a profinite invariant (Book II, Part X) that
    persists through substrate replacement. -/
```

## Source Excerpt

```lean
structure MetamorphosisSelfDesc where
  /-- ω-germ code preserved across metamorphosis. -/
  code_preserved : Bool := true
  /-- SelfDesc holds at every instant. -/
  selfdesc_continuous : Bool := true
  /-- Code is profinite invariant (Book II, Part X). -/
  profinite_invariant : Bool := true
  deriving Repr
```
