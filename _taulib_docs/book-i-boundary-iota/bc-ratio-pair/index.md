---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_ratio_pair",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota/bc-ratio-pair/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Iota`.",
  "declaration_id": "TauLib.BookI.Boundary.Iota::bc_ratio_pair",
  "declaration_slug": "bc-ratio-pair",
  "kind": "def",
  "name": "bc_ratio_pair",
  "module_name": "TauLib.BookI.Boundary.Iota",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota/",
  "source_line_start": 65,
  "source_line_end": 66,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L65-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Iota",
        "url": "/verify/taulib/docs/book-i-boundary-iota/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L65-L66",
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

- Module: [TauLib.BookI.Boundary.Iota](/verify/taulib/docs/book-i-boundary-iota/)
- Source path: [`TauLib/BookI/Boundary/Iota.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L65-L66)
- Source range: L65-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- B/C count ratio as a pair (numerator, denominator).
    Returns (count_b, count_c) where the ratio is count_b / count_c. -/
```

## Source Excerpt

```lean
def bc_ratio_pair (n N : TauIdx) : Nat × Nat :=
  (count_b_dominant n N, count_c_dominant n N)
```
