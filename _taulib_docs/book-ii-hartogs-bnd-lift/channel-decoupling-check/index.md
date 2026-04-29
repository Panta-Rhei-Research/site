---
{
  "projection_kind": "taulib_declaration",
  "title": "channel_decoupling_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/channel-decoupling-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::channel_decoupling_check",
  "declaration_slug": "channel-decoupling-check",
  "kind": "def",
  "name": "channel_decoupling_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 259,
  "source_line_end": 285,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L259-L285",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L259-L285",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L259-L285)
- Source range: L259-L285
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Stronger channel independence: under the BndLift, the B and C
    coordinates of the ABCD chart evolve independently.
    For x and x + P_n (same stage-n, different stage-(n+1)):
    the B-change and C-change are decoupled.

    Evidence: at representative indices, the B-sector and C-sector
    projections of the bipolar decomposition remain orthogonal after lift. -/
```

## Source Excerpt

```lean
def channel_decoupling_check (stage bound : TauIdx) : Bool :=
  let pn := primorial stage
  go 2 (bound + 1) pn
where
  go (x fuel : Nat) (pn : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      -- Compare x with x + P_n (lifted by one primorial step)
      let y := x + pn
      if y > bound then go (x + 1) (fuel - 1) pn
      else
        -- Same stage-n projection
        let same_stage := reduce x stage == reduce y stage
        -- Get bipolar decompositions
        let bp_x := interior_bipolar (from_tau_idx x)
        let bp_y := interior_bipolar (from_tau_idx y)
        -- Idempotent projections remain orthogonal for both
        let orth_x := SectorPair.mul
                        (SectorPair.mul e_plus_sector bp_x)
                        (SectorPair.mul e_minus_sector bp_x) == ⟨0, 0⟩
        let orth_y := SectorPair.mul
                        (SectorPair.mul e_plus_sector bp_y)
                        (SectorPair.mul e_minus_sector bp_y) == ⟨0, 0⟩
        same_stage && orth_x && orth_y &&
        go (x + 1) (fuel - 1) pn
  termination_by fuel
```
