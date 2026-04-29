---
{
  "projection_kind": "taulib_declaration",
  "title": "proto_rational_count_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-bsdbridge/proto-rational-count-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.BSDbridge`.",
  "declaration_id": "TauLib.BookII.Closure.BSDbridge::proto_rational_count_check",
  "declaration_slug": "proto-rational-count-check",
  "kind": "def",
  "name": "proto_rational_count_check",
  "module_name": "TauLib.BookII.Closure.BSDbridge",
  "module_url": "/verify/taulib/docs/book-ii-closure-bsdbridge/",
  "source_line_start": 141,
  "source_line_end": 143,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L141-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L141-L143",
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
- Source path: [`TauLib/BookII/Closure/BSDbridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/BSDbridge.lean#L141-L143)
- Source range: L141-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Proto-rational count check: at stage 1 (P_1 = 2), no points are
    newly determined (x=0 and x=1 are excluded by x > 1 condition,
    but reduce(0, 0) = 0 and reduce(1, 0) = 0, so stage 0 already
    captures them). Actually at stage 1, x = 0 has reduce(0, 0) = 0 = x
    but x <= 1, so not counted. x = 1 is also <= 1.
    At stage 2 (P_2 = 6): points 2, 3, 4, 5 are new (reduce(x, 1) != x
    for x >= 2 since P_1 = 2). -/
```

## Source Excerpt

```lean
def proto_rational_count_check : Bool :=
  proto_rational_count_at_stage 2 == 4 &&    -- x = 2, 3, 4, 5
  proto_rational_count_at_stage 3 >= 10       -- many new at stage 3
```
