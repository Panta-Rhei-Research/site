---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_stage",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-stage/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_stage",
  "declaration_slug": "hom-stage",
  "kind": "def",
  "name": "hom_stage",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 51,
  "source_line_end": 52,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L51-L52",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L51-L52",
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

- Module: [TauLib.BookII.Enrichment.SelfEnrichment](/verify/taulib/docs/book-ii-enrichment-self-enrichment/)
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L51-L52)
- Source range: L51-L52
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D53` — Self-Enrichment Structure

## Immediate Comment / Docstring

```lean
/-- [II.D53] Self-enrichment structure: hom-space at stage k.
    hom_stage(a, b, k) = reduce(a, k) applied to b at stage k.
    This represents the evaluation of the canonical hom-map:
    the set of reduce-compatible maps on Z/P_kZ forms a τ-object
    because it is itself closed under stage reduction. -/
```

## Source Excerpt

```lean
def hom_stage (a b k : TauIdx) : TauIdx :=
  reduce (reduce a k + reduce b k) k
```
