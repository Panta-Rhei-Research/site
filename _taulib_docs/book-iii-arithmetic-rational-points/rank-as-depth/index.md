---
{
  "projection_kind": "taulib_declaration",
  "title": "rank_as_depth",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-rational-points/rank-as-depth/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::rank_as_depth",
  "declaration_slug": "rank-as-depth",
  "kind": "def",
  "name": "rank_as_depth",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 80,
  "source_line_end": 89,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L80-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L80-L89",
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/verify/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L80-L89)
- Source range: L80-L89
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D60` — Rank as Tower Depth

## Immediate Comment / Docstring

```lean
/-- [III.D60] Rank of a τ-rational point: the minimal depth at which
    the group operation stabilizes. -/
```

## Source Excerpt

```lean
def rank_as_depth (x db : TauIdx) : TauIdx :=
  go x 1 (db + 1)
where
  go (x k fuel : Nat) : TauIdx :=
    if fuel = 0 then k
    else if k > db then k
    else
      if is_rational_at x k then k
      else go x (k + 1) (fuel - 1)
  termination_by fuel
```
