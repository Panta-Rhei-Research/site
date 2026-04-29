---
{
  "projection_kind": "taulib_declaration",
  "title": "NuclearShellStructure",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-shell-structure/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::NuclearShellStructure",
  "declaration_slug": "nuclear-shell-structure",
  "kind": "structure",
  "name": "NuclearShellStructure",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 267,
  "source_line_end": 272,
  "registry_ids": [
    "IV.P130"
  ],
  "related_registry_items": [
    {
      "id": "IV.P130",
      "title": "Nuclear shell structure",
      "url": "/registry/object/IV.P130/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L267-L272",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.HadronsNuclei",
        "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L267-L272",
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

- Module: [TauLib.BookIV.Particles.HadronsNuclei](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/)
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L267-L272)
- Source range: L267-L272
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P130` — Nuclear shell structure

## Immediate Comment / Docstring

```lean
/-- [IV.P130] T²-winding modes for nucleons organize into shells.
    Cumulative counts at shell closures produce the magic numbers:
    2, 8, 20, 28, 50, 82, 126. -/
```

## Source Excerpt

```lean
structure NuclearShellStructure where
  /-- Magic numbers. -/
  magic_numbers : List Nat := [2, 8, 20, 28, 50, 82, 126]
  /-- Origin: T²-winding shell closures. -/
  origin : String := "T^2 winding mode shells"
  deriving Repr
```
