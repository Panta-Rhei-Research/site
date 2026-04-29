---
{
  "projection_kind": "taulib_declaration",
  "title": "pentation_channel_exhaustion",
  "permalink": "/verify/taulib/docs/book-i-orbit-ladder/pentation-channel-exhaustion/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Ladder`.",
  "declaration_id": "TauLib.BookI.Orbit.Ladder::pentation_channel_exhaustion",
  "declaration_slug": "pentation-channel-exhaustion",
  "kind": "theorem",
  "name": "pentation_channel_exhaustion",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_url": "/verify/taulib/docs/book-i-orbit-ladder/",
  "source_line_start": 132,
  "source_line_end": 134,
  "registry_ids": [
    "I.L01"
  ],
  "related_registry_items": [
    {
      "id": "I.L01",
      "title": "Pentation Non-Injectivity",
      "url": "/registry/object/I.L01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L132-L134",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Ladder",
        "url": "/verify/taulib/docs/book-i-orbit-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L132-L134",
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

- Module: [TauLib.BookI.Orbit.Ladder](/verify/taulib/docs/book-i-orbit-ladder/)
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L132-L134)
- Source range: L132-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.L01` — Pentation Non-Injectivity

## Immediate Comment / Docstring

```lean
/-- [I.L01] Pentation cannot be assigned a canonical orbit channel:
    all 3 solenoidal generators are consumed by levels 1-3,
    and alpha is the counting scaffold. No 5th channel exists (K6).

    This is the channel-exhaustion form of the saturation argument. -/
```

## Source Excerpt

```lean
theorem pentation_channel_exhaustion :
    ladderChannel .tet_level = none := by
  rfl
```
