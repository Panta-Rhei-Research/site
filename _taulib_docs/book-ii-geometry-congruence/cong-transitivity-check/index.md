---
{
  "projection_kind": "taulib_declaration",
  "title": "cong_transitivity_check",
  "permalink": "/corpus/taulib/docs/book-ii-geometry-congruence/cong-transitivity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Congruence`.",
  "declaration_id": "TauLib.BookII.Geometry.Congruence::cong_transitivity_check",
  "declaration_slug": "cong-transitivity-check",
  "kind": "def",
  "name": "cong_transitivity_check",
  "module_name": "TauLib.BookII.Geometry.Congruence",
  "module_url": "/corpus/taulib/docs/book-ii-geometry-congruence/",
  "source_line_start": 73,
  "source_line_end": 79,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L73-L79",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.Congruence",
        "url": "/corpus/taulib/docs/book-ii-geometry-congruence/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L73-L79",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Geometry.Congruence](/corpus/taulib/docs/book-ii-geometry-congruence/)
- Source path: [`TauLib/BookII/Geometry/Congruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L73-L79)
- Source range: L73-L79
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T16, C3] Transitivity: AB ≅ CD ∧ CD ≅ EF ⟹ AB ≅ EF.
    Follows from transitivity of equality on depths. -/
```

## Source Excerpt

```lean
def cong_transitivity_check (bound db : TauIdx) : Bool :=
  -- Spot check: verify for specific witness triples
  let pairs := [(2,3), (3,5), (5,7), (7,11), (2,4), (4,8), (6,10)]
  pairs.all fun (a, b) =>
    pairs.all fun (c, d) =>
      pairs.all fun (e, f) =>
        !(congruent a b c d db && congruent c d e f db) || congruent a b e f db
```
