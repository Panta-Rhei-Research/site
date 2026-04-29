---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L250",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/example-l250/",
  "summary_short": "`example` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::#eval:250",
  "declaration_slug": "example-l250",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 250,
  "source_line_end": 250,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L250-L250",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L250-L250",
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
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L250-L250)
- Source range: L250-L250
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Non-omega objects are not infinity objects (verified by construction)
```

## Source Excerpt

```lean
example : ¬ InfinityObject ⟨alpha, 5⟩ := no_orbit_infinity alpha (by decide) 5
```
