---
{
  "projection_kind": "taulib_declaration",
  "title": "id_reduce_compat",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-describing/id-reduce-compat/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Enrichment.SelfDescribing`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfDescribing::id_reduce_compat",
  "declaration_slug": "id-reduce-compat",
  "kind": "theorem",
  "name": "id_reduce_compat",
  "module_name": "TauLib.BookII.Enrichment.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-describing/",
  "source_line_start": 240,
  "source_line_end": 242,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L240-L242",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L240-L242",
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

- Module: [TauLib.BookII.Enrichment.SelfDescribing](/verify/taulib/docs/book-ii-enrichment-self-describing/)
- Source path: [`TauLib/BookII/Enrichment/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfDescribing.lean#L240-L242)
- Source range: L240-L242
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The identity map is reduce-compatible: the Yoneda direction.
    reduce(reduce(x, k), j) = reduce(x, j) for j <= k.
    This is reduction_compat from ModArith. -/
```

## Source Excerpt

```lean
theorem id_reduce_compat (x : TauIdx) {j k : TauIdx} (h : j ≤ k) :
    reduce (reduce x k) j = reduce x j :=
  reduction_compat x h
```
