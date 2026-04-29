---
{
  "projection_kind": "taulib_declaration",
  "title": "four_ray_complete",
  "permalink": "/verify/taulib/docs/book-ii-interior-abcdrigidity/four-ray-complete/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.ABCDRigidity`.",
  "declaration_id": "TauLib.BookII.Interior.ABCDRigidity::four_ray_complete",
  "declaration_slug": "four-ray-complete",
  "kind": "def",
  "name": "four_ray_complete",
  "module_name": "TauLib.BookII.Interior.ABCDRigidity",
  "module_url": "/verify/taulib/docs/book-ii-interior-abcdrigidity/",
  "source_line_start": 45,
  "source_line_end": 46,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L45-L46",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.ABCDRigidity",
        "url": "/verify/taulib/docs/book-ii-interior-abcdrigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L45-L46",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.Interior.ABCDRigidity](/verify/taulib/docs/book-ii-interior-abcdrigidity/)
- Source path: [`TauLib/BookII/Interior/ABCDRigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L45-L46)
- Source range: L45-L46
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.P03, clause 1] Completeness:
    The ABCD chart assigns a unique quadruple to every X ≥ 2.
    Verified by injectivity (no collisions) for X = 2..bound. -/
```

## Source Excerpt

```lean
def four_ray_complete (bound : TauIdx) : Bool :=
  faithful_check bound
```
