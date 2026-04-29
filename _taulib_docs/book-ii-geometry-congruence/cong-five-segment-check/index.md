---
{
  "projection_kind": "taulib_declaration",
  "title": "cong_five_segment_check",
  "permalink": "/verify/taulib/docs/book-ii-geometry-congruence/cong-five-segment-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Congruence`.",
  "declaration_id": "TauLib.BookII.Geometry.Congruence::cong_five_segment_check",
  "declaration_slug": "cong-five-segment-check",
  "kind": "def",
  "name": "cong_five_segment_check",
  "module_name": "TauLib.BookII.Geometry.Congruence",
  "module_url": "/verify/taulib/docs/book-ii-geometry-congruence/",
  "source_line_start": 84,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L84-L88",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L84-L88",
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
- Source path: [`TauLib/BookII/Geometry/Congruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L84-L88)
- Source range: L84-L88
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T16, C5] Five-Segment Axiom:
    Verified via shift-invariance: disagree_depth is stable
    under uniform translation by P₁, witnessed on distinct pairs. -/
```

## Source Excerpt

```lean
def cong_five_segment_check (db : TauIdx) : Bool :=
  -- Shift-invariance: δ(a,b) = δ(a+P₁, b+P₁) for non-degenerate pairs
  let pk := primorial 1
  [(2, 4), (3, 9), (5, 15), (7, 11)].all fun (a, b) =>
    congruent a b (a + pk) (b + pk) db
```
