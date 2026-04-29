---
{
  "projection_kind": "taulib_declaration",
  "title": "ConsumerMixer",
  "permalink": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/consumer-mixer/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.ConsumerMixer`.",
  "declaration_id": "TauLib.BookVI.Consumer.ConsumerMixer::ConsumerMixer",
  "declaration_slug": "consumer-mixer",
  "kind": "structure",
  "name": "ConsumerMixer",
  "module_name": "TauLib.BookVI.Consumer.ConsumerMixer",
  "module_url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/",
  "source_line_start": 37,
  "source_line_end": 50,
  "registry_ids": [
    "VI.D46"
  ],
  "related_registry_items": [
    {
      "id": "VI.D46",
      "title": "Consumer Mixer on (γ, η)",
      "url": "/registry/object/VI.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L37-L50",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L37-L50",
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
- Source path: [`TauLib/BookVI/Consumer/ConsumerMixer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L37-L50)
- Source range: L37-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D46` — Consumer Mixer on (γ, η)

## Immediate Comment / Docstring

```lean
/-- [VI.D46] Consumer Mixer on (π', π''): mixed-sector pairing
    of both fiber generators. The only non-primitive sector.
    Generator pair: (π', π'') on fiber T² (Book I, Part I).
    Winding: π₁(T²) ≅ ℤ × ℤ gives two independent winding numbers
    (Book II, Part II). Both must be nontrivial. -/
```

## Source Excerpt

```lean
structure ConsumerMixer where
  /-- Generator pair label. -/
  generator_pair : String := "pi_prime_pi_double_prime"
  /-- Mixed sector (not primitive). -/
  is_mixed : Bool := true
  /-- Winding number on π' (must be ≥ 1). -/
  winding_pi_prime : Nat
  /-- Winding number on π'' (must be ≥ 1). -/
  winding_pi_double : Nat
  /-- π' winding nontrivial. -/
  pi_prime_nontrivial : winding_pi_prime ≥ 1
  /-- π'' winding nontrivial. -/
  pi_double_nontrivial : winding_pi_double ≥ 1
  deriving Repr
```
