---
{
  "projection_kind": "taulib_declaration",
  "title": "NonDissEndomorphism",
  "permalink": "/verify/taulib/docs/book-iv-many-body-nflboundary/non-diss-endomorphism/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.ManyBody.NFLBoundary`.",
  "declaration_id": "TauLib.BookIV.ManyBody.NFLBoundary::NonDissEndomorphism",
  "declaration_slug": "non-diss-endomorphism",
  "kind": "structure",
  "name": "NonDissEndomorphism",
  "module_name": "TauLib.BookIV.ManyBody.NFLBoundary",
  "module_url": "/verify/taulib/docs/book-iv-many-body-nflboundary/",
  "source_line_start": 48,
  "source_line_end": 55,
  "registry_ids": [
    "IV.D390"
  ],
  "related_registry_items": [
    {
      "id": "IV.D390",
      "title": "Non-Dissipative Endomorphism",
      "url": "/registry/object/IV.D390/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L48-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.ManyBody.NFLBoundary",
        "url": "/verify/taulib/docs/book-iv-many-body-nflboundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L48-L55",
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

- Module: [TauLib.BookIV.ManyBody.NFLBoundary](/verify/taulib/docs/book-iv-many-body-nflboundary/)
- Source path: [`TauLib/BookIV/ManyBody/NFLBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/ManyBody/NFLBoundary.lean#L48-L55)
- Source range: L48-L55
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D390` — Non-Dissipative Endomorphism

## Immediate Comment / Docstring

```lean
/-- [IV.D390] An endomorphism Φ: H_∂ → H_∂ is non-dissipative if it
    preserves all clopen ideals: Φ(I) = I for every clopen ideal I.
    A dissipative endomorphism strictly shrinks at least one ideal. -/
```

## Source Excerpt

```lean
structure NonDissEndomorphism where
  /-- Preserves all clopen ideals. -/
  preserves_clopen : Bool := true
  /-- Dissipative = strictly shrinks some ideal. -/
  dissipative_shrinks : Bool := true
  /-- Acts on boundary character algebra H_∂. -/
  domain : String := "H_∂"
  deriving Repr
```
