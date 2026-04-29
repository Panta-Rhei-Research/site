---
{
  "projection_kind": "taulib_declaration",
  "title": "ConsciousnessMixedSector",
  "permalink": "/verify/taulib/docs/book-vi-mind-consciousness/consciousness-mixed-sector/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Consciousness`.",
  "declaration_id": "TauLib.BookVI.Mind.Consciousness::ConsciousnessMixedSector",
  "declaration_slug": "consciousness-mixed-sector",
  "kind": "structure",
  "name": "ConsciousnessMixedSector",
  "module_name": "TauLib.BookVI.Mind.Consciousness",
  "module_url": "/verify/taulib/docs/book-vi-mind-consciousness/",
  "source_line_start": 105,
  "source_line_end": 112,
  "registry_ids": [
    "VI.T38"
  ],
  "related_registry_items": [
    {
      "id": "VI.T38",
      "title": "Consciousness as Mixed-Sector Self-Modeling",
      "url": "/registry/object/VI.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L105-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L105-L112",
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
- Source path: [`TauLib/BookVI/Mind/Consciousness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Consciousness.lean#L105-L112)
- Source range: L105-L112
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T38` — Consciousness as Mixed-Sector Self-Modeling

## Immediate Comment / Docstring

```lean
/-- [VI.T38] Consciousness = Mixed-Sector Self-Modeling (CROWN JEWEL).
    Consciousness requires Eval² (second-order self-description),
    which is only available in the mixed sector (VI.L07).
    Primitive sectors have Eval¹ only → no self-modeling → no consciousness.
    This is the structural explanation of why consciousness requires
    the consumer sector: both fiber generators must be active
    for the evaluator to model itself. -/
```

## Source Excerpt

```lean
structure ConsciousnessMixedSector where
  /-- Requires second-order evaluation Eval². -/
  requires_eval_squared : Bool := true
  /-- Only mixed sector supports Eval². -/
  only_mixed_sector : Bool := true
  /-- Primitive sectors excluded. -/
  primitive_excluded : Bool := true
  deriving Repr
```
