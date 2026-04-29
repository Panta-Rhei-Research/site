---
{
  "projection_kind": "taulib_declaration",
  "title": "NowHypersurface",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/now-hypersurface/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::NowHypersurface",
  "declaration_slug": "now-hypersurface",
  "kind": "structure",
  "name": "NowHypersurface",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 171,
  "source_line_end": 178,
  "registry_ids": [
    "V.D22"
  ],
  "related_registry_items": [
    {
      "id": "V.D22",
      "title": "Sigma-Now Hypersurface",
      "url": "/registry/object/V.D22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L171-L178",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L171-L178",
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

- Module: [TauLib.BookV.Temporal.TemporalIgnition](/verify/taulib/docs/book-v-temporal-temporal-ignition/)
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L171-L178)
- Source range: L171-L178
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D22` — Sigma-Now Hypersurface

## Immediate Comment / Docstring

```lean
/-- [V.D22] The now-hypersurface: the current refinement depth n_*
    of the universe. The observed state of the universe corresponds
    to a specific depth in the refinement tower.

    n_* is far beyond both ignition depth and opening depth:
    n_* >> n_open >> n_ign. -/
```

## Source Excerpt

```lean
structure NowHypersurface where
  /-- Current depth n_*. -/
  current_depth : ProtoTime
  /-- Reference ignition depth. -/
  ignition : IgnitionDepth
  /-- Current depth exceeds ignition. -/
  past_ignition : current_depth.tick > ignition.n_ign
  deriving Repr
```
