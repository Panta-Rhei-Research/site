---
{
  "projection_kind": "taulib_declaration",
  "title": "find_parallel_partner",
  "permalink": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/find-parallel-partner/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.PaschParallel`.",
  "declaration_id": "TauLib.BookII.Geometry.PaschParallel::find_parallel_partner",
  "declaration_slug": "find-parallel-partner",
  "kind": "def",
  "name": "find_parallel_partner",
  "module_name": "TauLib.BookII.Geometry.PaschParallel",
  "module_url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/",
  "source_line_start": 89,
  "source_line_end": 97,
  "registry_ids": [
    "II.T18"
  ],
  "related_registry_items": [
    {
      "id": "II.T18",
      "title": "Parallel Postulate",
      "url": "/registry/object/II.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L89-L97",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Geometry.PaschParallel",
        "url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L89-L97",
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

- Module: [TauLib.BookII.Geometry.PaschParallel](/verify/taulib/docs/book-ii-geometry-pasch-parallel/)
- Source path: [`TauLib/BookII/Geometry/PaschParallel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L89-L97)
- Source range: L89-L97
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T18` — Parallel Postulate

## Immediate Comment / Docstring

```lean
/-- [II.T18] Find a parallel partner: w ≠ z with δ(z,w) = k in [2, bound].
    Returns true iff such a partner exists. -/
```

## Source Excerpt

```lean
def find_parallel_partner (z k db bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (w fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if w > bound then false
    else if w != z && disagree_depth z w db == k then true
    else go (w + 1) (fuel - 1)
  termination_by fuel
```
