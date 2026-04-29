---
{
  "projection_kind": "taulib_declaration",
  "title": "RadiationMode",
  "permalink": "/verify/taulib/docs/book-iv-arena-actors-dynamics/radiation-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.ActorsDynamics`.",
  "declaration_id": "TauLib.BookIV.Arena.ActorsDynamics::RadiationMode",
  "declaration_slug": "radiation-mode",
  "kind": "structure",
  "name": "RadiationMode",
  "module_name": "TauLib.BookIV.Arena.ActorsDynamics",
  "module_url": "/verify/taulib/docs/book-iv-arena-actors-dynamics/",
  "source_line_start": 62,
  "source_line_end": 69,
  "registry_ids": [
    "IV.D268"
  ],
  "related_registry_items": [
    {
      "id": "IV.D268",
      "title": "Radiation",
      "url": "/registry/object/IV.D268/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L62-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L62-L69",
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
- Source path: [`TauLib/BookIV/Arena/ActorsDynamics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/ActorsDynamics.lean#L62-L69)
- Source range: L62-L69
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D268` — Radiation

## Immediate Comment / Docstring

```lean
/-- [IV.D268] Radiation: a non-localized (base-only) propagation mode.
    No fiber stiffness → massless. Travels at c along base τ¹. -/
```

## Source Excerpt

```lean
structure RadiationMode where
  /-- Always base carrier. -/
  carrier : CarrierType
  carrier_is_base : carrier = .Base
  /-- Always massless. -/
  massive : Bool
  massless : massive = false
  deriving Repr
```
