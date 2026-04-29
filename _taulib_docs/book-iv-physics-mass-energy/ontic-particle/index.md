---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticParticle",
  "permalink": "/verify/taulib/docs/book-iv-physics-mass-energy/ontic-particle/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::OnticParticle",
  "declaration_slug": "ontic-particle",
  "kind": "structure",
  "name": "OnticParticle",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/verify/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 169,
  "source_line_end": 176,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L169-L176",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.MassEnergy",
        "url": "/verify/taulib/docs/book-iv-physics-mass-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L169-L176",
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

- Module: [TauLib.BookIV.Physics.MassEnergy](/verify/taulib/docs/book-iv-physics-mass-energy/)
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L169-L176)
- Source range: L169-L176
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ontic particles have fiber carrier (stable T² topology). -/
```

## Source Excerpt

```lean
structure OnticParticle where
  /-- Mass of the particle. -/
  mass : MassIndex
  /-- Ontic particles are persistent. -/
  persistent_proof : mass.is_persistent = true
  /-- Ontic particles live on the fiber T². -/
  fiber_proof : mass.carrier = .Fiber
  deriving Repr
```
