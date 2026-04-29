---
{
  "projection_kind": "taulib_declaration",
  "title": "verify_k1_count",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/verify-k1-count/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.EnrichmentLadder`.",
  "declaration_id": "TauLib.BookII.Enrichment.EnrichmentLadder::verify_k1_count",
  "declaration_slug": "verify-k1-count",
  "kind": "def",
  "name": "verify_k1_count",
  "module_name": "TauLib.BookII.Enrichment.EnrichmentLadder",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-enrichment-ladder/",
  "source_line_start": 119,
  "source_line_end": 137,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L119-L137",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L119-L137",
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
- Source path: [`TauLib/BookII/Enrichment/EnrichmentLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/EnrichmentLadder.lean#L119-L137)
- Source range: L119-L137
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verify the k=1 count: all 4 maps {0,1} -> {0,1} are reduce-compatible.
    We enumerate all 4 maps and check each one. -/
```

## Source Excerpt

```lean
def verify_k1_count : Bool :=
  go 0 0 0 5
where
  go (f0 f1 count fuel : Nat) : Bool :=
    if fuel = 0 then count == 4
    else
      -- Check reduce-compat for map f(0) = f0, f(1) = f1:
      -- ∀ x ∈ {0,1}: reduce(f(x), 0) = reduce(f(reduce(x, 0)), 0)
      -- At k=1 this is always true (both sides are 0), but we compute it.
      let apply_f := fun (x : Nat) => if x == 0 then f0 else f1
      let compat :=
        (reduce (apply_f 0) 0 == reduce (apply_f (reduce 0 0)) 0) &&
        (reduce (apply_f 1) 0 == reduce (apply_f (reduce 1 0)) 0)
      let new_count := if compat then count + 1 else count
      -- Advance to next map: iterate (f0, f1) over {0,1} x {0,1}
      if f1 = 0 then go f0 1 new_count (fuel - 1)
      else if f0 = 0 then go 1 0 new_count (fuel - 1)
      else new_count == 4  -- last map (1,1): 4 total
  termination_by fuel
```
