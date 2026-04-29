---
{
  "projection_kind": "taulib_declaration",
  "title": "GlueballDef",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/glueball-def/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::GlueballDef",
  "declaration_slug": "glueball-def",
  "kind": "structure",
  "name": "GlueballDef",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 120,
  "source_line_end": 129,
  "registry_ids": [
    "IV.D201"
  ],
  "related_registry_items": [
    {
      "id": "IV.D201",
      "title": "Glueball",
      "url": "/registry/object/IV.D201/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L120-L129",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L120-L129",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L120-L129)
- Source range: L120-L129
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D201` — Glueball

## Immediate Comment / Docstring

```lean
/-- [IV.D201] A glueball is a bound state of the strong vacuum field
    Γ_s* with no quark content: a color-neutral excitation of the
    su(3) connection field above the vacuum minimum.

    Predicted by lattice QCD at ~1.5-1.7 GeV for J^PC = 0^++. -/
```

## Source Excerpt

```lean
structure GlueballDef where
  /-- Quark content: none. -/
  quark_content : Nat := 0
  /-- Predicted mass range low (MeV). -/
  mass_low_mev : Nat := 1500
  /-- Predicted mass range high (MeV). -/
  mass_high_mev : Nat := 1700
  /-- Quantum numbers J^PC. -/
  jpc : String := "0++"
  deriving Repr
```
