---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_h0_tension",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/remark-h0-tension/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::remark_h0_tension",
  "declaration_slug": "remark-h0-tension",
  "kind": "def",
  "name": "remark_h0_tension",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 275,
  "source_line_end": 278,
  "registry_ids": [
    "V.R370"
  ],
  "related_registry_items": [
    {
      "id": "V.R370",
      "title": "H_0 Tension as Galactic Scale Effect",
      "url": "/registry/object/V.R370/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L275-L278",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L275-L278",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L275-L278)
- Source range: L275-L278
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R370` — H_0 Tension as Galactic Scale Effect

## Immediate Comment / Docstring

```lean
/-- [V.R370] H₀ tension remark: structural connection to galactic dynamics. -/
```

## Source Excerpt

```lean
def remark_h0_tension : String :=
  "H_0 tension (local 73 vs CMB 67.4 km/s/Mpc, 6.8 sigma) propagates to a_0 = c*H_0*iota/2. " ++
  "Galaxies probe local H_0; CMB probes Hubble-flow H_0. " ++
  "Falsifiable: BTFR normalization A must shift as H_0 tension resolves."
```
