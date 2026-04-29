---
{
  "projection_kind": "taulib_declaration",
  "title": "IonicBond",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/ionic-bond/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::IonicBond",
  "declaration_slug": "ionic-bond",
  "kind": "structure",
  "name": "IonicBond",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 239,
  "source_line_end": 246,
  "registry_ids": [
    "IV.D206"
  ],
  "related_registry_items": [
    {
      "id": "IV.D206",
      "title": "Ionic bond",
      "url": "/registry/object/IV.D206/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L239-L246",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L239-L246",
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
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L239-L246)
- Source range: L239-L246
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D206` — Ionic bond

## Immediate Comment / Docstring

```lean
/-- [IV.D206] An ionic bond is a complete transfer of electron winding
    modes from atom A to atom B such that both ions achieve noble gas
    closure. Bond energy E_ionic ≈ −k²α/r_AB. -/
```

## Source Excerpt

```lean
structure IonicBond where
  /-- Complete electron transfer. -/
  complete_transfer : Bool := true
  /-- Both ions approach noble gas closure. -/
  both_closed : Bool := true
  /-- Example. -/
  example_compound : String := "NaCl"
  deriving Repr
```
