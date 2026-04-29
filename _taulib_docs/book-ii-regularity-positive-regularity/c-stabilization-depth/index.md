---
{
  "projection_kind": "taulib_declaration",
  "title": "c_stabilization_depth",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/c-stabilization-depth/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::c_stabilization_depth",
  "declaration_slug": "c-stabilization-depth",
  "kind": "def",
  "name": "c_stabilization_depth",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 76,
  "source_line_end": 94,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L76-L94",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L76-L94",
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
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L76-L94)
- Source range: L76-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D49` — Tau-Regularity

## Immediate Comment / Docstring

```lean
/-- [II.D49] C-channel stabilization depth: the smallest stage k
    at which the C-coordinate stabilizes through all subsequent stages. -/
```

## Source Excerpt

```lean
def c_stabilization_depth (x db : TauIdx) : Nat :=
  go x 1 (db + 1)
where
  go (x k fuel : Nat) : Nat :=
    if fuel = 0 then db + 1
    else if k > db then db + 1
    else
      let ck := (from_tau_idx (reduce x k)).c
      let stable := check_stable x ck (k + 1) (db - k)
      if stable then k
      else go x (k + 1) (fuel - 1)
  termination_by fuel
  check_stable (x : Nat) (target : Nat) (j fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if j > db then true
    else
      let cj := (from_tau_idx (reduce x j)).c
      (cj == target) && check_stable x target (j + 1) (fuel - 1)
  termination_by fuel
```
