---
{
  "projection_kind": "taulib_declaration",
  "title": "twocat_vert_comp_scan",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/twocat-vert-comp-scan/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::twocat_vert_comp_scan",
  "declaration_slug": "twocat-vert-comp-scan",
  "kind": "def",
  "name": "twocat_vert_comp_scan",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 152,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L152-L162",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L152-L162",
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
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L152-L162)
- Source range: L152-L162
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: vertical composition of squaring after identity.
    sq ∘_v id at stage k: reduce((reduce(x, k))², k) should equal reduce(x², k).
    This tests that composition of 2-cells is coherent with modular arithmetic
    (relies on Nat.mul_mod, not just mod idempotence). -/
```

## Source Excerpt

```lean
def twocat_vert_comp_scan (x k db fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if k > db then true
  else
    -- sq(id(x, k), k) = reduce((reduce(x,k))², k)
    let id_val := reduce x k
    let sq_of_id := reduce (id_val * id_val) k
    -- Direct squaring: reduce(x², k)
    let direct_sq := reduce (x * x) k
    (sq_of_id == direct_sq) && twocat_vert_comp_scan x (k + 1) db (fuel - 1)
termination_by fuel
```
