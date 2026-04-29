---
{
  "projection_kind": "taulib_declaration",
  "title": "dag_indices_go",
  "permalink": "/verify/taulib/docs/book-i-coordinates-abcd/dag-indices-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ABCD`.",
  "declaration_id": "TauLib.BookI.Coordinates.ABCD::dag_indices_go",
  "declaration_slug": "dag-indices-go",
  "kind": "def",
  "name": "dag_indices_go",
  "module_name": "TauLib.BookI.Coordinates.ABCD",
  "module_url": "/verify/taulib/docs/book-i-coordinates-abcd/",
  "source_line_start": 65,
  "source_line_end": 78,
  "registry_ids": [
    "I.D24"
  ],
  "related_registry_items": [
    {
      "id": "I.D24",
      "title": "Address DAG",
      "url": "/registry/object/I.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L65-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ABCD",
        "url": "/verify/taulib/docs/book-i-coordinates-abcd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L65-L78",
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

- Module: [TauLib.BookI.Coordinates.ABCD](/verify/taulib/docs/book-i-coordinates-abcd/)
- Source path: [`TauLib/BookI/Coordinates/ABCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ABCD.lean#L65-L78)
- Source range: L65-L78
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D24` — Address DAG

## Immediate Comment / Docstring

```lean
/-- [I.D24] Collect all distinct indices reachable by recursing into ABCD
    coordinates. Uses a visited set for deduplication (DAG, not tree). -/
```

## Source Excerpt

```lean
def dag_indices_go (worklist visited : List TauIdx) (fuel : Nat) : List TauIdx :=
  if fuel = 0 then visited
  else match worklist with
  | [] => visited
  | y :: rest =>
    if visited.contains y then dag_indices_go rest visited (fuel - 1)
    else if y ≤ 1 then dag_indices_go rest (y :: visited) (fuel - 1)
    else
      let a := coord_A y
      let b := coord_B y
      let c := coord_C y
      let d := coord_D y
      dag_indices_go (a :: b :: c :: d :: rest) (y :: visited) (fuel - 1)
termination_by fuel
```
