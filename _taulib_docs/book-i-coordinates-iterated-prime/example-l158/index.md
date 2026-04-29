---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L158",
  "permalink": "/verify/taulib/docs/book-i-coordinates-iterated-prime/example-l158/",
  "summary_short": "`example` declaration in `TauLib.BookI.Coordinates.IteratedPrime`.",
  "declaration_id": "TauLib.BookI.Coordinates.IteratedPrime::#eval:158",
  "declaration_slug": "example-l158",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Coordinates.IteratedPrime",
  "module_url": "/verify/taulib/docs/book-i-coordinates-iterated-prime/",
  "source_line_start": 158,
  "source_line_end": 158,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L158-L158",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.IteratedPrime",
        "url": "/verify/taulib/docs/book-i-coordinates-iterated-prime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L158-L158",
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

- Module: [TauLib.BookI.Coordinates.IteratedPrime](/verify/taulib/docs/book-i-coordinates-iterated-prime/)
- Source path: [`TauLib/BookI/Coordinates/IteratedPrime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/IteratedPrime.lean#L158-L158)
- Source range: L158-L158
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Level 3 (η-orbit): val(η_n) = p_{p_{p_n}}
-- η_1 = p_{p_{p_1}} = p_{p_2} = p_3 = 5
-- η_2 = p_{p_{p_2}} = p_{p_3} = p_5 = 11
-- η_3 = p_{p_{p_3}} = p_{p_5} = p_11 = 31
-- η_4 = p_{p_{p_4}} = p_{p_7} = p_17 = 59
-- η_5 = p_{p_{p_5}} = p_{p_11} = p_31 = 127
```

## Source Excerpt

```lean
example : towerVal 3 1 = 5 := by native_decide
```
