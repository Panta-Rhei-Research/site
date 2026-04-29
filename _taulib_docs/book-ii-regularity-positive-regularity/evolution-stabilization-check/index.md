---
{
  "projection_kind": "taulib_declaration",
  "title": "evolution_stabilization_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-positive-regularity/evolution-stabilization-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PositiveRegularity`.",
  "declaration_id": "TauLib.BookII.Regularity.PositiveRegularity::evolution_stabilization_check",
  "declaration_slug": "evolution-stabilization-check",
  "kind": "def",
  "name": "evolution_stabilization_check",
  "module_name": "TauLib.BookII.Regularity.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-ii-regularity-positive-regularity/",
  "source_line_start": 215,
  "source_line_end": 239,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L215-L239",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L215-L239",
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
- Source path: [`TauLib/BookII/Regularity/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PositiveRegularity.lean#L215-L239)
- Source range: L215-L239
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Evolution stabilization: for regular points, the evolution operator
    output at the regularity depth equals the output at all deeper stages. -/
```

## Source Excerpt

```lean
def evolution_stabilization_check (bound db : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let rd := regularity_depth x db
      if rd > db then go (x + 1) (fuel - 1)  -- not regular, skip
      else
        -- At the regularity depth, the evolved point stabilizes
        let bp_rd := interior_bipolar (from_tau_idx (reduce x rd))
        -- Check all deeper stages agree
        let ok := check_deep x bp_rd rd db (db - rd + 1)
        ok && go (x + 1) (fuel - 1)
  termination_by fuel
  check_deep (x : Nat) (bp_rd : SectorPair) (rd k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let bp_k := interior_bipolar (from_tau_idx (reduce x k))
      -- B and C sectors should match the regularity-depth values
      (bp_k.b_sector == bp_rd.b_sector && bp_k.c_sector == bp_rd.c_sector) &&
      check_deep x bp_rd rd (k + 1) (fuel - 1)
  termination_by fuel
```
