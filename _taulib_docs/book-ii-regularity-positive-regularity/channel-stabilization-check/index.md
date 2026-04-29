---
{
  "projection_kind": "taulib_declaration",
  "title": "channel_stabilization_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/channel-stabilization-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::channel_stabilization_check",
  "declaration_slug": "channel-stabilization-check",
  "kind": "def",
  "name": "channel_stabilization_check",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 248,
  "source_line_end": 282,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L248-L282",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L248-L282",
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
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L248-L282)
- Source range: L248-L282
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Channel-wise evolution stabilization: the B-component stabilizes
    independently of the C-component, and vice versa.
    This connects regularity back to the idempotent decomposition. -/
```

## Source Excerpt

```lean
def channel_stabilization_check (bound db : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let rd_b := b_stabilization_depth x db
      let rd_c := c_stabilization_depth x db
      -- B-channel stabilizes independently
      let b_ok := if rd_b ≤ db then
        let b_val := (from_tau_idx (reduce x rd_b)).b
        check_b_stable x b_val rd_b db (db - rd_b + 1)
      else true
      -- C-channel stabilizes independently
      let c_ok := if rd_c ≤ db then
        let c_val := (from_tau_idx (reduce x rd_c)).c
        check_c_stable x c_val rd_c db (db - rd_c + 1)
      else true
      b_ok && c_ok && go (x + 1) (fuel - 1)
  termination_by fuel
  check_b_stable (x : Nat) (target : Nat) (from_k to_k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if from_k > to_k then true
    else
      let bk := (from_tau_idx (reduce x from_k)).b
      (bk == target) && check_b_stable x target (from_k + 1) to_k (fuel - 1)
  termination_by fuel
  check_c_stable (x : Nat) (target : Nat) (from_k to_k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if from_k > to_k then true
    else
      let ck := (from_tau_idx (reduce x from_k)).c
      (ck == target) && check_c_stable x target (from_k + 1) to_k (fuel - 1)
  termination_by fuel
```
