---
{
  "projection_kind": "taulib_declaration",
  "title": "extension_channel_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/extension-channel-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::extension_channel_check",
  "declaration_slug": "extension-channel-check",
  "kind": "def",
  "name": "extension_channel_check",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 65,
  "source_line_end": 90,
  "registry_ids": [
    "II.L12"
  ],
  "related_registry_items": [
    {
      "id": "II.L12",
      "title": "Extension in Split-Complex Codomain",
      "url": "/registry/object/II.L12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L65-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L65-L90",
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L65-L90)
- Source range: L65-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L12` — Extension in Split-Complex Codomain

## Immediate Comment / Docstring

```lean
/-- [II.L12] Extension channel check: for each boundary point x,
    bndlift(x, k) preserves the B/C decomposition.

    The B-channel of the lifted value comes from the B-channel of x:
    specifically, the B-coordinate of from_tau_idx(bndlift(x, k))
    is determined by the B-coordinate of from_tau_idx(reduce(x, k)).

    Similarly, the C-channel of the lifted value comes from the
    C-channel of x.

    Since bndlift(x, k) = reduce(x, k+1), and
    reduce(reduce(x, k+1), k) = reduce(x, k), the stage-k projection
    of the lifted value recovers the original stage-k data. The ABCD chart
    of the recovered data matches the original chart. -/
```

## Source Excerpt

```lean
def extension_channel_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- Stage-k data
      let rx_k := reduce x k
      let chart_k := from_tau_idx rx_k
      let bp_k : SectorPair := interior_bipolar chart_k
      -- Lifted to stage k+1 via bndlift
      let lifted := bndlift x k
      -- Reduce the lifted value back to stage k
      let reduced_lift := reduce lifted k
      let chart_reduced := from_tau_idx reduced_lift
      let bp_reduced : SectorPair := interior_bipolar chart_reduced
      -- B-channel preserved: the B-coordinate at stage k is recovered
      let b_ok := bp_reduced.b_sector == bp_k.b_sector
      -- C-channel preserved: the C-coordinate at stage k is recovered
      let c_ok := bp_reduced.c_sector == bp_k.c_sector
      -- Full sector pair matches
      let full_ok := bp_reduced == bp_k
      b_ok && c_ok && full_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
