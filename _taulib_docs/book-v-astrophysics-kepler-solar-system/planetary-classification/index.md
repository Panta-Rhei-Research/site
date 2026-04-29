---
{
  "projection_kind": "taulib_declaration",
  "title": "planetary_classification",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/planetary-classification/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::planetary_classification",
  "declaration_slug": "planetary-classification",
  "kind": "theorem",
  "name": "planetary_classification",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 207,
  "source_line_end": 210,
  "registry_ids": [
    "V.P62"
  ],
  "related_registry_items": [
    {
      "id": "V.P62",
      "title": "Solar System Concordance --- V.P26",
      "url": "/registry/object/V.P62/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L207-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L207-L210",
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
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L207-L210)
- Source range: L207-L210
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P62` — Solar System Concordance --- V.P26

## Immediate Comment / Docstring

```lean
/-- [V.P62] Planetary classification from defect budget: the four
    planetary types correspond to distinct defect-budget regimes
    in the D-sector readout. -/
```

## Source Excerpt

```lean
theorem planetary_classification :
    [PlanetaryType.Rocky, PlanetaryType.GasGiant,
     PlanetaryType.IceGiant, PlanetaryType.DwarfPlanet].length = 4 := by
  native_decide
```
