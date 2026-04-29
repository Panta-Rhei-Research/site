---
{
  "projection_kind": "taulib_declaration",
  "title": "proto_rational_examples_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/proto-rational-examples-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::proto_rational_examples_check",
  "declaration_slug": "proto-rational-examples-check",
  "kind": "def",
  "name": "proto_rational_examples_check",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 101,
  "source_line_end": 110,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L101-L110",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L101-L110",
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
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L101-L110)
- Source range: L101-L110
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D65` — Proto-Rationality

## Immediate Comment / Docstring

```lean
/-- [II.D65] Proto-rational examples check: verify specific examples.
    - x = 2 is proto-rational at stage 2 (P_2 = 6 > 2)
    - x = 5 is proto-rational at stage 2 (P_2 = 6 > 5)
    - x = 7 is proto-rational at stage 3 (P_3 = 30 > 7)
    - x = 12 is proto-rational at stage 3 (P_3 = 30 > 12) -/
```

## Source Excerpt

```lean
def proto_rational_examples_check : Bool :=
  is_proto_rational 2 5 &&
  is_proto_rational 5 5 &&
  is_proto_rational 7 5 &&
  is_proto_rational 12 5 &&
  -- Stage checks
  proto_rational_stage 2 5 == 2 &&
  proto_rational_stage 5 5 == 2 &&
  proto_rational_stage 7 5 == 3 &&
  proto_rational_stage 12 5 == 3
```
