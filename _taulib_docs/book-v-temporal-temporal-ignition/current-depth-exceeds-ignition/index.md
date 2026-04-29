---
{
  "projection_kind": "taulib_declaration",
  "title": "current_depth_exceeds_ignition",
  "permalink": "/verify/taulib/docs/book-v-temporal-temporal-ignition/current-depth-exceeds-ignition/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.TemporalIgnition`.",
  "declaration_id": "TauLib.BookV.Temporal.TemporalIgnition::current_depth_exceeds_ignition",
  "declaration_slug": "current-depth-exceeds-ignition",
  "kind": "theorem",
  "name": "current_depth_exceeds_ignition",
  "module_name": "TauLib.BookV.Temporal.TemporalIgnition",
  "module_url": "/verify/taulib/docs/book-v-temporal-temporal-ignition/",
  "source_line_start": 189,
  "source_line_end": 191,
  "registry_ids": [
    "V.T12"
  ],
  "related_registry_items": [
    {
      "id": "V.T12",
      "title": "Now-Within-Epoch Theorem",
      "url": "/registry/object/V.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L189-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L189-L191",
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
- Source path: [`TauLib/BookV/Temporal/TemporalIgnition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/TemporalIgnition.lean#L189-L191)
- Source range: L189-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T12` — Now-Within-Epoch Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T12] The current depth n_* far exceeds the ignition depth n_ign.

    This is structurally enforced: the refinement tower has advanced
    well beyond the ignition threshold. The "far exceeds" is captured
    by the past_ignition field of NowHypersurface. -/
```

## Source Excerpt

```lean
theorem current_depth_exceeds_ignition (h : NowHypersurface) :
    h.current_depth.tick > h.ignition.n_ign :=
  h.past_ignition
```
