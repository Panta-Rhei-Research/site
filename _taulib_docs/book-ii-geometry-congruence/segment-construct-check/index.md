---
{
  "projection_kind": "taulib_declaration",
  "title": "segment_construct_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-congruence/segment-construct-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Congruence`.",
  "declaration_id": "TauLib.BookII.Geometry.Congruence::segment_construct_check",
  "declaration_slug": "segment-construct-check",
  "kind": "def",
  "name": "segment_construct_check",
  "module_name": "TauLib.BookII.Geometry.Congruence",
  "module_url": "/verify/taulib/docs/book-ii-geometry-congruence/",
  "source_line_start": 101,
  "source_line_end": 113,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L101-L113",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L101-L113",
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
- Source path: [`TauLib/BookII/Geometry/Congruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L101-L113)
- Source range: L101-L113
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verify segment construction achieves target depth. -/
```

## Source Excerpt

```lean
def segment_construct_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (d m fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if d > bound then true
    else if m > db then go (d + 1) 1 (fuel - 1)
    else
      let e := segment_construct d m
      (e ≤ bound + primorial db + 1 →
        disagree_depth d e db == m) &&
      go d (m + 1) (fuel - 1)
  termination_by fuel
```
