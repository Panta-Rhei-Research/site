---
{
  "projection_kind": "taulib_declaration",
  "title": "AtomDef",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/atom-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::AtomDef",
  "declaration_slug": "atom-def",
  "kind": "structure",
  "name": "AtomDef",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 59,
  "source_line_end": 70,
  "registry_ids": [
    "IV.D203"
  ],
  "related_registry_items": [
    {
      "id": "IV.D203",
      "title": "Atom as dressed nuclear mode",
      "url": "/registry/object/IV.D203/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L59-L70",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/verify/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L59-L70",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/verify/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L59-L70)
- Source range: L59-L70
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D203` — Atom as dressed nuclear mode

## Immediate Comment / Docstring

```lean
/-- [IV.D203] An atom of atomic number Z is a stable composite of:
    1. Nuclear core: Z protons + N neutrons (bound by C-sector)
    2. Electron shell: Z electrons on T² (bound by B-sector EM)

    A neutral atom has vanishing net B-sector winding:
    electromagnetically closed. -/
```

## Source Excerpt

```lean
structure AtomDef where
  /-- Atomic number Z. -/
  z : Nat
  /-- Neutron number N. -/
  n : Nat
  /-- Number of shell electrons in neutral atom. -/
  electrons : Nat
  /-- Neutral: electrons = Z. -/
  neutral : electrons = z
  /-- Electromagnetically closed. -/
  em_closed : Bool := true
  deriving Repr
```
