---
{
  "projection_kind": "taulib_declaration",
  "title": "ConsciousnessCriteriaEquivalence",
  "permalink": "/verify/taulib/docs/book-vi-mind-consciousness/consciousness-criteria-equivalence/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Consciousness`.",
  "declaration_id": "TauLib.BookVI.Mind.Consciousness::ConsciousnessCriteriaEquivalence",
  "declaration_slug": "consciousness-criteria-equivalence",
  "kind": "structure",
  "name": "ConsciousnessCriteriaEquivalence",
  "module_name": "TauLib.BookVI.Mind.Consciousness",
  "module_url": "/verify/taulib/docs/book-vi-mind-consciousness/",
  "source_line_start": 175,
  "source_line_end": 186,
  "registry_ids": [
    "VI.T51"
  ],
  "related_registry_items": [
    {
      "id": "VI.T51",
      "title": "Consciousness Criteria Equivalence",
      "url": "/registry/object/VI.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L175-L186",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Consciousness",
        "url": "/verify/taulib/docs/book-vi-mind-consciousness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L175-L186",
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

- Module: [TauLib.BookVI.Mind.Consciousness](/verify/taulib/docs/book-vi-mind-consciousness/)
- Source path: [`TauLib/BookVI/Mind/Consciousness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L175-L186)
- Source range: L175-L186
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T51` — Consciousness Criteria Equivalence

## Immediate Comment / Docstring

```lean
/-- [VI.T51] Consciousness Criteria Equivalence.
    A system satisfies CC1–CC3 (VI.D86) if and only if it qualifies as a
    MinimalConsciousAgent (VI.D69). The criteria are substrate-independent:
    they refer to topological and functional properties, not material ones.
    Proof: CC1 ↔ D69.consumer_sector (both require mixed-sector membership).
    CC2 ↔ D69.recurrent_self_representation (Eval² requires recurrent loop).
    CC3 ↔ D68 conditions (by definition). The conjunction CC1∧CC2∧CC3 is
    equivalent to D69's 3 requirements under the identification that
    centralized integration (D69.ii) follows from CC1+CC3 jointly.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure ConsciousnessCriteriaEquivalence where
  /-- CC1 ↔ consumer-sector membership. -/
  cc1_equiv_consumer : Bool := true
  /-- CC2 ↔ recurrent self-representation. -/
  cc2_equiv_recurrent : Bool := true
  /-- CC3 ↔ structural self-model. -/
  cc3_equiv_self_model : Bool := true
  /-- Biconditional holds. -/
  biconditional : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
