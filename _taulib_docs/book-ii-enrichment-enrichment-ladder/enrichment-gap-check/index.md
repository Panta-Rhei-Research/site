---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_gap_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/enrichment-gap-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::enrichment_gap_check",
  "declaration_slug": "enrichment-gap-check",
  "kind": "def",
  "name": "enrichment_gap_check",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 215,
  "source_line_end": 220,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L215-L220",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.EnrichmentLadder",
        "url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L215-L220",
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

- Module: [TauLib.BookII.Enrichment.EnrichmentLadder](/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/)
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L215-L220)
- Source range: L215-L220
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D58` — E0/E1 Transition

## Immediate Comment / Docstring

```lean
/-- [II.D58] Enrichment gap check:
    E1 is strictly richer than E0.

    At E1, the hom-counts form a tower (internal tau-object):
    count_k projects to count_{k-1} via the restriction map.
    At E0, there is no such tower structure -- the counts are just
    external natural numbers with no inter-stage coherence.

    The gap is witnessed by the self-enrichment component:
    E1 has Hom objects that are themselves tau-objects, which is
    data that E0 cannot express (E0 has no notion of "internal object"). -/
```

## Source Excerpt

```lean
def enrichment_gap_check (bound db k_max : TauIdx) : Bool :=
  let e1_self := e1_self_enrichment_witness bound db
  let e1_full := e1_layer_check bound db k_max
  let e0_external := e0_external_hom_check db
  let tower_structure := e1_internal_hom_check db
  e0_external && e1_self && e1_full && tower_structure
```
