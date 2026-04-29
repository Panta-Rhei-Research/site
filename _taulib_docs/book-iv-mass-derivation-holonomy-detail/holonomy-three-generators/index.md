---
{
  "projection_kind": "taulib_declaration",
  "title": "holonomy_three_generators",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/holonomy-three-generators/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.HolonomyDetail`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.HolonomyDetail::holonomy_three_generators",
  "declaration_slug": "holonomy-three-generators",
  "kind": "theorem",
  "name": "holonomy_three_generators",
  "module_name": "TauLib.BookIV.MassDerivation.HolonomyDetail",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/",
  "source_line_start": 110,
  "source_line_end": 111,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L110-L111",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.HolonomyDetail",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L110-L111",
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

- Module: [TauLib.BookIV.MassDerivation.HolonomyDetail](/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/)
- Source path: [`TauLib/BookIV/MassDerivation/HolonomyDetail.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L110-L111)
- Source range: L110-L111
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Three generators listed. -/
```

## Source Excerpt

```lean
theorem holonomy_three_generators :
    triple_holonomy_H3.generators.length = 3 := rfl
```
