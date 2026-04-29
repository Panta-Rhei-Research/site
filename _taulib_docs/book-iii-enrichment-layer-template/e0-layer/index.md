---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_layer",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/e0-layer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::e0_layer",
  "declaration_slug": "e0-layer",
  "kind": "def",
  "name": "e0_layer",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 141,
  "source_line_end": 151,
  "registry_ids": [
    "III.D06"
  ],
  "related_registry_items": [
    {
      "id": "III.D06",
      "title": "E₀ Layer (Mathematics)",
      "url": "/registry/object/III.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L141-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L141-L151",
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
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L141-L151)
- Source range: L141-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D06` — E₀ Layer (Mathematics)

## Immediate Comment / Docstring

```lean
/-- [III.D06] E₀ Layer: the mathematical kernel (Books I-III).
    - Carrier: τ-objects with NF addressing (x < P_k)
    - Predicate: NF-addressability (reduce is identity on valid elements)
    - Decoder: peel map Φ — ABCD extraction
    - Invariant: holomorphic structure (reduce-compatibility) -/
```

## Source Excerpt

```lean
def e0_layer (bound db : TauIdx) : LayerTemplate :=
  { carrier_check := fun x k => x < primorial k
  , predicate_check := fun x k => reduce x k == x
  , decoder := fun x _k =>
      -- ABCD peel: extract the A-coordinate (first prime factor contribution)
      -- nth_prime is 1-indexed in TauLib (nth_prime 0 = 0, nth_prime 1 = 2)
      x % 2
  , invariant_check := fun x k =>
      -- Holomorphic: reduce(reduce(x, k), k) = reduce(x, k)
      reduce (reduce x k) k == reduce x k
  }
```
