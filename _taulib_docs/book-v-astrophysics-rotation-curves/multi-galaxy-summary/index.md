---
{
  "projection_kind": "taulib_declaration",
  "title": "multiGalaxySummary",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/multi-galaxy-summary/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::multiGalaxySummary",
  "declaration_slug": "multi-galaxy-summary",
  "kind": "def",
  "name": "multiGalaxySummary",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 414,
  "source_line_end": 417,
  "registry_ids": [
    "V.R390"
  ],
  "related_registry_items": [
    {
      "id": "V.R390",
      "title": "Multi-Galaxy Statistical Summary",
      "url": "/registry/object/V.R390/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L414-L417",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L414-L417",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L414-L417)
- Source range: L414-L417
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R390` — Multi-Galaxy Statistical Summary

## Immediate Comment / Docstring

```lean
/-- [V.R390] Multi-Galaxy Statistical Summary.

    V.T85 (Planck): RMS = 0.067 dex — BEST formula, zero free params.
    V.T85 (Local):  RMS = 0.062 dex — slightly better with local H₀.
    V.D232 (Local): RMS = 0.138 dex — systematically too low.

    BTFR slope 3.991 ≈ 4.000: confirms M_b ∝ v⁴ exactly.
    No mass-dependent trend: same formula works for dwarfs and giants.
    Dominant error source: baryonic mass uncertainty (factor 2–3). -/
```

## Source Excerpt

```lean
def multiGalaxySummary : String :=
  "20-galaxy benchmark: V.T85(Planck) RMS=0.067 dex, BTFR slope=3.991, " ++
  "no mass-dependent trend (r=0.21). Zero free parameters. " ++
  "Dominant error: M_b uncertainty (factor 2-3)."
```
