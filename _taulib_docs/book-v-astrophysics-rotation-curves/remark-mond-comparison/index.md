---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_mond_comparison",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/remark-mond-comparison/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::remark_mond_comparison",
  "declaration_slug": "remark-mond-comparison",
  "kind": "def",
  "name": "remark_mond_comparison",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 281,
  "source_line_end": 286,
  "registry_ids": [
    "V.R371"
  ],
  "related_registry_items": [
    {
      "id": "V.R371",
      "title": "MOND Comparison Table",
      "url": "/registry/object/V.R371/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L281-L286",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L281-L286",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L281-L286)
- Source range: L281-L286
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R371` — MOND Comparison Table

## Immediate Comment / Docstring

```lean
/-- [V.R371] MOND comparison: τ surpasses on 4 structural dimensions. -/
```

## Source Excerpt

```lean
def remark_mond_comparison : String :=
  "tau surpasses MOND: " ++
  "(1) no free interpolation function (capacity equation determines transition), " ++
  "(2) a_0 from first principles V.D232 at 0.9%, " ++
  "(3) BTFR normalization A from iota_tau and H_0 only, " ++
  "(4) RAR from single sector coupling kappa(D;1) = 1 - iota_tau."
```
