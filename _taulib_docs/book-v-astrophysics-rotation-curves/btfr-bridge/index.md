---
{
  "projection_kind": "taulib_declaration",
  "title": "btfr_bridge",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/btfr-bridge/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::btfr_bridge",
  "declaration_slug": "btfr-bridge",
  "kind": "def",
  "name": "btfr_bridge",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 343,
  "source_line_end": 345,
  "registry_ids": [
    "V.R389"
  ],
  "related_registry_items": [
    {
      "id": "V.R389",
      "title": "√ι_τ Bridge for BTFR Normalization",
      "url": "/registry/object/V.R389/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L343-L345",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L343-L345",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L343-L345)
- Source range: L343-L345
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R389` — √ι_τ Bridge for BTFR Normalization

## Immediate Comment / Docstring

```lean
/-- [V.R389] √ι_τ Bridge for BTFR normalization.

    A_T85(Planck) = 28.35 M☉/(km/s)⁴ — raw V.T85 normalization
    A_T85/√ι_τ = 48.52 M☉/(km/s)⁴ — bridge normalization
    A_obs = 47 M☉/(km/s)⁴ — observed BTFR (McGaugh+2012)

    Agreement: +3.2% (Planck), geometric mean ≈ 46.6 M☉/(km/s)⁴.
    The √ι_τ factor corrects for the fiber coherence contribution
    to the effective gravitational coupling at galactic scales. -/
```

## Source Excerpt

```lean
def btfr_bridge : String :=
  "A_T85/sqrt(iota) = 48.52 M_sun/(km/s)^4, A_obs = 47. Agreement: +3.2% (Planck). " ++
  "sqrt(iota) = 0.584 bridges bare capacity to observed BTFR normalization."
```
