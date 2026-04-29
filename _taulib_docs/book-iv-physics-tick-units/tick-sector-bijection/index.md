---
{
  "projection_kind": "taulib_declaration",
  "title": "tick_sector_bijection",
  "permalink": "/verify/taulib/docs/book-iv-physics-tick-units/tick-sector-bijection/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.TickUnits`.",
  "declaration_id": "TauLib.BookIV.Physics.TickUnits::tick_sector_bijection",
  "declaration_slug": "tick-sector-bijection",
  "kind": "theorem",
  "name": "tick_sector_bijection",
  "module_name": "TauLib.BookIV.Physics.TickUnits",
  "module_url": "/verify/taulib/docs/book-iv-physics-tick-units/",
  "source_line_start": 135,
  "source_line_end": 146,
  "registry_ids": [
    "IV.T125"
  ],
  "related_registry_items": [
    {
      "id": "IV.T125",
      "title": "Tick-Sector Bijection",
      "url": "/registry/object/IV.T125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L135-L146",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L135-L146",
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
- Source path: [`TauLib/BookIV/Physics/TickUnits.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L135-L146)
- Source range: L135-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T125` — Tick-Sector Bijection

## Immediate Comment / Docstring

```lean
/-- [IV.T125] Tick-Sector Bijection: each tick kind maps to a distinct sector,
    and each sector has exactly one tick kind. -/
```

## Source Excerpt

```lean
theorem tick_sector_bijection :
    TickKind.AlphaTick.sector ≠ TickKind.PiStep.sector ∧
    TickKind.AlphaTick.sector ≠ TickKind.GammaOscillation.sector ∧
    TickKind.AlphaTick.sector ≠ TickKind.EtaStep.sector ∧
    TickKind.AlphaTick.sector ≠ TickKind.OmegaCrossing.sector ∧
    TickKind.PiStep.sector ≠ TickKind.GammaOscillation.sector ∧
    TickKind.PiStep.sector ≠ TickKind.EtaStep.sector ∧
    TickKind.PiStep.sector ≠ TickKind.OmegaCrossing.sector ∧
    TickKind.GammaOscillation.sector ≠ TickKind.EtaStep.sector ∧
    TickKind.GammaOscillation.sector ≠ TickKind.OmegaCrossing.sector ∧
    TickKind.EtaStep.sector ≠ TickKind.OmegaCrossing.sector := by
  simp [TickKind.sector]
```
