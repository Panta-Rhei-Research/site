---
{
  "projection_kind": "taulib_declaration",
  "title": "IronPeak",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/iron-peak/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::IronPeak",
  "declaration_slug": "iron-peak",
  "kind": "structure",
  "name": "IronPeak",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 314,
  "source_line_end": 323,
  "registry_ids": [
    "IV.P131"
  ],
  "related_registry_items": [
    {
      "id": "IV.P131",
      "title": "Iron peak from competing sectors",
      "url": "/registry/object/IV.P131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L314-L323",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L314-L323",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L314-L323)
- Source range: L314-L323
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P131` — Iron peak from competing sectors

## Immediate Comment / Docstring

```lean
/-- [IV.P131] The binding energy maximum at A ≈ 56 (iron peak) results
    from optimal balance between:
    - C-sector (strong) binding per nucleon (saturating)
    - B-sector (EM) repulsion per nucleon (growing as Z²/A^(1/3))

    Crossover near iron-56 where Coulomb cost exceeds marginal binding. -/
```

## Source Excerpt

```lean
structure IronPeak where
  /-- Peak mass number. -/
  peak_A : Nat := 56
  /-- Binding sector. -/
  binding_sector : Sector := .C
  /-- Repulsion sector. -/
  repulsion_sector : Sector := .B
  /-- B/A at peak (MeV ×100). -/
  ba_peak_mev_x100 : Nat := 879
  deriving Repr
```
