---
{
  "projection_kind": "taulib_declaration",
  "title": "TemporalEpoch",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/temporal-epoch/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::TemporalEpoch",
  "declaration_slug": "temporal-epoch",
  "kind": "inductive",
  "name": "TemporalEpoch",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 69,
  "source_line_end": 79,
  "registry_ids": [
    "V.D20"
  ],
  "related_registry_items": [
    {
      "id": "V.D20",
      "title": "Three Temporal Epochs",
      "url": "/registry/object/V.D20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L69-L79",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L69-L79",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookV.Temporal.TemporalIgnition](/verify/taulib/docs/book-v-temporal-temporal-ignition/)
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L69-L79)
- Source range: L69-L79
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D20` — Three Temporal Epochs

## Immediate Comment / Docstring

```lean
/-- [V.D20] The three temporal epochs of the α-orbit.

    The partition is exhaustive and ordered:
    PreTemporal < Opening < Temporal in depth. -/
```

## Source Excerpt

```lean
inductive TemporalEpoch where
  /-- Pre-temporal: spectral labels incomplete, ticks indistinguishable.
      Depth range: 1 ≤ n < n_ign. -/
  | PreTemporal
  /-- Opening: full labels present, rapid equilibration.
      Depth range: n_ign ≤ n < n_open. Corresponds to early universe. -/
  | Opening
  /-- Temporal: stable sector differentiation, well-defined physical time.
      Depth range: n ≥ n_open. The current epoch. -/
  | Temporal
  deriving Repr, DecidableEq, BEq, Inhabited
```
