---
{
  "projection_kind": "taulib_declaration",
  "title": "epoch_exhaust",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/epoch-exhaust/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::epoch_exhaust",
  "declaration_slug": "epoch-exhaust",
  "kind": "theorem",
  "name": "epoch_exhaust",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 221,
  "source_line_end": 223,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L221-L223",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L221-L223",
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
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L221-L223)
- Source range: L221-L223
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All temporal epochs are accounted for. -/
```

## Source Excerpt

```lean
theorem epoch_exhaust (e : TemporalEpoch) :
    e = .PreTemporal ∨ e = .Opening ∨ e = .Temporal := by
  cases e <;> simp
```
