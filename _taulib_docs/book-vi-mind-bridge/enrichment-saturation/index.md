---
{
  "projection_kind": "taulib_declaration",
  "title": "EnrichmentSaturation",
  "permalink": "/verify/taulib/docs/book-vi-mind-bridge/enrichment-saturation/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Mind.Bridge`.",
  "declaration_id": "TauLib.BookVI.Mind.Bridge::EnrichmentSaturation",
  "declaration_slug": "enrichment-saturation",
  "kind": "structure",
  "name": "EnrichmentSaturation",
  "module_name": "TauLib.BookVI.Mind.Bridge",
  "module_url": "/verify/taulib/docs/book-vi-mind-bridge/",
  "source_line_start": 41,
  "source_line_end": 50,
  "registry_ids": [
    "VI.T37"
  ],
  "related_registry_items": [
    {
      "id": "VI.T37",
      "title": "Enrichment Saturation Theorem",
      "url": "/registry/object/VI.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L41-L50",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Mind.Bridge",
        "url": "/verify/taulib/docs/book-vi-mind-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L41-L50",
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

- Module: [TauLib.BookVI.Mind.Bridge](/verify/taulib/docs/book-vi-mind-bridge/)
- Source path: [`TauLib/BookVI/Mind/Bridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Mind/Bridge.lean#L41-L50)
- Source range: L41-L50
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T37` — Enrichment Saturation Theorem

## Immediate Comment / Docstring

```lean
/-- [VI.T37] Enrichment Saturation: E₄ collapses to E₃.
    The enrichment ladder E₁ (chemistry) → E₂ (life) →
    E₃ (consciousness) → E₄ (?) saturates at 4 layers.
    E₄ does not produce a genuinely new enrichment layer;
    it collapses back to E₃. Scope: conjectural. -/
```

## Source Excerpt

```lean
structure EnrichmentSaturation where
  /-- Total enrichment layers before saturation. -/
  layer_count : Nat
  /-- Exactly 4 layers (E₁–E₄, but E₄ collapses). -/
  count_eq : layer_count = 4
  /-- E₄ collapses (does not generate new layer). -/
  e4_collapses : Bool := true
  /-- Scope: conjectural (not yet τ-effective). -/
  scope : String := "conjectural"
  deriving Repr
```
