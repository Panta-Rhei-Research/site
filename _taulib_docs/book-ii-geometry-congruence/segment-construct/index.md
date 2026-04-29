---
{
  "projection_kind": "taulib_declaration",
  "title": "segment_construct",
  "permalink": "/verify/taulib/docs/book-ii-geometry-congruence/segment-construct/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Congruence`.",
  "declaration_id": "TauLib.BookII.Geometry.Congruence::segment_construct",
  "declaration_slug": "segment-construct",
  "kind": "def",
  "name": "segment_construct",
  "module_name": "TauLib.BookII.Geometry.Congruence",
  "module_url": "/verify/taulib/docs/book-ii-geometry-congruence/",
  "source_line_start": 97,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L97-L98",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.Congruence",
        "url": "/verify/taulib/docs/book-ii-geometry-congruence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L97-L98",
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

- Module: [TauLib.BookII.Geometry.Congruence](/verify/taulib/docs/book-ii-geometry-congruence/)
- Source path: [`TauLib/BookII/Geometry/Congruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L97-L98)
- Source range: L97-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T16, C4] Segment construction: given target depth m,
    find element E at depth m from D.
    Uses primorial structure: E = D + P_m gives δ(D,E) = m. -/
```

## Source Excerpt

```lean
def segment_construct (d_val target_depth : TauIdx) : TauIdx :=
  d_val + primorial target_depth
```
