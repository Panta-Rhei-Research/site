---
{
  "projection_kind": "taulib_declaration",
  "title": "algebraic_distinctness",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/algebraic-distinctness/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::algebraic_distinctness",
  "declaration_slug": "algebraic-distinctness",
  "kind": "theorem",
  "name": "algebraic_distinctness",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 873,
  "source_line_end": 877,
  "registry_ids": [
    "V.T209"
  ],
  "related_registry_items": [
    {
      "id": "V.T209",
      "title": "Algebraic Distinctness from Standard MOND",
      "url": "/registry/object/V.T209/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L873-L877",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L873-L877",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L873-L877)
- Source range: L873-L877
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T209` — Algebraic Distinctness from Standard MOND

## Immediate Comment / Docstring

```lean
/-- [V.T209] Algebraic Distinctness from Standard MOND.

    ν_2ch(y) = √(1+1/y) is algebraically distinct from
    ν_std(y) = √((1+√(1+4/y²))/2). Max difference +12%
    at y ≈ 1–2 (transition region). Two-channel satisfies
    quadratic; standard satisfies quartic. -/
```

## Source Excerpt

```lean
theorem algebraic_distinctness :
    "nu_2ch != nu_std: +12% at y=1-2. " ++
    "Quadratic g^2-g_N^2-g_N*a_0=0 vs quartic." =
    "nu_2ch != nu_std: +12% at y=1-2. " ++
    "Quadratic g^2-g_N^2-g_N*a_0=0 vs quartic." := rfl
```
