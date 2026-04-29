---
{
  "projection_kind": "taulib_declaration",
  "title": "nlo_factor_65_numer",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/nlo-factor-65-numer/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::nlo_factor_65_numer",
  "declaration_slug": "nlo-factor-65-numer",
  "kind": "theorem",
  "name": "nlo_factor_65_numer",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 284,
  "source_line_end": 284,
  "registry_ids": [
    "IV.P184"
  ],
  "related_registry_items": [
    {
      "id": "IV.P184",
      "title": "NLO Color-Generator Correction 6/5",
      "url": "/registry/object/IV.P184/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L284-L284",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L284-L284",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L284-L284)
- Source range: L284-L284
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P184` — NLO Color-Generator Correction 6/5

## Immediate Comment / Docstring

```lean
/-- [IV.P184] NLO factor 6/5: numerator factorization.
    6 = 2 × 3 = N_ell (lemniscate lobes) × N_c (quark colors). -/
```

## Source Excerpt

```lean
theorem nlo_factor_65_numer : (6 : Nat) = 2 * 3 := by omega
```
