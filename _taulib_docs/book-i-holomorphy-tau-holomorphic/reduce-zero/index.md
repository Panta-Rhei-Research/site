---
{
  "projection_kind": "taulib_declaration",
  "title": "reduce_zero",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/reduce-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::reduce_zero",
  "declaration_slug": "reduce-zero",
  "kind": "theorem",
  "name": "reduce_zero",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 165,
  "source_line_end": 166,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L165-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L165-L166",
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

- Module: [TauLib.BookI.Holomorphy.TauHolomorphic](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L165-L166)
- Source range: L165-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: the reduce function applied to zero gives zero. -/
```

## Source Excerpt

```lean
private theorem reduce_zero (k : TauIdx) : reduce 0 k = 0 := by
  simp [reduce, Nat.zero_mod]
```
