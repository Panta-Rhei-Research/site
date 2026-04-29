---
{
  "projection_kind": "taulib_declaration",
  "title": "SignatureRigidity",
  "permalink": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/signature-rigidity/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.ConsumerMixer`.",
  "declaration_id": "TauLib.BookVI.Consumer.ConsumerMixer::SignatureRigidity",
  "declaration_slug": "signature-rigidity",
  "kind": "structure",
  "name": "SignatureRigidity",
  "module_name": "TauLib.BookVI.Consumer.ConsumerMixer",
  "module_url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/",
  "source_line_start": 79,
  "source_line_end": 92,
  "registry_ids": [
    "VI.T25"
  ],
  "related_registry_items": [
    {
      "id": "VI.T25",
      "title": "Signature Rigidity Determines Uniqueness",
      "url": "/registry/object/VI.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L79-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.ConsumerMixer",
        "url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L79-L92",
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

- Module: [TauLib.BookVI.Consumer.ConsumerMixer](/verify/taulib/docs/book-vi-consumer-consumer-mixer/)
- Source path: [`TauLib/BookVI/Consumer/ConsumerMixer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L79-L92)
- Source range: L79-L92
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T25` — Signature Rigidity Determines Uniqueness

## Immediate Comment / Docstring

```lean
/-- [VI.T25] Signature Rigidity Determines Uniqueness.
    Among the 10 possible generator pairings on τ³:
    - base–base (α,π): both base → no fiber innovation → unstable
    - base–fiber (α,π') etc.: mixed base+fiber → partial → unstable
    - fiber–fiber (π',π''): both fiber generators → full T² coverage → stable
    Only (π',π'') yields a stable mixed sector. -/
```

## Source Excerpt

```lean
structure SignatureRigidity where
  /-- Total possible pairings from 5 generators taken 2. -/
  total_pairings : Nat
  /-- Only fiber–fiber is stable. -/
  base_base_stable : Bool := false
  /-- Base–fiber pairings unstable. -/
  base_fiber_stable : Bool := false
  /-- Fiber–fiber pairing stable (π',π'' only). -/
  fiber_fiber_stable : Bool := true
  /-- Stable pairings count. -/
  stable_count : Nat
  /-- Exactly 1 stable pairing. -/
  stable_eq : stable_count = 1
  deriving Repr
```
