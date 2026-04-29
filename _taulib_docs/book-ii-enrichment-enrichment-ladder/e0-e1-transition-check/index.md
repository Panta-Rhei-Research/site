---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_e1_transition_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-e1-transition-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::e0_e1_transition_check",
  "declaration_slug": "e0-e1-transition-check",
  "kind": "def",
  "name": "e0_e1_transition_check",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 194,
  "source_line_end": 198,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L194-L198",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L194-L198",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L194-L198)
- Source range: L194-L198
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D58` — E0/E1 Transition

## Immediate Comment / Docstring

```lean
/-- [II.D58] E0/E1 transition check:
    the external count at E0 equals the internal tau-value at E1.
    Both counting methods agree: the external enumeration (brute force)
    and the internal tau-counting (via restriction maps) give the same
    answer.

    We verify this concretely at k=1: external count = 4 maps,
    and all 4 restrict correctly to stage 0. -/
```

## Source Excerpt

```lean
def e0_e1_transition_check (db : TauIdx) : Bool :=
  let e0_ok := e0_external_hom_check db
  let e1_ok := e1_internal_hom_check db
  let k1_count_ok := count_rc_endomorphisms_k1 == 4
  e0_ok && e1_ok && k1_count_ok
```
