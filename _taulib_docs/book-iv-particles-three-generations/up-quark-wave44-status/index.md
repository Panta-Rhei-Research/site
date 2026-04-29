---
{
  "projection_kind": "taulib_declaration",
  "title": "UpQuarkWave44Status",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/up-quark-wave44-status/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::UpQuarkWave44Status",
  "declaration_slug": "up-quark-wave44-status",
  "kind": "structure",
  "name": "UpQuarkWave44Status",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2774,
  "source_line_end": 2783,
  "registry_ids": [
    "IV.R432"
  ],
  "related_registry_items": [
    {
      "id": "IV.R432",
      "title": "Up Quark Status Update (Wave 44)",
      "url": "/registry/object/IV.R432/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2774-L2783",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2774-L2783",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2774-L2783)
- Source range: L2774-L2783
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R432` — Up Quark Status Update (Wave 44)

## Immediate Comment / Docstring

```lean
/-- [IV.R432] Up quark status update (Wave 44). -/
```

## Source Excerpt

```lean
structure UpQuarkWave44Status where
  /-- Direct formula deviation (ppm). -/
  direct_ppm : Int := 395
  /-- Chain formula deviation (ppm). -/
  chain_ppm : Int := 31043
  /-- Improvement factor. -/
  improvement : Nat := 79
  /-- All six quarks sub-1600 ppm now. -/
  all_sub_1600 : Bool := true
  deriving Repr
```
