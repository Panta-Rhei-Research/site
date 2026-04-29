---
{
  "projection_kind": "taulib_declaration",
  "title": "contraction_is_kappa_D",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/contraction-is-kappa-d/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::contraction_is_kappa_D",
  "declaration_slug": "contraction-is-kappa-d",
  "kind": "theorem",
  "name": "contraction_is_kappa_D",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 301,
  "source_line_end": 302,
  "registry_ids": [
    "V.R113",
    "V.R114",
    "V.R115",
    "V.R116"
  ],
  "related_registry_items": [
    {
      "id": "V.R113",
      "title": "Compatibility with Book~IV",
      "url": "/registry/object/V.R113/"
    },
    {
      "id": "V.R114",
      "title": "Not the same as thermal equilibrium",
      "url": "/registry/object/V.R114/"
    },
    {
      "id": "V.R115",
      "title": "The role of gravity in ordering",
      "url": "/registry/object/V.R115/"
    },
    {
      "id": "V.R116",
      "title": "The contraction rate is the gravitational coupling",
      "url": "/registry/object/V.R116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L301-L302",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L301-L302",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L301-L302)
- Source range: L301-L302
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R113` — Compatibility with Book~IV
- `V.R114` — Not the same as thermal equilibrium
- `V.R115` — The role of gravity in ordering
- `V.R116` — The contraction rate is the gravitational coupling

## Immediate Comment / Docstring

```lean
-- [V.R113] Compatibility with Book IV: total entropy dS/d(alpha-orbit) >= 0
-- because S_ref increases faster than S_def decreases.

-- [V.R114] Not the Same as Thermal Equilibrium: categorical equilibrium
-- (zero defect, minimal disorder) differs from classical (maximal disorder).

-- [V.R115] The Role of Gravity in Ordering: gravity is the primary ordering
-- mechanism; defect absorption rate is controlled by kappa(D;1) = 1 - iota_tau.

-- [V.R116] The contraction rate IS the gravitational coupling:
```

## Source Excerpt

```lean
theorem contraction_is_kappa_D :
    contraction_numer = iota_tau_denom - iota_tau_numer := rfl
```
