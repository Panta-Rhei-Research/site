---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalLadder",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/canonical-ladder/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::CanonicalLadder",
  "declaration_slug": "canonical-ladder",
  "kind": "structure",
  "name": "CanonicalLadder",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 109,
  "source_line_end": 120,
  "registry_ids": [
    "VII.T05"
  ],
  "related_registry_items": [
    {
      "id": "VII.T05",
      "title": "Canonical Ladder Theorem",
      "url": "/registry/object/VII.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L109-L120",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L109-L120",
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
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L109-L120)
- Source range: L109-L120
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.T05` — Canonical Ladder Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T05] Canonical Ladder: non-empty at every layer, strictly increasing,
    terminated by Saturation Theorem, and canonical (determined by structure
    of kernel and five generators, not editorial choice).

    Enrichment equations:
    - E₁ = Enrich(E₀): sector admissibility on NF objects
    - E₂ = Enrich(E₁): SelfDesc on sectors
    - E₃ = Enrich(E₂): SelfDesc² on self-describing codes -/
```

## Source Excerpt

```lean
structure CanonicalLadder where
  layer_count : Nat
  count_eq : layer_count = 4
  /-- Non-empty at each level. -/
  non_empty : Bool := true
  /-- Strictly increasing. -/
  strict : Bool := true
  /-- Saturating at E₃. -/
  saturating : Bool := true
  /-- Canonical: structurally determined. -/
  canonical : Bool := true
  deriving Repr
```
