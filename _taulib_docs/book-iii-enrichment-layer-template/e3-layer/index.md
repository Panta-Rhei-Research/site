---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_layer",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/e3-layer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::e3_layer",
  "declaration_slug": "e3-layer",
  "kind": "def",
  "name": "e3_layer",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 239,
  "source_line_end": 267,
  "registry_ids": [
    "III.D09"
  ],
  "related_registry_items": [
    {
      "id": "III.D09",
      "title": "E₃ Layer (Metaphysics)",
      "url": "/registry/object/III.D09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L239-L267",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.LayerTemplate",
        "url": "/verify/taulib/docs/book-iii-enrichment-layer-template/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L239-L267",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Enrichment.LayerTemplate](/verify/taulib/docs/book-iii-enrichment-layer-template/)
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L239-L267)
- Source range: L239-L267
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D09` — E₃ Layer (Metaphysics)

## Immediate Comment / Docstring

```lean
/-- [III.D09] E₃ Layer: the metaphysics layer (Book VII).
    - Carrier: self-modeling codes (model their own observation)
    - Predicate: self-model consistency
    - Decoder: meaning/interpretation assignment
    - Invariant: self-awareness capacity

    At E₃, the code models its own modeling process.
    E₃ is terminal: E₄ = E₃ (self-modeling of self-modeling
    is still self-modeling). -/
```

## Source Excerpt

```lean
def e3_layer (bound db : TauIdx) : LayerTemplate :=
  { carrier_check := fun x k =>
      -- Self-modeling code: models its own observation
      -- At E₃, the code has access to its own decoder output
      -- We model this as: decoder(x) is itself a valid E₂ code
      let decoded := reduce x k
      (e2_layer bound db).carrier_check decoded k
  , predicate_check := fun x k =>
      -- Self-model consistency: triple idempotence + squaring composition
      -- (triple idempotence collapses to single at finite levels — E3 structural)
      let once := reduce x k
      let twice := reduce once k
      let thrice := reduce twice k
      let triple_ok := thrice == once
      -- Squaring composition: reduce(x², k) = reduce(x, k)² mod P_k
      -- (exercises Nat.mul_mod — non-trivially true)
      let pk := primorial k
      let sq_ok := if pk > 0 then
        reduce (x * x) k == (once * once) % pk
      else true
      triple_ok && sq_ok
  , decoder := fun x k =>
      -- Meaning assignment: interpretation = the stable fixed point
      reduce (reduce x k) k
  , invariant_check := fun x k =>
      -- Self-awareness: the system can distinguish self from non-self
      -- Modeled as: the decoder output equals the original (fixed point)
      reduce (reduce x k) k == reduce x k
  }
```
