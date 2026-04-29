---
{
  "projection_kind": "taulib_declaration",
  "title": "rank_stabilization_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-rational-points/rank-stabilization-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::rank_stabilization_check",
  "declaration_slug": "rank-stabilization-check",
  "kind": "def",
  "name": "rank_stabilization_check",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 131,
  "source_line_end": 143,
  "registry_ids": [
    "III.P25"
  ],
  "related_registry_items": [
    {
      "id": "III.P25",
      "title": "Mordell-Weil Analogue",
      "url": "/registry/object/III.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L131-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L131-L143",
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
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L131-L143)
- Source range: L131-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P25` — Mordell-Weil Analogue

## Immediate Comment / Docstring

```lean
/-- [III.P25] Rank stabilization: rank is non-decreasing across depths. -/
```

## Source Excerpt

```lean
def rank_stabilization_check (bound db : TauIdx) : Bool :=
  go 0 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      -- Rank at db is the final rank
      let r := rank_as_depth x db
      -- All rational at every level ≥ rank
      let ok := r <= db
      ok && go (x + 1) (fuel - 1)
  termination_by fuel
```
