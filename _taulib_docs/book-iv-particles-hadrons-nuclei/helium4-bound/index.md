---
{
  "projection_kind": "taulib_declaration",
  "title": "Helium4Bound",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/helium4-bound/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::Helium4Bound",
  "declaration_slug": "helium4-bound",
  "kind": "structure",
  "name": "Helium4Bound",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 286,
  "source_line_end": 297,
  "registry_ids": [
    "IV.R135"
  ],
  "related_registry_items": [
    {
      "id": "IV.R135",
      "title": "Why He-4 is tightly bound",
      "url": "/registry/object/IV.R135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L286-L297",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L286-L297",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L286-L297)
- Source range: L286-L297
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R135` — Why He-4 is tightly bound

## Immediate Comment / Docstring

```lean
/-- [IV.R135] He-4 (Z=N=2) is the first doubly magic nucleus.
    B/A ≈ 7.1 MeV, preferred alpha-decay product.
    Completely fills lowest winding mode (0,0) with all four slots. -/
```

## Source Excerpt

```lean
structure Helium4Bound where
  /-- Atomic number Z. -/
  z : Nat := 2
  /-- Neutron number N. -/
  n : Nat := 2
  /-- Binding per nucleon (MeV ×10). -/
  ba_mev_x10 : Nat := 71
  /-- Doubly magic. -/
  doubly_magic : Bool := true
  /-- Number of nucleon slots filled. -/
  slots_filled : Nat := 4
  deriving Repr
```
