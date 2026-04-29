---
{
  "projection_kind": "taulib_declaration",
  "title": "mond_scale_from_iota",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/mond-scale-from-iota/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::mond_scale_from_iota",
  "declaration_slug": "mond-scale-from-iota",
  "kind": "theorem",
  "name": "mond_scale_from_iota",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 134,
  "source_line_end": 136,
  "registry_ids": [
    "V.C13"
  ],
  "related_registry_items": [
    {
      "id": "V.C13",
      "title": "Baryonic Tully--Fisher from Capacity --- V.R20",
      "url": "/registry/object/V.C13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L134-L136",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L134-L136",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L134-L136)
- Source range: L134-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C13` — Baryonic Tully--Fisher from Capacity --- V.R20

## Immediate Comment / Docstring

```lean
/-- [V.C13] MOND acceleration scale from ι_τ: a₀ is not a free
    parameter but derives from the τ-master constant.

    a₀ ~ c · H₀ · f(ι_τ)

    where f(ι_τ) is a function of the master constant that connects
    the galactic acceleration scale to cosmological parameters.

    The numerical coincidence a₀ ≈ cH₀/6 is structural in
    the τ-framework. -/
```

## Source Excerpt

```lean
theorem mond_scale_from_iota :
    "a0 derives from iota_tau via a0 ~ c*H0*f(iota_tau), not a free parameter" =
    "a0 derives from iota_tau via a0 ~ c*H0*f(iota_tau), not a free parameter" := rfl
```
