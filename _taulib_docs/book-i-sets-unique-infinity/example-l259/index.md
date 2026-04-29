---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L259",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/example-l259/",
  "summary_short": "`example` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::#eval:259",
  "declaration_slug": "example-l259",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 259,
  "source_line_end": 259,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L259-L259",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.UniqueInfinity",
        "url": "/verify/taulib/docs/book-i-sets-unique-infinity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L259-L259",
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

- Module: [TauLib.BookI.Sets.UniqueInfinity](/verify/taulib/docs/book-i-sets-unique-infinity/)
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L259-L259)
- Source range: L259-L259
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Constant sequence converges
```

## Source Excerpt

```lean
example : GermConvergence (fun _ => 42) 10 := const_seq_converges 42 10
```
