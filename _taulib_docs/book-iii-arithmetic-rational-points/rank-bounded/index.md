---
{
  "projection_kind": "taulib_declaration",
  "title": "rank_bounded",
  "permalink": "/corpus/taulib/docs/book-iii-arithmetic-rational-points/rank-bounded/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::rank_bounded",
  "declaration_slug": "rank-bounded",
  "kind": "theorem",
  "name": "rank_bounded",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/corpus/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 180,
  "source_line_end": 181,
  "registry_ids": [
    "III.D60"
  ],
  "related_registry_items": [
    {
      "id": "III.D60",
      "title": "Rank as Tower Depth",
      "url": "/registry/object/III.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L180-L181",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/corpus/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L180-L181",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/corpus/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L180-L181)
- Source range: L180-L181
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D60` — Rank as Tower Depth

## Immediate Comment / Docstring

```lean
/-- [III.D60] Structural: rank is bounded by db. -/
```

## Source Excerpt

```lean
theorem rank_bounded :
    rank_as_depth 42 5 ≤ 5 := by native_decide
```
