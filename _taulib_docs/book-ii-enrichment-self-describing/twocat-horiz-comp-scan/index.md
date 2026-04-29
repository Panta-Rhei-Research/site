---
{
  "projection_kind": "taulib_declaration",
  "title": "twocat_horiz_comp_scan",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/twocat-horiz-comp-scan/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::twocat_horiz_comp_scan",
  "declaration_slug": "twocat-horiz-comp-scan",
  "kind": "def",
  "name": "twocat_horiz_comp_scan",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 167,
  "source_line_end": 175,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L167-L175",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfDescribing",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L167-L175",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L167-L175)
- Source range: L167-L175
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: horizontal composition of squaring after doubling.
    sq(dbl(x, k), k) = reduce((reduce(2x, k))², k) should equal
    reduce((2x)², k) = reduce(4x², k). Tests mul_mod coherence. -/
```

## Source Excerpt

```lean
def twocat_horiz_comp_scan (x k db fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if k > db then true
  else
    let dbl_val := reduce (2 * x) k
    let sq_of_dbl := reduce (dbl_val * dbl_val) k
    let direct := reduce (4 * x * x) k
    (sq_of_dbl == direct) && twocat_horiz_comp_scan x (k + 1) db (fuel - 1)
termination_by fuel
```
