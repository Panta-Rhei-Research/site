---
{
  "projection_kind": "taulib_declaration",
  "title": "EnrichmentLevel",
  "permalink": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/enrichment-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::EnrichmentLevel",
  "declaration_slug": "enrichment-level",
  "kind": "inductive",
  "name": "EnrichmentLevel",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 54,
  "source_line_end": 57,
  "registry_ids": [
    "II.D58"
  ],
  "related_registry_items": [
    {
      "id": "II.D58",
      "title": "E0/E1 Transition",
      "url": "/registry/object/II.D58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L54-L57",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.EnrichmentLadder",
        "url": "/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L54-L57",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookII.Enrichment.EnrichmentLadder](/corpus/taulib/docs/book-ii-enrichment-enrichment-ladder/)
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L54-L57)
- Source range: L54-L57
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `II.D58` — E0/E1 Transition

## Immediate Comment / Docstring

```lean
/-- [II.D58] Enrichment levels. E0 is the base category (Book I).
    E1 is the self-enriched category (Book II). -/
```

## Source Excerpt

```lean
inductive EnrichmentLevel where
  | E0 : EnrichmentLevel
  | E1 : EnrichmentLevel
  deriving Repr, DecidableEq
```
