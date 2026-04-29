---
{
  "projection_kind": "taulib_declaration",
  "title": "parallel_check_z",
  "permalink": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/parallel-check-z/",
  "summary_short": "`def` declaration in `TauLib.BookII.Geometry.PaschParallel`.",
  "declaration_id": "TauLib.BookII.Geometry.PaschParallel::parallel_check_z",
  "declaration_slug": "parallel-check-z",
  "kind": "def",
  "name": "parallel_check_z",
  "module_name": "TauLib.BookII.Geometry.PaschParallel",
  "module_url": "/verify/taulib/docs/book-ii-geometry-pasch-parallel/",
  "source_line_start": 100,
  "source_line_end": 111,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L100-L111",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L100-L111",
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
- Source path: [`TauLib/BookII/Geometry/PaschParallel.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Geometry/PaschParallel.lean#L100-L111)
- Source range: L100-L111
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Inner loop for parallel check: iterate over z for fixed x, y. -/
```

## Source Excerpt

```lean
def parallel_check_z (x y bound db : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (z fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if z > bound then true
    else if on_depth_line x y z db then
      go (z + 1) (fuel - 1)
    else
      let k := disagree_depth x y db
      find_parallel_partner z k db bound && go (z + 1) (fuel - 1)
  termination_by fuel
```
