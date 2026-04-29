---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_independence_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-circles/bc-independence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Circles`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Circles::bc_independence_check",
  "declaration_slug": "bc-independence-check",
  "kind": "def",
  "name": "bc_independence_check",
  "module_name": "TauLib.BookII.Transcendentals.Circles",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-circles/",
  "source_line_start": 114,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L114-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Circles",
        "url": "/verify/taulib/docs/book-ii-transcendentals-circles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L114-L121",
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

- Module: [TauLib.BookII.Transcendentals.Circles](/verify/taulib/docs/book-ii-transcendentals-circles/)
- Source path: [`TauLib/BookII/Transcendentals/Circles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L114-L121)
- Source range: L114-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Independence check: B and C orbits are genuinely independent.
    Witness: find points with same B but different C, and vice versa. -/
```

## Source Excerpt

```lean
def bc_independence_check : Bool :=
  -- 8=(2,3,1,1) vs 64=(2,3,2,1): same B=3 but C=1 vs C=2
  let p8 := from_tau_idx 8
  let p64 := from_tau_idx 64
  (p8.b == p64.b && p8.c != p64.c) &&
  -- 2=(2,1,1,1) vs 8=(2,3,1,1): different B, same C=1
  let p2 := from_tau_idx 2
  (p2.c == p8.c && p2.b != p8.b)
```
