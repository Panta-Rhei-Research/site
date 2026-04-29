---
{
  "projection_kind": "taulib_declaration",
  "title": "tick_exhaustion",
  "permalink": "/verify/taulib/docs/book-iv-physics-tick-units/tick-exhaustion/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.TickUnits`.",
  "declaration_id": "TauLib.BookIV.Physics.TickUnits::tick_exhaustion",
  "declaration_slug": "tick-exhaustion",
  "kind": "theorem",
  "name": "tick_exhaustion",
  "module_name": "TauLib.BookIV.Physics.TickUnits",
  "module_url": "/verify/taulib/docs/book-iv-physics-tick-units/",
  "source_line_start": 149,
  "source_line_end": 152,
  "registry_ids": [
    "IV.T126"
  ],
  "related_registry_items": [
    {
      "id": "IV.T126",
      "title": "Tick Exhaustion",
      "url": "/registry/object/IV.T126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L149-L152",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.TickUnits",
        "url": "/verify/taulib/docs/book-iv-physics-tick-units/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L149-L152",
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

- Module: [TauLib.BookIV.Physics.TickUnits](/verify/taulib/docs/book-iv-physics-tick-units/)
- Source path: [`TauLib/BookIV/Physics/TickUnits.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L149-L152)
- Source range: L149-L152
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T126` — Tick Exhaustion

## Immediate Comment / Docstring

```lean
/-- [IV.T126] Tick Exhaustion: every tick kind is one of the five. -/
```

## Source Excerpt

```lean
theorem tick_exhaustion (t : TickKind) :
    t = .AlphaTick ∨ t = .PiStep ∨ t = .GammaOscillation ∨
    t = .EtaStep ∨ t = .OmegaCrossing := by
  cases t <;> simp
```
