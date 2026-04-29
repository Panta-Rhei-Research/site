---
{
  "projection_kind": "taulib_declaration",
  "title": "vacuum_zero_prediction",
  "permalink": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/vacuum-zero-prediction/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::vacuum_zero_prediction",
  "declaration_slug": "vacuum-zero-prediction",
  "kind": "def",
  "name": "vacuum_zero_prediction",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 186,
  "source_line_end": 191,
  "registry_ids": [
    "V.T139"
  ],
  "related_registry_items": [
    {
      "id": "V.T139",
      "title": "Vacuum energy is exactly zero",
      "url": "/registry/object/V.T139/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L186-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L186-L191",
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
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L186-L191)
- Source range: L186-L191
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T139` — Vacuum energy is exactly zero

## Immediate Comment / Docstring

```lean
/-- [V.T139] Vacuum energy is exactly zero.

    rho_vac^tau = 0 (exact, not fine-tuned).
    Lambda = 0 in the tau-Einstein equation.
    Cosmic acceleration from S_def -> S_ref transition.

    Testable via: w_eff(z) measurement.
    tau predicts w varies with z (not exactly -1).
    If w = -1 exactly at all z, tau's mechanism is refuted. -/
```

## Source Excerpt

```lean
def vacuum_zero_prediction : FalsifiablePrediction where
  name := "Vacuum energy zero"
  prediction := "rho_vac = 0; Lambda = 0; w varies with z"
  falsifier := "w(z) confirmed exactly -1 at all redshifts"
  strength := .Strong
  registry_id := "V.T139"
```
