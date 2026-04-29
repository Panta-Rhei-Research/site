---
{
  "projection_kind": "taulib_declaration",
  "title": "pre_temporal_no_labels",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/pre-temporal-no-labels/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::pre_temporal_no_labels",
  "declaration_slug": "pre-temporal-no-labels",
  "kind": "theorem",
  "name": "pre_temporal_no_labels",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 156,
  "source_line_end": 159,
  "registry_ids": [
    "V.P04"
  ],
  "related_registry_items": [
    {
      "id": "V.P04",
      "title": "Pre-Temporal Indistinguishability",
      "url": "/registry/object/V.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L156-L159",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.TemporalIgnition",
        "url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L156-L159",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Temporal.TemporalIgnition](/verify/taulib/docs/book-v-temporal-temporal-ignition/)
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L156-L159)
- Source range: L156-L159
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P04` — Pre-Temporal Indistinguishability

## Immediate Comment / Docstring

```lean
/-- [V.P04] In the pre-temporal epoch, no subsystem can distinguish
    ticks. The spectral labels are incomplete, so sector differentiation
    has not yet occurred. Ticks exist (the refinement tower advances)
    but they carry no physically distinguishable signatures.

    Formalized: at pre-temporal depth, the epoch classification is
    PreTemporal (i.e., full sector labels are NOT yet present). -/
```

## Source Excerpt

```lean
theorem pre_temporal_no_labels (t : ProtoTime) (n_ign n_open : Nat)
    (h : t.tick < n_ign) :
    epoch_classification t n_ign n_open = .PreTemporal := by
  simp [epoch_classification, h]
```
