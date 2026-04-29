---
{
  "projection_kind": "taulib_declaration",
  "title": "DeuteronBinding",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/deuteron-binding/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::DeuteronBinding",
  "declaration_slug": "deuteron-binding",
  "kind": "structure",
  "name": "DeuteronBinding",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 231,
  "source_line_end": 238,
  "registry_ids": [
    "IV.R133"
  ],
  "related_registry_items": [
    {
      "id": "IV.R133",
      "title": "Deuteron binding in tau-language",
      "url": "/registry/object/IV.R133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L231-L238",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L231-L238",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L231-L238)
- Source range: L231-L238
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R133` — Deuteron binding in tau-language

## Immediate Comment / Docstring

```lean
/-- [IV.R133] The deuteron is the minimal two-nucleon winding
    configuration on T². Binding energy B_d ≈ 2.224 MeV from
    η-holonomy field overlap. -/
```

## Source Excerpt

```lean
structure DeuteronBinding where
  /-- Number of nucleons. -/
  nucleon_count : Nat := 2
  /-- Binding energy (keV). -/
  binding_keV : Nat := 2224
  /-- Minimal configuration. -/
  minimal : Bool := true
  deriving Repr
```
