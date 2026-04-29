---
{
  "projection_kind": "taulib_declaration",
  "title": "FractionalCRSublattice",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/fractional-crsublattice/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::FractionalCRSublattice",
  "declaration_slug": "fractional-crsublattice",
  "kind": "structure",
  "name": "FractionalCRSublattice",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 49,
  "source_line_end": 56,
  "registry_ids": [
    "IV.D158"
  ],
  "related_registry_items": [
    {
      "id": "IV.D158",
      "title": "Fractional CR-sublattice",
      "url": "/registry/object/IV.D158/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L49-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L49-L56",
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L49-L56)
- Source range: L49-L56
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D158` — Fractional CR-sublattice

## Immediate Comment / Docstring

```lean
/-- [IV.D158] The fractional CR-sublattice Lambda_CR^{1/3}:
    {(m, n/3) : m,n in Z} subset Z x (1/3)Z, refining the character
    lattice to accommodate color-charged modes with fractional
    eta-component n/3 not in Z. -/
```

## Source Excerpt

```lean
structure FractionalCRSublattice where
  /-- Lattice description. -/
  lattice : String := "Z x (1/3)Z"
  /-- Refinement factor (denominator of eta-fraction). -/
  refinement_factor : Nat := 3
  /-- Purpose: accommodate color-charged modes. -/
  purpose : String := "fractional eta-holonomy for color-charged modes"
  deriving Repr
```
