---
{
  "projection_kind": "taulib_declaration",
  "title": "three_epochs_nonempty",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/three-epochs-nonempty/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::three_epochs_nonempty",
  "declaration_slug": "three-epochs-nonempty",
  "kind": "theorem",
  "name": "three_epochs_nonempty",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 132,
  "source_line_end": 143,
  "registry_ids": [
    "V.T11"
  ],
  "related_registry_items": [
    {
      "id": "V.T11",
      "title": "Epoch Existence Theorem",
      "url": "/registry/object/V.T11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L132-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L132-L143",
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
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L132-L143)
- Source range: L132-L143
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T11` — Epoch Existence Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T11] All three temporal epochs are nonempty: there exist depths
    in each epoch.

    Given n_ign > 1 and n_open > n_ign, all three epochs contain at
    least one depth:
    - PreTemporal contains depth 1 (since 1 < n_ign)
    - Opening contains depth n_ign (since n_ign < n_open)
    - Temporal contains depth n_open (since n_open ≥ n_open) -/
```

## Source Excerpt

```lean
theorem three_epochs_nonempty (n_ign n_open : Nat)
    (h_ign : n_ign > 1) (h_open : n_open > n_ign) :
    -- PreTemporal is nonempty
    (∃ t : ProtoTime, epoch_classification t n_ign n_open = .PreTemporal) ∧
    -- Opening is nonempty
    (∃ t : ProtoTime, epoch_classification t n_ign n_open = .Opening) ∧
    -- Temporal is nonempty
    (∃ t : ProtoTime, epoch_classification t n_ign n_open = .Temporal) := by
  refine ⟨⟨⟨1, by omega⟩, ?_⟩, ⟨⟨n_ign, by omega⟩, ?_⟩, ⟨⟨n_open, by omega⟩, ?_⟩⟩
  · simp [epoch_classification]; omega
  · simp [epoch_classification]; omega
  · simp [epoch_classification]; omega
```
