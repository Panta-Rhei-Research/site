---
{
  "projection_kind": "taulib_declaration",
  "title": "unified_at_three_sixty",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/unified-at-three-sixty/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Coordinates.HyperfactIsomorphism`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactIsomorphism::unified_at_three_sixty",
  "declaration_slug": "unified-at-three-sixty",
  "kind": "theorem",
  "name": "unified_at_three_sixty",
  "module_name": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/",
  "source_line_start": 187,
  "source_line_end": 188,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L187-L188",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactIsomorphism",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L187-L188",
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

- Module: [TauLib.BookI.Coordinates.HyperfactIsomorphism](/verify/taulib/docs/book-i-coordinates-hyperfact-isomorphism/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactIsomorphism.lean#L187-L188)
- Source range: L187-L188
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Concrete at X = 360**. -/
```

## Source Excerpt

```lean
theorem unified_at_three_sixty :
    hyperfact_check 360 = true := by native_decide
```
