---
{
  "projection_kind": "taulib_declaration",
  "title": "no_singularity_prediction",
  "permalink": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/no-singularity-prediction/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::no_singularity_prediction",
  "declaration_slug": "no-singularity-prediction",
  "kind": "def",
  "name": "no_singularity_prediction",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 115,
  "source_line_end": 120,
  "registry_ids": [
    "V.T136"
  ],
  "related_registry_items": [
    {
      "id": "V.T136",
      "title": "No singularities in tau",
      "url": "/registry/object/V.T136/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L115-L120",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.FalsifiableSeams",
        "url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L115-L120",
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

- Module: [TauLib.BookV.Orthodox.FalsifiableSeams](/verify/taulib/docs/book-v-orthodox-falsifiable-seams/)
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L115-L120)
- Source range: L115-L120
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T136` — No singularities in tau

## Immediate Comment / Docstring

```lean
/-- [V.T136] No singularities in tau: the tau-Einstein equation
    admits no singular solutions.

    kappa_tau = 1 - iota_tau is finite and nonzero at every depth.
    The profinite tower ensures all boundary characters are bounded.
    Singular solutions of GR are chart artifacts.

    Testable via: gravitational wave echoes, post-merger ringdown
    anomalies, future BH interior probes. -/
```

## Source Excerpt

```lean
def no_singularity_prediction : FalsifiablePrediction where
  name := "No singularities"
  prediction := "BH interiors have finite curvature"
  falsifier := "Detection of a physical singularity signal"
  strength := .Medium
  registry_id := "V.T136"
```
