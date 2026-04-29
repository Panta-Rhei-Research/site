---
{
  "projection_kind": "taulib_declaration",
  "title": "metricVsCapacitySource",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/metric-vs-capacity-source/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::metricVsCapacitySource",
  "declaration_slug": "metric-vs-capacity-source",
  "kind": "def",
  "name": "metricVsCapacitySource",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 671,
  "source_line_end": 674,
  "registry_ids": [
    "V.D263"
  ],
  "related_registry_items": [
    {
      "id": "V.D263",
      "title": "Metric vs Capacity Source Distinction",
      "url": "/registry/object/V.D263/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L671-L674",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L671-L674",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L671-L674)
- Source range: L671-L674
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D263` — Metric vs Capacity Source Distinction

## Immediate Comment / Docstring

```lean
/-- [V.D263] Metric vs Capacity Source Distinction.

    CAPACITY-SOURCED (linearized PDE):
      u ~ GM/(c²r) · f(r/ℓ_τ)
      → v² = −(c²r/2)u′ ~ GM/r  (Keplerian, c cancels)

    METRIC-SOURCED (full τ-Einstein via a₀):
      a₀ = c²/(2ℓ_τ)  (universal, mass-independent)
      → v⁴ = GM · a₀ = GMc²/(2ℓ_τ)  (flat, c² survives)

    The capacity equation gives the SHAPE (K₀ → logarithmic → flat).
    The metric coupling a₀ gives the AMPLITUDE (correct v). -/
```

## Source Excerpt

```lean
def metricVsCapacitySource : String :=
  "Capacity-sourced: u~GM/(c^2*r) -> v^2~GM/r (Keplerian). " ++
  "Metric-sourced: a_0=c^2/(2*ell) -> v^4=GM*a_0 (flat). " ++
  "Shape from capacity, amplitude from metric."
```
