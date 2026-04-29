---
{
  "projection_kind": "taulib_declaration",
  "title": "NuclearForce",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/nuclear-force/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::NuclearForce",
  "declaration_slug": "nuclear-force",
  "kind": "structure",
  "name": "NuclearForce",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 213,
  "source_line_end": 220,
  "registry_ids": [
    "IV.D202"
  ],
  "related_registry_items": [
    {
      "id": "IV.D202",
      "title": "Nuclear force",
      "url": "/registry/object/IV.D202/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L213-L220",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L213-L220",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L213-L220)
- Source range: L213-L220
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D202` — Nuclear force

## Immediate Comment / Docstring

```lean
/-- [IV.D202] The nuclear force is the residual C-sector interaction
    from partial overlap of nucleon color fields at ~1 fm.
    Mediated by virtual meson exchange, principally the pion
    (range ≈ ℏ/m_π c ≈ 1.4 fm). -/
```

## Source Excerpt

```lean
structure NuclearForce where
  /-- Range (fm ×10). -/
  range_fm_x10 : Nat := 14
  /-- Mediator. -/
  mediator : String := "pion (primarily)"
  /-- Mechanism. -/
  mechanism : String := "residual C-sector color field overlap"
  deriving Repr
```
