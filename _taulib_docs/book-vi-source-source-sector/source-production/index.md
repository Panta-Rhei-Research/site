---
{
  "projection_kind": "taulib_declaration",
  "title": "SourceProduction",
  "permalink": "/verify/taulib/docs/book-vi-source-source-sector/source-production/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.SourceSector`.",
  "declaration_id": "TauLib.BookVI.Source.SourceSector::SourceProduction",
  "declaration_slug": "source-production",
  "kind": "structure",
  "name": "SourceProduction",
  "module_name": "TauLib.BookVI.Source.SourceSector",
  "module_url": "/verify/taulib/docs/book-vi-source-source-sector/",
  "source_line_start": 104,
  "source_line_end": 111,
  "registry_ids": [
    "VI.T20"
  ],
  "related_registry_items": [
    {
      "id": "VI.T20",
      "title": "Source as γ-Fiber Production",
      "url": "/registry/object/VI.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L104-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.SourceSector",
        "url": "/verify/taulib/docs/book-vi-source-source-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L104-L111",
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

- Module: [TauLib.BookVI.Source.SourceSector](/verify/taulib/docs/book-vi-source-source-sector/)
- Source path: [`TauLib/BookVI/Source/SourceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/SourceSector.lean#L104-L111)
- Source range: L104-L111
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T20` — Source as γ-Fiber Production

## Immediate Comment / Docstring

```lean
/-- [VI.T20] Source = π'-Fiber Production Theorem.
    A source Life loop has nontrivial π'-winding on the fiber
    with net positive structure generation. -/
```

## Source Excerpt

```lean
structure SourceProduction where
  /-- Winding on π' (fiber). -/
  winding_pi_prime : Nat
  /-- Winding is nontrivial (≥ 1). -/
  pi_prime_nontrivial : winding_pi_prime ≥ 1
  /-- Net structure generation. -/
  net_generation : Bool := true
  deriving Repr
```
