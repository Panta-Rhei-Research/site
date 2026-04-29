---
{
  "projection_kind": "taulib_declaration",
  "title": "proto_rational_stage",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/proto-rational-stage/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::proto_rational_stage",
  "declaration_slug": "proto-rational-stage",
  "kind": "def",
  "name": "proto_rational_stage",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 66,
  "source_line_end": 75,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L66-L75",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L66-L75",
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
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L66-L75)
- Source range: L66-L75
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D65` — Proto-Rationality

## Immediate Comment / Docstring

```lean
/-- [II.D65] Find the smallest stage k at which x is determined.
    Returns 0 if x is not proto-rational within max_k stages. -/
```

## Source Excerpt

```lean
def proto_rational_stage (x max_k : TauIdx) : TauIdx :=
  if x ≤ 1 then 0
  else find_min_stage x 1 (max_k + 1)
where
  find_min_stage (x k fuel : Nat) : Nat :=
    if fuel = 0 then 0
    else if k > max_k then 0
    else if reduce x k == x then k
    else find_min_stage x (k + 1) (fuel - 1)
  termination_by fuel
```
