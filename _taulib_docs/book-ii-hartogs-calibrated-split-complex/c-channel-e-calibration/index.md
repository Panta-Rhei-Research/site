---
{
  "projection_kind": "taulib_declaration",
  "title": "c_channel_e_calibration",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/c-channel-e-calibration/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CalibratedSplitComplex`.",
  "declaration_id": "TauLib.BookII.Hartogs.CalibratedSplitComplex::c_channel_e_calibration",
  "declaration_slug": "c-channel-e-calibration",
  "kind": "def",
  "name": "c_channel_e_calibration",
  "module_name": "TauLib.BookII.Hartogs.CalibratedSplitComplex",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-calibrated-split-complex/",
  "source_line_start": 218,
  "source_line_end": 230,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L218-L230",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L218-L230",
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
- Source path: [`TauLib/BookII/Hartogs/CalibratedSplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CalibratedSplitComplex.lean#L218-L230)
- Source range: L218-L230
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The C-channel is e-calibrated: the growth ratio P_{k+1}/P_k = p_{k+1},
    and primorial growth is super-exponential with base related to e.
    Evidence: ln(P_k) ~ sum_{i=1}^{k} ln(p_i) grows; the average
    growth factor approaches e for large k via PNT.
    At small k: verify p_{k+1} >= 2 (each step at least doubles). -/
```

## Source Excerpt

```lean
def c_channel_e_calibration (stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      -- Growth factor = p_{k+1} >= 2
      (pk > 0 && pk1 / pk >= 2) &&
      go (k + 1) (fuel - 1)
  termination_by fuel
```
