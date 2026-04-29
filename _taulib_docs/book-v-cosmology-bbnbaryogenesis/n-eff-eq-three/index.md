---
{
  "projection_kind": "taulib_declaration",
  "title": "n_eff_eq_three",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-eq-three/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::n_eff_eq_three",
  "declaration_slug": "n-eff-eq-three",
  "kind": "theorem",
  "name": "n_eff_eq_three",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 176,
  "source_line_end": 176,
  "registry_ids": [
    "V.T151"
  ],
  "related_registry_items": [
    {
      "id": "V.T151",
      "title": "N_eff from Sector Exhaustion",
      "url": "/registry/object/V.T151/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L176-L176",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L176-L176",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L176-L176)
- Source range: L176-L176
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T151` — N_eff from Sector Exhaustion

## Immediate Comment / Docstring

```lean
/-- [V.T151] N_eff from sector exhaustion: the effective number of
    neutrino species equals the number of non-gravitational generators.

    N_eff = |{π, γ, η}| = 3. -/
```

## Source Excerpt

```lean
theorem n_eff_eq_three : n_gauge_generators = 3 := rfl
```
