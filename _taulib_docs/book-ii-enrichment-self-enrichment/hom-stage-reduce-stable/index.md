---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_stage_reduce_stable",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-stage-reduce-stable/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_stage_reduce_stable",
  "declaration_slug": "hom-stage-reduce-stable",
  "kind": "theorem",
  "name": "hom_stage_reduce_stable",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 343,
  "source_line_end": 346,
  "registry_ids": [
    "II.D53"
  ],
  "related_registry_items": [
    {
      "id": "II.D53",
      "title": "Self-Enrichment Structure",
      "url": "/registry/object/II.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L343-L346",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfEnrichment",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L343-L346",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.Enrichment.SelfEnrichment](/verify/taulib/docs/book-ii-enrichment-self-enrichment/)
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L343-L346)
- Source range: L343-L346
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D53` — Self-Enrichment Structure

## Immediate Comment / Docstring

```lean
/-- [II.D53] Formal proof: hom_stage is reduce-stable.
    reduce(hom_stage(a, b, k), k) = hom_stage(a, b, k).
    This follows from reduce(reduce(x, k), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
theorem hom_stage_reduce_stable (a b k : TauIdx) :
    reduce (hom_stage a b k) k = hom_stage a b k := by
  simp only [hom_stage, reduce]
  exact Nat.mod_mod_of_dvd _ (dvd_refl (primorial k))
```
