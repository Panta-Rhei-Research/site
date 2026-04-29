---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_layer",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/e2-layer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::e2_layer",
  "declaration_slug": "e2-layer",
  "kind": "def",
  "name": "e2_layer",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 202,
  "source_line_end": 228,
  "registry_ids": [
    "III.D08",
    "III.D09"
  ],
  "related_registry_items": [
    {
      "id": "III.D08",
      "title": "E₂ Layer (Computation)",
      "url": "/registry/object/III.D08/"
    },
    {
      "id": "III.D09",
      "title": "E₃ Layer (Metaphysics)",
      "url": "/registry/object/III.D09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L202-L228",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L202-L228",
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
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L202-L228)
- Source range: L202-L228
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D08` — E₂ Layer (Computation)
- `III.D09` — E₃ Layer (Metaphysics)

## Immediate Comment / Docstring

```lean
/-- [III.D08] E₂ Layer: the computation layer (Book VI).
    - Carrier: self-referential codes (address = program)
    - Predicate: operational closure (D(C) produces another code)
    - Decoder: phenotype map (code → observable behavior)
    - Invariant: error-correction capacity

    At E₂, the code IS a τ-address. The τ-Tower Machine (TTM)
    from Book I is the structural template. -/
```

## Source Excerpt

```lean
def e2_layer (bound db : TauIdx) : LayerTemplate :=
  { carrier_check := fun x k =>
      -- Self-referential code: x is both address and program
      -- At E₂, every τ-address IS a code (code = data nativity)
      reduce x k == x || x >= primorial k
  , predicate_check := fun x k =>
      -- Operational closure: applying decoder to code produces another code
      -- D(C) = reduce(C, k-1) is always a valid code at stage k-1
      k == 0 || reduce x (k - 1) < primorial (k - 1) || primorial (k - 1) == 0
  , decoder := fun x k =>
      -- Phenotype map: observable behavior = value at stage k
      reduce x k
  , invariant_check := fun x k =>
      -- Error-correction: the code is self-correcting under reduce
      -- reduce(reduce(x, k), k) = reduce(x, k)
      reduce (reduce x k) k == reduce x k
  }

-- ============================================================
-- E₃ LAYER (METAPHYSICS) [III.D09]
-- ============================================================

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
