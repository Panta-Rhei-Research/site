---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L193",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/example-l193/",
  "summary_short": "`example` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::#eval:193",
  "declaration_slug": "example-l193",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 193,
  "source_line_end": 202,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L193-L202",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-rat-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L193-L202",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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

- Module: [TauLib.BookI.Boundary.TauRatInv](/verify/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L193-L202)
- Source range: L193-L202
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Negative: 1/(-2/3) = -3/2
```

## Source Excerpt

```lean
example :
    let q : TauRat := ⟨⟨0, 2⟩, 3, by norm_num⟩
    have h : q.is_nonzero := by unfold TauRat.is_nonzero TauInt.toInt; norm_num
    (q.inv h).toRat = -3/2 := by
  intro q h
  rw [toRat_inv]
  simp [TauRat.toRat, TauInt.toInt, q]
  norm_num

end Tau.Boundary
```
