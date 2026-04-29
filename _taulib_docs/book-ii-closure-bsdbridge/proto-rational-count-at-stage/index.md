---
{
  "projection_kind": "taulib_declaration",
  "title": "proto_rational_count_at_stage",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/proto-rational-count-at-stage/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::proto_rational_count_at_stage",
  "declaration_slug": "proto-rational-count-at-stage",
  "kind": "def",
  "name": "proto_rational_count_at_stage",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 115,
  "source_line_end": 132,
  "registry_ids": [
    "II.D65"
  ],
  "related_registry_items": [
    {
      "id": "II.D65",
      "title": "Proto-Rationality",
      "url": "/registry/object/II.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L115-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.BSDbridge",
        "url": "/verify/taulib/docs/book-ii-closure-bsdbridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L115-L132",
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

- Module: [TauLib.BookII.Closure.BSDbridge](/verify/taulib/docs/book-ii-closure-bsdbridge/)
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L115-L132)
- Source range: L115-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D65` — Proto-Rationality

## Immediate Comment / Docstring

```lean
/-- [II.D65] Proto-rational count at stage k: the number of proto-rational
    points determined at exactly stage k (i.e., reduce(x, k) = x but
    reduce(x, k-1) != x, for x > 1). -/
```

## Source Excerpt

```lean
def proto_rational_count_at_stage (k : TauIdx) : TauIdx :=
  if k = 0 then 0
  else
    let pk := primorial k
    let pk_prev := if k >= 1 then primorial (k - 1) else 1
    go pk pk_prev 2 0 (pk + 1)
where
  go (pk pk_prev x count fuel : Nat) : Nat :=
    if fuel = 0 then count
    else if x >= pk then count
    else
      -- x is determined at stage k: reduce(x, k) = x (always true if x < pk)
      -- x is NOT determined at stage k-1: reduce(x, k-1) != x
      let at_prev := reduce x (k - 1)
      let new_stage := x ≥ 2 && at_prev != x
      let new_count := if new_stage then count + 1 else count
      go pk pk_prev (x + 1) new_count (fuel - 1)
  termination_by fuel
```
