---
{
  "projection_kind": "taulib_declaration",
  "title": "TickKind",
  "permalink": "/verify/taulib/docs/book-iv-physics-tick-units/tick-kind/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.TickUnits`.",
  "declaration_id": "TauLib.BookIV.Physics.TickUnits::TickKind",
  "declaration_slug": "tick-kind",
  "kind": "inductive",
  "name": "TickKind",
  "module_name": "TauLib.BookIV.Physics.TickUnits",
  "module_url": "/verify/taulib/docs/book-iv-physics-tick-units/",
  "source_line_start": 54,
  "source_line_end": 70,
  "registry_ids": [
    "IV.D322"
  ],
  "related_registry_items": [
    {
      "id": "IV.D322",
      "title": "Tick Kind",
      "url": "/registry/object/IV.D322/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L54-L70",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L54-L70",
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

- Module: [TauLib.BookIV.Physics.TickUnits](/verify/taulib/docs/book-iv-physics-tick-units/)
- Source path: [`TauLib/BookIV/Physics/TickUnits.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L54-L70)
- Source range: L54-L70
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D322` — Tick Kind

## Immediate Comment / Docstring

```lean
/-- [IV.D322] The 5 tick kinds, one per generator/sector.
    Each tick is the minimal non-identity endomorphism in its sector. -/
```

## Source Excerpt

```lean
inductive TickKind where
  /-- α-tick: minimal gravitational endomorphism of τ¹ in sector D.
      The internal unit of temporal duration. -/
  | AlphaTick
  /-- π-step: minimal weak endomorphism of τ¹ in sector A.
      The internal unit of weak process evolution. -/
  | PiStep
  /-- γ-oscillation: minimal EM endomorphism of T² in sector B.
      The internal unit of electromagnetic phase. -/
  | GammaOscillation
  /-- η-step: minimal strong endomorphism of T² in sector C.
      The internal unit of confinement-scale process. -/
  | EtaStep
  /-- ω-crossing: minimal lobe automorphism at B∩C in sector ω.
      The internal unit of mass acquisition. -/
  | OmegaCrossing
  deriving Repr, DecidableEq, BEq, Inhabited
```
