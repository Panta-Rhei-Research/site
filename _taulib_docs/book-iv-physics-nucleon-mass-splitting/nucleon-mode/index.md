---
{
  "projection_kind": "taulib_declaration",
  "title": "NucleonMode",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nucleon-mode/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::NucleonMode",
  "declaration_slug": "nucleon-mode",
  "kind": "inductive",
  "name": "NucleonMode",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 59,
  "source_line_end": 62,
  "registry_ids": [
    "IV.D340"
  ],
  "related_registry_items": [
    {
      "id": "IV.D340",
      "title": "Nucleon Boundary Mode",
      "url": "/registry/object/IV.D340/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L59-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L59-L62",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L59-L62)
- Source range: L59-L62
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D340` — Nucleon Boundary Mode

## Immediate Comment / Docstring

```lean
/-- [IV.D340] The two nucleon modes on the T² micro-donut.
    Proton = χ₊-dominant (B-sector, EM); neutron = χ₋-dominant (C-sector, strong). -/
```

## Source Excerpt

```lean
inductive NucleonMode where
  | Proton  : NucleonMode   -- χ₊, B-sector, U(1), gamma-generator
  | Neutron : NucleonMode   -- χ₋, C-sector, SU(3), eta-generator
  deriving DecidableEq, Repr
```
