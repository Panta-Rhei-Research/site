---
{
  "projection_kind": "taulib_declaration",
  "title": "pinch_surjective_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-torus-degeneration/pinch-surjective-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.TorusDegeneration`.",
  "declaration_id": "TauLib.BookII.Topology.TorusDegeneration::pinch_surjective_check",
  "declaration_slug": "pinch-surjective-check",
  "kind": "def",
  "name": "pinch_surjective_check",
  "module_name": "TauLib.BookII.Topology.TorusDegeneration",
  "module_url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/",
  "source_line_start": 64,
  "source_line_end": 84,
  "registry_ids": [
    "II.T13"
  ],
  "related_registry_items": [
    {
      "id": "II.T13",
      "title": "Torus Degeneration Theorem",
      "url": "/registry/object/II.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L64-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.TorusDegeneration",
        "url": "/verify/taulib/docs/book-ii-topology-torus-degeneration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L64-L84",
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

- Module: [TauLib.BookII.Topology.TorusDegeneration](/verify/taulib/docs/book-ii-topology-torus-degeneration/)
- Source path: [`TauLib/BookII/Topology/TorusDegeneration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/TorusDegeneration.lean#L64-L84)
- Source range: L64-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T13` — Torus Degeneration Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T13] The pinch map is surjective: all three regions
    (plus lobe, minus lobe, wedge) are hit.
    Evidence: exhibit witnesses for each. -/
```

## Source Excerpt

```lean
def pinch_surjective_check : Bool :=
  -- Wedge: need B = C, both > 0. X = 12 has (3,1,1,4) → B=C=1
  let has_wedge := match pinch_point 12 with
    | .wedge => true
    | _ => false
  -- Plus lobe: need B > C. X = 64 has (2,3,2,1) → B=3 > C=2
  let has_plus := match pinch_point 64 with
    | .plus_lobe _ => true
    | _ => false
  -- Minus lobe: harder to find, need C > B
  -- Check small range for C > B examples
  let has_minus := go 2 200
  has_wedge && has_plus && has_minus
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if x > 200 then false
    else match pinch_point x with
      | .minus_lobe _ => true
      | _ => go (x + 1) (fuel - 1)
  termination_by fuel
```
