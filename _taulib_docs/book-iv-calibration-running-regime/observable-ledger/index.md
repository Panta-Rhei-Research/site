---
{
  "projection_kind": "taulib_declaration",
  "title": "ObservableLedger",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/observable-ledger/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::ObservableLedger",
  "declaration_slug": "observable-ledger",
  "kind": "structure",
  "name": "ObservableLedger",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 59,
  "source_line_end": 66,
  "registry_ids": [
    "IV.D300"
  ],
  "related_registry_items": [
    {
      "id": "IV.D300",
      "title": "Coupling Ledger and Observable Ledger",
      "url": "/registry/object/IV.D300/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L59-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.RunningRegime",
        "url": "/verify/taulib/docs/book-iv-calibration-running-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L59-L66",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L59-L66)
- Source range: L59-L66
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D300` — Coupling Ledger and Observable Ledger

## Immediate Comment / Docstring

```lean
/-- [IV.D300] The observable ledger at scale μ: the apparent coupling
    values as seen by instruments at energy scale μ.
    Distinct from the ontic coupling ledger (which is μ-independent). -/
```

## Source Excerpt

```lean
structure ObservableLedger where
  /-- Number of coupling entries (same as ontic: 10). -/
  entry_count : Nat
  entry_eq : entry_count = 10
  /-- Scale-dependent (unlike ontic ledger). -/
  scale_dependent : Bool
  scale_true : scale_dependent = true
  deriving Repr
```
