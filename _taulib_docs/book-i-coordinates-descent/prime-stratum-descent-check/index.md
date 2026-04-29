---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_stratum_descent_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-descent/prime-stratum-descent-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Descent`.",
  "declaration_id": "TauLib.BookI.Coordinates.Descent::prime_stratum_descent_check",
  "declaration_slug": "prime-stratum-descent-check",
  "kind": "def",
  "name": "prime_stratum_descent_check",
  "module_name": "TauLib.BookI.Coordinates.Descent",
  "module_url": "/verify/taulib/docs/book-i-coordinates-descent/",
  "source_line_start": 57,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L57-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Descent",
        "url": "/verify/taulib/docs/book-i-coordinates-descent/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L57-L62",
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

- Module: [TauLib.BookI.Coordinates.Descent](/verify/taulib/docs/book-i-coordinates-descent/)
- Source path: [`TauLib/BookI/Coordinates/Descent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L57-L62)
- Source range: L57-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check that the largest prime of D is strictly less than A. -/
```

## Source Excerpt

```lean
def prime_stratum_descent_check (x : TauIdx) : Bool :=
  if x ≤ 1 then true
  else
    let (a, _, _, d) := greedy_peel x
    if d ≤ 1 then true
    else largest_prime_divisor d < a
```
