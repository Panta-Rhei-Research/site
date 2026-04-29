---
{
  "projection_kind": "taulib_declaration",
  "title": "is_proto_rational",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/is-proto-rational/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::is_proto_rational",
  "declaration_slug": "is-proto-rational",
  "kind": "def",
  "name": "is_proto_rational",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 53,
  "source_line_end": 62,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L53-L62",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L53-L62",
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
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L53-L62)
- Source range: L53-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D65` — Proto-Rationality

## Immediate Comment / Docstring

```lean
/-- [II.D65] Check if a point x is proto-rational: x > 1 and there exists
    a stage k (searched up to max_k) such that reduce(x, k) = x. -/
```

## Source Excerpt

```lean
def is_proto_rational (x max_k : TauIdx) : Bool :=
  if x ≤ 1 then false
  else find_stage x 1 (max_k + 1)
where
  find_stage (x k fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if k > max_k then false
    else if reduce x k == x then true
    else find_stage x (k + 1) (fuel - 1)
  termination_by fuel
```
