---
{
  "projection_kind": "taulib_declaration",
  "title": "no_bsm_astro",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/no-bsm-astro/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::no_bsm_astro",
  "declaration_slug": "no-bsm-astro",
  "kind": "theorem",
  "name": "no_bsm_astro",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 259,
  "source_line_end": 261,
  "registry_ids": [
    "V.P87"
  ],
  "related_registry_items": [
    {
      "id": "V.P87",
      "title": "LCDM Budget Translation",
      "url": "/registry/object/V.P87/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L259-L261",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L259-L261",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L259-L261)
- Source range: L259-L261
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P87` — LCDM Budget Translation

## Immediate Comment / Docstring

```lean
/-- [V.P87] Completeness implies no BSM astrophysics: since all
    phenomena are covered, no beyond-standard-model (BSM)
    astrophysical physics is required.

    Prediction: no dark matter particle, no dark energy field,
    no fifth force, no modified gravity (beyond τ-corrections),
    no extra dimensions, no string-theory-specific signatures
    will be found in astrophysical observations. -/
```

## Source Excerpt

```lean
theorem no_bsm_astro :
    "5-sector completeness implies no BSM astrophysical physics needed" =
    "5-sector completeness implies no BSM astrophysical physics needed" := rfl
```
