---
{
  "projection_kind": "taulib_declaration",
  "title": "TickKind.measuredInvariant",
  "permalink": "/verify/taulib/docs/book-iv-physics-tick-units/measured-invariant/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.TickUnits`.",
  "declaration_id": "TauLib.BookIV.Physics.TickUnits::TickKind.measuredInvariant",
  "declaration_slug": "measured-invariant",
  "kind": "def",
  "name": "TickKind.measuredInvariant",
  "module_name": "TauLib.BookIV.Physics.TickUnits",
  "module_url": "/verify/taulib/docs/book-iv-physics-tick-units/",
  "source_line_start": 122,
  "source_line_end": 127,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L122-L127",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L122-L127",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Physics/TickUnits.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/TickUnits.lean#L122-L127)
- Source range: L122-L127
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The primary invariant measured by counting a given tick kind. -/
```

## Source Excerpt

```lean
def TickKind.measuredInvariant : TickKind → PrimaryInvariant
  | .AlphaTick      => .Gravity  -- counting α-ticks measures gravitational duration
  | .PiStep         => .Time     -- counting π-steps measures temporal evolution
  | .GammaOscillation => .Energy -- counting γ-oscillations measures energy
  | .EtaStep        => .Mass     -- counting η-steps measures confinement (mass)
  | .OmegaCrossing  => .Entropy  -- counting ω-crossings measures entropy production
```
