---
{
  "projection_kind": "taulib_declaration",
  "title": "n_eff_upper_bound",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/n-eff-upper-bound/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::n_eff_upper_bound",
  "declaration_slug": "n-eff-upper-bound",
  "kind": "theorem",
  "name": "n_eff_upper_bound",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 188,
  "source_line_end": 188,
  "registry_ids": [
    "V.P113"
  ],
  "related_registry_items": [
    {
      "id": "V.P113",
      "title": "Dark Sector Closure",
      "url": "/registry/object/V.P113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L188-L188",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L188-L188",
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
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L188-L188)
- Source range: L188-L188
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P113` — Dark Sector Closure

## Immediate Comment / Docstring

```lean
/-- [V.P113] Dark sector closure: the 5 generators of Category τ
    exhaust all available sectors (D, A, B, C, ω). No additional
    generator exists to host a dark sector.

    Consequence: N_eff ≤ 3 is a structural upper bound. Any
    observation of N_eff > 3 would falsify the 5-generator theorem. -/
```

## Source Excerpt

```lean
theorem n_eff_upper_bound : n_gauge_generators ≤ 3 := le_refl 3
```
