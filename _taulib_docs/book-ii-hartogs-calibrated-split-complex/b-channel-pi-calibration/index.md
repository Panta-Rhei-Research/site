---
{
  "projection_kind": "taulib_declaration",
  "title": "b_channel_pi_calibration",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/b-channel-pi-calibration/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CalibratedSplitComplex`.",
  "declaration_id": "TauLib.BookII.Hartogs.CalibratedSplitComplex::b_channel_pi_calibration",
  "declaration_slug": "b-channel-pi-calibration",
  "kind": "def",
  "name": "b_channel_pi_calibration",
  "module_name": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/",
  "source_line_start": 193,
  "source_line_end": 211,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L193-L211",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
        "url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L193-L211",
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

- Module: [TauLib.BookII.Hartogs.CalibratedSplitComplex](/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/)
- Source path: [`TauLib/BookII/Hartogs/CalibratedSplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L193-L211)
- Source range: L193-L211
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The B-channel is π-calibrated: the number of B-residues at stage k
    equals p_k, and each arc has angular width 2π/p_k.
    In scaled arithmetic: full circle = 2 * pi_cal, arc = 2 * pi_cal / p_k.
    Verify: p_k arcs sum to a full circle. -/
```

## Source Excerpt

```lean
def b_channel_pi_calibration (stages : TauIdx) : Bool :=
  let h := calibrated_htau
  go 1 (stages + 1) h.pi_cal
where
  go (k fuel : Nat) (pi_cal : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      let pk := nth_prime k
      -- Full circle = 2 * pi_cal
      -- p_k arcs of width 2*pi_cal/p_k should sum to 2*pi_cal
      -- Evidence: pk * (2 * pi_cal / pk) is close to 2 * pi_cal
      let arc_width := 2 * pi_cal / pk
      let total := pk * arc_width
      let full := 2 * pi_cal
      -- Within 1 arc-width of the full circle (integer rounding)
      (full >= total && full - total < arc_width + 1) &&
      go (k + 1) (fuel - 1) pi_cal
  termination_by fuel
```
