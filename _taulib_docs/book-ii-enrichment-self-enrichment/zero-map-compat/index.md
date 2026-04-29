---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_map_compat",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/zero-map-compat/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::zero_map_compat",
  "declaration_slug": "zero-map-compat",
  "kind": "theorem",
  "name": "zero_map_compat",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 368,
  "source_line_end": 372,
  "registry_ids": [
    "II.D54"
  ],
  "related_registry_items": [
    {
      "id": "II.D54",
      "title": "Hom Object",
      "url": "/registry/object/II.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L368-L372",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L368-L372",
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
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L368-L372)
- Source range: L368-L372
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D54` — Hom Object

## Immediate Comment / Docstring

```lean
/-- [II.D54] Formal proof: the constant 0 map is reduce-compatible.
    reduce(0, k) = 0 for all k, so the zero map trivially satisfies
    f(reduce(x, k)) = reduce(f(x), k). -/
```

## Source Excerpt

```lean
theorem zero_map_compat (_x k : TauIdx) :
    reduce (0 : TauIdx) k = (0 : TauIdx) := by
  simp [reduce, Nat.zero_mod]

end Tau.BookII.Enrichment
```
