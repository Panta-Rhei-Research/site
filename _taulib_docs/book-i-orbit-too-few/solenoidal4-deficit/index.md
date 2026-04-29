---
{
  "projection_kind": "taulib_declaration",
  "title": "solenoidal4_deficit",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-few/solenoidal4-deficit/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.TooFew`.",
  "declaration_id": "TauLib.BookI.Orbit.TooFew::solenoidal4_deficit",
  "declaration_slug": "solenoidal4-deficit",
  "kind": "theorem",
  "name": "solenoidal4_deficit",
  "module_name": "TauLib.BookI.Orbit.TooFew",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-few/",
  "source_line_start": 88,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L88-L88",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooFew",
        "url": "/verify/taulib/docs/book-i-orbit-too-few/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L88-L88",
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

- Module: [TauLib.BookI.Orbit.TooFew](/verify/taulib/docs/book-i-orbit-too-few/)
- Source path: [`TauLib/BookI/Orbit/TooFew.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L88-L88)
- Source range: L88-L88
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The deficit: 2 solenoidal generators for 3 rewiring levels needed. -/
```

## Source Excerpt

```lean
theorem solenoidal4_deficit : solenoidal4.length < 3 := by decide
```
