---
{
  "projection_kind": "taulib_declaration",
  "title": "SaturationResult",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/saturation-result/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::SaturationResult",
  "declaration_slug": "saturation-result",
  "kind": "structure",
  "name": "SaturationResult",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 305,
  "source_line_end": 315,
  "registry_ids": [
    "VII.T06"
  ],
  "related_registry_items": [
    {
      "id": "VII.T06",
      "title": "Saturation Theorem",
      "url": "/registry/object/VII.T06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L305-L315",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L305-L315",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L305-L315)
- Source range: L305-L315
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T06` — Saturation Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T06] Saturation Theorem: Enrich(E₃) = E₃. No E₄ exists.
    Three conditions for genuine E₄ ALL blocked:
    1. No new generator (no_new_lobe, L05)
    2. No new mediator (no_new_crossing_mediator, L06)
    3. No new carrier (carrier_closure, L07)

    Consequence: enrichment series is complete at E₃. -/
```

## Source Excerpt

```lean
structure SaturationResult where
  /-- E₃ is terminal. -/
  terminal_layer : EnrichLayer
  terminal_eq : terminal_layer = .e3
  /-- Three blocking conditions satisfied. -/
  no_new_lobe_blocked : Bool := true
  no_new_mediator_blocked : Bool := true
  no_new_carrier_blocked : Bool := true
  /-- All three blocked ⟹ saturation. -/
  saturated : Bool := true
  deriving Repr
```
