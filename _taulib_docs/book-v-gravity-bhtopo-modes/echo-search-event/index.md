---
{
  "projection_kind": "taulib_declaration",
  "title": "EchoSearchEvent",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-search-event/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::EchoSearchEvent",
  "declaration_slug": "echo-search-event",
  "kind": "structure",
  "name": "EchoSearchEvent",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 631,
  "source_line_end": 638,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L631-L638",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L631-L638",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L631-L638)
- Source range: L631-L638
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Echo search event entry — V.D283 -/
```

## Source Excerpt

```lean
structure EchoSearchEvent where
  event_name : String
  final_mass_x10 : Nat      -- M_final in 0.1 M☉
  main_snr_x10 : Nat        -- main SNR × 10
  echo_snr_x100 : Nat       -- (1,0) echo SNR × 100
  t_plus_us : Nat            -- t₊ in microseconds
  t_minus_us : Nat           -- t₋ in microseconds
  deriving Repr
```
