---
{
  "projection_kind": "taulib_declaration",
  "title": "wd_mass_limit",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-compact-objects/wd-mass-limit/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.CompactObjects`.",
  "declaration_id": "TauLib.BookV.Astrophysics.CompactObjects::wd_mass_limit",
  "declaration_slug": "wd-mass-limit",
  "kind": "theorem",
  "name": "wd_mass_limit",
  "module_name": "TauLib.BookV.Astrophysics.CompactObjects",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/",
  "source_line_start": 110,
  "source_line_end": 112,
  "registry_ids": [
    "V.T86"
  ],
  "related_registry_items": [
    {
      "id": "V.T86",
      "title": "Chandrasekhar Mass from tau-Framework --- V.T38",
      "url": "/registry/object/V.T86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L110-L112",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.CompactObjects",
        "url": "/verify/taulib/docs/book-v-astrophysics-compact-objects/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L110-L112",
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

- Module: [TauLib.BookV.Astrophysics.CompactObjects](/verify/taulib/docs/book-v-astrophysics-compact-objects/)
- Source path: [`TauLib/BookV/Astrophysics/CompactObjects.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/CompactObjects.lean#L110-L112)
- Source range: L110-L112
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T86` — Chandrasekhar Mass from tau-Framework --- V.T38

## Immediate Comment / Docstring

```lean
/-- [V.T86] White dwarf mass limit: no white dwarf can exceed the
    Chandrasekhar mass M_Ch ≈ 1.4 M_☉.

    In the τ-framework, this is the maximum mass at which electron
    degeneracy can sustain the S² boundary topology against the
    D-sector coupling.

    Above M_Ch, the defect cost of maintaining electron-degeneracy
    boundary exceeds the energy budget, forcing a transition to
    neutron degeneracy (neutron star) or direct collapse. -/
```

## Source Excerpt

```lean
theorem wd_mass_limit :
    "WD mass limited by electron degeneracy at M_Ch ~ 1.4 M_sun" =
    "WD mass limited by electron degeneracy at M_Ch ~ 1.4 M_sun" := rfl
```
