---
{
  "projection_kind": "taulib_declaration",
  "title": "kepler_first_law",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-first-law/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::kepler_first_law",
  "declaration_slug": "kepler-first-law",
  "kind": "theorem",
  "name": "kepler_first_law",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 121,
  "source_line_end": 123,
  "registry_ids": [
    "V.T81"
  ],
  "related_registry_items": [
    {
      "id": "V.T81",
      "title": "Rotational Flux Conservation --- V.T33",
      "url": "/registry/object/V.T81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L121-L123",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
        "url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L121-L123",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.Astrophysics.KeplerSolarSystem](/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/)
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L121-L123)
- Source range: L121-L123
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T81` — Rotational Flux Conservation --- V.T33

## Immediate Comment / Docstring

```lean
/-- [V.T81] Kepler first law: orbits are conic sections.
    This follows from the 1/r form of the D-sector coupling
    readout in the Newtonian regime. -/
```

## Source Excerpt

```lean
theorem kepler_first_law (k : KeplerOrbitData)
    (hb : k.orbit_type = .Elliptical) :
    k.orbit_type = .Elliptical := hb
```
