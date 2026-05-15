---
{
  "projection_kind": "taulib_declaration",
  "title": "congruent",
  "permalink": "/corpus/taulib/docs/book-ii-geometry-congruence/congruent/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.Congruence`.",
  "declaration_id": "TauLib.BookII.Geometry.Congruence::congruent",
  "declaration_slug": "congruent",
  "kind": "def",
  "name": "congruent",
  "module_name": "TauLib.BookII.Geometry.Congruence",
  "module_url": "/corpus/taulib/docs/book-ii-geometry-congruence/",
  "source_line_start": 37,
  "source_line_end": 38,
  "registry_ids": [
    "II.D20"
  ],
  "related_registry_items": [
    {
      "id": "II.D20",
      "title": "Congruence Relation",
      "url": "/registry/object/II.D20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L37-L38",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L37-L38",
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
- Source path: [`TauLib/BookII/Geometry/Congruence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/Congruence.lean#L37-L38)
- Source range: L37-L38
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.D20` — Congruence Relation

## Immediate Comment / Docstring

```lean
/-- [II.D20] Ultrametric congruence: AB ≅ CD iff δ(A,B) = δ(C,D).
    Segments have equal "length" iff their endpoints have equal
    agreement depth in the primorial tower. -/
```

## Source Excerpt

```lean
def congruent (a b c d db : TauIdx) : Bool :=
  disagree_depth a b db == disagree_depth c d db
```
