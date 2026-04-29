---
{
  "projection_kind": "taulib_declaration",
  "title": "SubstrateAbstraction",
  "permalink": "/verify/taulib/docs/book-vi-consumer-identity/substrate-abstraction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Identity`.",
  "declaration_id": "TauLib.BookVI.Consumer.Identity::SubstrateAbstraction",
  "declaration_slug": "substrate-abstraction",
  "kind": "structure",
  "name": "SubstrateAbstraction",
  "module_name": "TauLib.BookVI.Consumer.Identity",
  "module_url": "/verify/taulib/docs/book-vi-consumer-identity/",
  "source_line_start": 91,
  "source_line_end": 102,
  "registry_ids": [
    "VI.T50"
  ],
  "related_registry_items": [
    {
      "id": "VI.T50",
      "title": "Substrate Abstraction",
      "url": "/registry/object/VI.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L91-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Identity",
        "url": "/verify/taulib/docs/book-vi-consumer-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L91-L102",
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

- Module: [TauLib.BookVI.Consumer.Identity](/verify/taulib/docs/book-vi-consumer-identity/)
- Source path: [`TauLib/BookVI/Consumer/Identity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L91-L102)
- Source range: L91-L102
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T50` — Substrate Abstraction

## Immediate Comment / Docstring

```lean
/-- [VI.T50] Substrate Abstraction Theorem.
    The 5 Distinction conditions (VI.D04) + 3 SelfDesc conditions (VI.D08)
    are necessary and sufficient for life, independent of material substrate.
    Proof: (1) Sufficiency: the definitions use only abstract morphisms,
    functors, and winding numbers — no material predicates appear.
    (2) Necessity: failure of any condition produces a counterexample
    (VI.D16 Absence catalog). (3) Independence: VI.L08 shows that
    replacing the material substrate while preserving code + evaluation
    preserves life-equivalence; VI.D53 locates identity in the code.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure SubstrateAbstraction where
  /-- All 8 conditions (5+3) are formulated abstractly. -/
  conditions_abstract : Bool := true
  /-- 8 conditions are sufficient for life. -/
  sufficient : Bool := true
  /-- 8 conditions are necessary for life (Absence catalog). -/
  necessary : Bool := true
  /-- No material predicate appears in any condition. -/
  substrate_independent : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
