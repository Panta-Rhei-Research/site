---
{
  "projection_kind": "taulib_declaration",
  "title": "transitionRadius",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/transition-radius/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::transitionRadius",
  "declaration_slug": "transition-radius",
  "kind": "def",
  "name": "transitionRadius",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 842,
  "source_line_end": 844,
  "registry_ids": [
    "V.D268"
  ],
  "related_registry_items": [
    {
      "id": "V.D268",
      "title": "Transition Radius",
      "url": "/registry/object/V.D268/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L842-L844",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L842-L844",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L842-L844)
- Source range: L842-L844
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D268` — Transition Radius

## Immediate Comment / Docstring

```lean
/-- [V.D268] Transition Radius.

    r_tr = √(GM/a₀), where g_N = a₀ (base = fiber equal).
    NGC 3198: r_tr ≈ 4.2 kpc ≈ 1.6 R_d.
    DDO 154: r_tr ≈ 0.25 kpc << R_d (entirely fiber-dominated). -/
```

## Source Excerpt

```lean
def transitionRadius : String :=
  "r_tr = sqrt(GM/a_0). NGC 3198: 4.2 kpc = 1.6 R_d. " ++
  "DDO 154: 0.25 kpc << R_d."
```
