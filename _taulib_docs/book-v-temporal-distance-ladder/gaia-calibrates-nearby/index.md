---
{
  "projection_kind": "taulib_declaration",
  "title": "gaia_calibrates_nearby",
  "permalink": "/verify/taulib/docs/book-v-temporal-distance-ladder/gaia-calibrates-nearby/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.DistanceLadder`.",
  "declaration_id": "TauLib.BookV.Temporal.DistanceLadder::gaia_calibrates_nearby",
  "declaration_slug": "gaia-calibrates-nearby",
  "kind": "theorem",
  "name": "gaia_calibrates_nearby",
  "module_name": "TauLib.BookV.Temporal.DistanceLadder",
  "module_url": "/verify/taulib/docs/book-v-temporal-distance-ladder/",
  "source_line_start": 220,
  "source_line_end": 221,
  "registry_ids": [
    "V.R41"
  ],
  "related_registry_items": [
    {
      "id": "V.R41",
      "title": "Gaia and the tau-readout",
      "url": "/registry/object/V.R41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L220-L221",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.DistanceLadder",
        "url": "/verify/taulib/docs/book-v-temporal-distance-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L220-L221",
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

- Module: [TauLib.BookV.Temporal.DistanceLadder](/verify/taulib/docs/book-v-temporal-distance-ladder/)
- Source path: [`TauLib/BookV/Temporal/DistanceLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/DistanceLadder.lean#L220-L221)
- Source range: L220-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R41` — Gaia and the tau-readout

## Immediate Comment / Docstring

```lean
/-- [V.R41] Gaia calibrates at nearby depths: Parallax rung operates at
    kpc scale (log10_parsec = 3). -/
```

## Source Excerpt

```lean
theorem gaia_calibrates_nearby :
    DistanceLadderRung.Parallax.log10_parsec = 3 := by rfl
```
