---
{
  "projection_kind": "taulib_declaration",
  "title": "kepler_third_law",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/kepler-third-law/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.KeplerSolarSystem`.",
  "declaration_id": "TauLib.BookV.Astrophysics.KeplerSolarSystem::kepler_third_law",
  "declaration_slug": "kepler-third-law",
  "kind": "theorem",
  "name": "kepler_third_law",
  "module_name": "TauLib.BookV.Astrophysics.KeplerSolarSystem",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-kepler-solar-system/",
  "source_line_start": 135,
  "source_line_end": 137,
  "registry_ids": [
    "V.T83"
  ],
  "related_registry_items": [
    {
      "id": "V.T83",
      "title": "Kepler's Second Law --- V.T35",
      "url": "/registry/object/V.T83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L135-L137",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L135-L137",
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
- Source path: [`TauLib/BookV/Astrophysics/KeplerSolarSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/KeplerSolarSystem.lean#L135-L137)
- Source range: L135-L137
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T83` — Kepler's Second Law --- V.T35

## Immediate Comment / Docstring

```lean
/-- [V.T83] Kepler third law: T^2 proportional to a^3.
    This follows from the specific form of the D-sector coupling
    κ(D;1) = 1−ι_τ in the Newtonian readout. -/
```

## Source Excerpt

```lean
theorem kepler_third_law :
    "T^2 / a^3 = 4pi^2 / (G*M) = readout of D-sector coupling" =
    "T^2 / a^3 = 4pi^2 / (G*M) = readout of D-sector coupling" := rfl
```
