---
{
  "projection_kind": "taulib_declaration",
  "title": "four_suffice_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-dimension-four/four-suffice-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.DimensionFour`.",
  "declaration_id": "TauLib.BookII.Topology.DimensionFour::four_suffice_check",
  "declaration_slug": "four-suffice-check",
  "kind": "def",
  "name": "four_suffice_check",
  "module_name": "TauLib.BookII.Topology.DimensionFour",
  "module_url": "/verify/taulib/docs/book-ii-topology-dimension-four/",
  "source_line_start": 52,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L52-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.DimensionFour",
        "url": "/verify/taulib/docs/book-ii-topology-dimension-four/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L52-L62",
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

- Module: [TauLib.BookII.Topology.DimensionFour](/verify/taulib/docs/book-ii-topology-dimension-four/)
- Source path: [`TauLib/BookII/Topology/DimensionFour.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/DimensionFour.lean#L52-L62)
- Source range: L52-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T11, upper bound] Four coordinates suffice:
    ABCD chart is injective (no two distinct X share coordinates). -/
```

## Source Excerpt

```lean
def four_suffice_check (bound : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      (x == y || abcd_coords x != abcd_coords y) &&
      go x (y + 1) (fuel - 1)
  termination_by fuel
```
