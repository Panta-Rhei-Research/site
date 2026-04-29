---
{
  "projection_kind": "taulib_declaration",
  "title": "gemMapping",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/gem-mapping/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::gemMapping",
  "declaration_slug": "gem-mapping",
  "kind": "def",
  "name": "gemMapping",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 940,
  "source_line_end": 942,
  "registry_ids": [
    "V.R393"
  ],
  "related_registry_items": [
    {
      "id": "V.R393",
      "title": "GEM Mapping",
      "url": "/registry/object/V.R393/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L940-L942",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L940-L942",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L940-L942)
- Source range: L940-L942
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R393` — GEM Mapping

## Immediate Comment / Docstring

```lean
/-- [V.R393] GEM Mapping.

    Standard GEM: v_gm = 2GJ/(c²r²), suppressed by (v/c)² ~ 10⁻⁷.
    NGC 3198 at 10 kpc: v_gm ≈ 0.01 m/s vs v_obs ≈ 150 km/s.
    Two-channel fiber is NOT gravitomagnetic but from T² of τ³. -/
```

## Source Excerpt

```lean
def gemMapping : String :=
  "v_gm = 2GJ/(c^2*r^2) ~ 10^-7 * v_obs. " ++
  "Standard GEM negligible. Fiber channel is NOT GEM."
```
