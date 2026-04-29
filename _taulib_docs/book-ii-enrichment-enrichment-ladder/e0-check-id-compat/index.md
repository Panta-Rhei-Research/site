---
{
  "projection_kind": "taulib_declaration",
  "title": "e0_check_id_compat",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/e0-check-id-compat/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::e0_check_id_compat",
  "declaration_slug": "e0-check-id-compat",
  "kind": "def",
  "name": "e0_check_id_compat",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 68,
  "source_line_end": 77,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L68-L77",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L68-L77",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L68-L77)
- Source range: L68-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: check reduce-compatibility of the identity map at stage k.
    The identity map id_k(x) = reduce(x, k) is reduce-compatible iff
    reduce(id_k(x), k-1) = id_k(reduce(x, k-1)) for all x.
    This reduces to: reduce(reduce(x, k), k-1) = reduce(reduce(x, k-1), k-1)
    = reduce(x, k-1). -/
```

## Source Excerpt

```lean
def e0_check_id_compat (k x fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if k = 0 then true
  else if x >= primorial k then true
  else
    let id_val := reduce x k
    let reduced_id := reduce id_val (k - 1)
    let direct := reduce x (k - 1)
    (reduced_id == direct) && e0_check_id_compat k (x + 1) (fuel - 1)
termination_by fuel
```
