---
{
  "projection_kind": "taulib_declaration",
  "title": "b_stabilization_depth",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/b-stabilization-depth/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::b_stabilization_depth",
  "declaration_slug": "b-stabilization-depth",
  "kind": "def",
  "name": "b_stabilization_depth",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 53,
  "source_line_end": 72,
  "registry_ids": [
    "II.D49"
  ],
  "related_registry_items": [
    {
      "id": "II.D49",
      "title": "Tau-Regularity",
      "url": "/registry/object/II.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L53-L72",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PositiveRegularity",
        "url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L53-L72",
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

- Module: [TauLib.BookII.Regularity.PositiveRegularity](/verify/taulib/docs/book-ii-regularity-positive-regularity/)
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L53-L72)
- Source range: L53-L72
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D49` — Tau-Regularity

## Immediate Comment / Docstring

```lean
/-- [II.D49] B-channel stabilization depth: the smallest stage k
    (starting from 1) at which the B-coordinate of from_tau_idx(reduce(x, k))
    equals the B-coordinate at all subsequent stages up to db.

    Returns the stabilization stage, or db+1 if no stabilization. -/
```

## Source Excerpt

```lean
def b_stabilization_depth (x db : TauIdx) : Nat :=
  go x 1 (db + 1)
where
  go (x k fuel : Nat) : Nat :=
    if fuel = 0 then db + 1
    else if k > db then db + 1
    else
      let bk := (from_tau_idx (reduce x k)).b
      -- Check if B-coordinate stays the same for all stages k+1 .. db
      let stable := check_stable x bk (k + 1) (db - k)
      if stable then k
      else go x (k + 1) (fuel - 1)
  termination_by fuel
  check_stable (x : Nat) (target : Nat) (j fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if j > db then true
    else
      let bj := (from_tau_idx (reduce x j)).b
      (bj == target) && check_stable x target (j + 1) (fuel - 1)
  termination_by fuel
```
