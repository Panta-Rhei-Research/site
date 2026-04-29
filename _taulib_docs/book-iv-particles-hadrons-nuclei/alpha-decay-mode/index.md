---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_decay_mode",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/alpha-decay-mode/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::alpha_decay_mode",
  "declaration_slug": "alpha-decay-mode",
  "kind": "def",
  "name": "alpha_decay_mode",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 346,
  "source_line_end": 347,
  "registry_ids": [
    "IV.R137"
  ],
  "related_registry_items": [
    {
      "id": "IV.R137",
      "title": "Alpha-decay as mode cluster ejection",
      "url": "/registry/object/IV.R137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L346-L347",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L346-L347",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L346-L347)
- Source range: L346-L347
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R137` — Alpha-decay as mode cluster ejection

## Immediate Comment / Docstring

```lean
/-- [IV.R137] Alpha-decay: ejection of a completely filled lowest-winding-mode
    cluster (4 nucleons) from the parent nucleus, tunneling through the
    Coulomb barrier. -/
```

## Source Excerpt

```lean
def alpha_decay_mode : String :=
  "Alpha-decay: 4-nucleon cluster ejection, lowest winding mode, Coulomb tunneling"
```
