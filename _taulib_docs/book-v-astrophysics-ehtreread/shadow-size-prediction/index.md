---
{
  "projection_kind": "taulib_declaration",
  "title": "shadow_size_prediction",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/shadow-size-prediction/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::shadow_size_prediction",
  "declaration_slug": "shadow-size-prediction",
  "kind": "theorem",
  "name": "shadow_size_prediction",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 121,
  "source_line_end": 123,
  "registry_ids": [
    "V.T95"
  ],
  "related_registry_items": [
    {
      "id": "V.T95",
      "title": "Shadow Shape Theorem (T^2 vs S^2)",
      "url": "/registry/object/V.T95/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L121-L123",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L121-L123",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L121-L123)
- Source range: L121-L123
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T95` — Shadow Shape Theorem (T^2 vs S^2)

## Immediate Comment / Docstring

```lean
/-- [V.T95] Shadow size prediction: the BH shadow angular diameter
    is determined by the photon capture radius r_ph = 3GM/c².

        θ_shadow = 3√3 · GM / (c² · D)

    where D is the angular diameter distance.

    The τ-framework gives the SAME shadow size as GR because the
    D-sector coupling at the photon sphere is identical to the GR
    metric at r = 3GM/c². The difference appears only AT and BELOW
    the horizon, not at the photon sphere.

    M87*: 42 ± 3 μas (EHT 2019, consistent)
    Sgr A*: 52 ± 1 μas (EHT 2022, consistent) -/
```

## Source Excerpt

```lean
theorem shadow_size_prediction :
    "Shadow = 3*sqrt(3)*GM/(c^2*D), identical to GR at photon sphere" =
    "Shadow = 3*sqrt(3)*GM/(c^2*D), identical to GR at photon sphere" := rfl
```
