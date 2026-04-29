---
{
  "projection_kind": "taulib_declaration",
  "title": "TwistorEmbedding",
  "permalink": "/verify/taulib/docs/book-v-orthodox-other-approaches/twistor-embedding/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.OtherApproaches`.",
  "declaration_id": "TauLib.BookV.Orthodox.OtherApproaches::TwistorEmbedding",
  "declaration_slug": "twistor-embedding",
  "kind": "structure",
  "name": "TwistorEmbedding",
  "module_name": "TauLib.BookV.Orthodox.OtherApproaches",
  "module_url": "/verify/taulib/docs/book-v-orthodox-other-approaches/",
  "source_line_start": 168,
  "source_line_end": 177,
  "registry_ids": [
    "V.P105"
  ],
  "related_registry_items": [
    {
      "id": "V.P105",
      "title": "Twistor embedding",
      "url": "/registry/object/V.P105/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L168-L177",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.OtherApproaches",
        "url": "/verify/taulib/docs/book-v-orthodox-other-approaches/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L168-L177",
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

- Module: [TauLib.BookV.Orthodox.OtherApproaches](/verify/taulib/docs/book-v-orthodox-other-approaches/)
- Source path: [`TauLib/BookV/Orthodox/OtherApproaches.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/OtherApproaches.lean#L168-L177)
- Source range: L168-L177
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P105` — Twistor embedding

## Immediate Comment / Docstring

```lean
/-- [V.P105] Twistor embedding: the Penrose transform for massless
    fields on Minkowski space embeds into the E1 readout.

    H^1(PT, O(n)) embeds into the massless sector of the boundary
    holonomy algebra. Twistor theory captures the base-circle
    (temporal) structure but misses the fiber T^2 (mass, confinement).

    This is a partial embedding, not an equivalence. -/
```

## Source Excerpt

```lean
structure TwistorEmbedding where
  /-- Embedding is well-defined for massless fields. -/
  massless_defined : Bool := true
  /-- Does NOT extend to massive fields. -/
  massive_defined : Bool := false
  /-- Captures base circle structure. -/
  captures_base : Bool := true
  /-- Misses fiber T^2 structure. -/
  misses_fiber : Bool := true
  deriving Repr
```
