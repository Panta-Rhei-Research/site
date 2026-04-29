---
{
  "projection_kind": "taulib_declaration",
  "title": "proto_rational_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/proto-rational-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::proto_rational_check",
  "declaration_slug": "proto-rational-check",
  "kind": "def",
  "name": "proto_rational_check",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 86,
  "source_line_end": 94,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L86-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L86-L94",
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
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L86-L94)
- Source range: L86-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D65` — Proto-Rationality

## Immediate Comment / Docstring

```lean
/-- [II.D65] Proto-rationality verification for a range [2, bound].
    Check that every x in the range is proto-rational (which is true
    for all finite x, since reduce(x, k) = x whenever P_k > x). -/
```

## Source Excerpt

```lean
def proto_rational_check (bound max_k : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      is_proto_rational x max_k && go (x + 1) (fuel - 1)
  termination_by fuel
```
