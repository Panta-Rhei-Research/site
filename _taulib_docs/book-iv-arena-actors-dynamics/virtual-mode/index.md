---
{
  "projection_kind": "taulib_declaration",
  "title": "VirtualMode",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/virtual-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::VirtualMode",
  "declaration_slug": "virtual-mode",
  "kind": "structure",
  "name": "VirtualMode",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 84,
  "source_line_end": 91,
  "registry_ids": [
    "IV.D269"
  ],
  "related_registry_items": [
    {
      "id": "IV.D269",
      "title": "Virtual particle",
      "url": "/registry/object/IV.D269/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L84-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.ActorsDynamics",
        "url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L84-L91",
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

- Module: [TauLib.BookIV.Arena.ActorsDynamics](/verify/taulib/docs/book-iv-arena-actors-dynamics/)
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L84-L91)
- Source range: L84-L91
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D269` — Virtual particle

## Immediate Comment / Docstring

```lean
/-- [IV.D269] Virtual particle: a transient defect existing only within
    fiber exchange. Off-shell: does not satisfy the mass-energy relation. -/
```

## Source Excerpt

```lean
structure VirtualMode where
  /-- Always fiber carrier. -/
  carrier : CarrierType
  carrier_is_fiber : carrier = .Fiber
  /-- Transient (not asymptotic). -/
  transient : Bool
  transient_true : transient = true
  deriving Repr
```
