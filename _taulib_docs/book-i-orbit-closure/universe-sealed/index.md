---
{
  "projection_kind": "taulib_declaration",
  "title": "universe_sealed",
  "permalink": "/verify/taulib/docs/book-i-orbit-closure/universe-sealed/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Closure`.",
  "declaration_id": "TauLib.BookI.Orbit.Closure::universe_sealed",
  "declaration_slug": "universe-sealed",
  "kind": "theorem",
  "name": "universe_sealed",
  "module_name": "TauLib.BookI.Orbit.Closure",
  "module_url": "/verify/taulib/docs/book-i-orbit-closure/",
  "source_line_start": 73,
  "source_line_end": 76,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L73-L76",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Closure",
        "url": "/verify/taulib/docs/book-i-orbit-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L73-L76",
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

- Module: [TauLib.BookI.Orbit.Closure](/verify/taulib/docs/book-i-orbit-closure/)
- Source path: [`TauLib/BookI/Orbit/Closure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L73-L76)
- Source range: L73-L76
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The universe is sealed: the seed of any TauObj is one of the 5 generators.
    This is K6, restated at the orbit level. -/
```

## Source Excerpt

```lean
theorem universe_sealed (x : TauObj) :
    x.seed = alpha ∨ x.seed = pi ∨ x.seed = gamma ∨
    x.seed = eta ∨ x.seed = omega :=
  K6_object_closure x
```
