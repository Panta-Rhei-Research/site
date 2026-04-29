---
{
  "projection_kind": "taulib_declaration",
  "title": "juno_dune_predictions",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/juno-dune-predictions/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::juno_dune_predictions",
  "declaration_slug": "juno-dune-predictions",
  "kind": "def",
  "name": "juno_dune_predictions",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 237,
  "source_line_end": 240,
  "registry_ids": [
    "V.P188"
  ],
  "related_registry_items": [
    {
      "id": "V.P188",
      "title": "JUNO/DUNE Cross-Check Predictions",
      "url": "/registry/object/V.P188/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L237-L240",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L237-L240",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L237-L240)
- Source range: L237-L240
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.P188` — JUNO/DUNE Cross-Check Predictions

## Immediate Comment / Docstring

```lean
/-- [V.P188] JUNO/DUNE predictions: solar splitting at sub-1%, atmospheric at sub-2%.
    Current τ values testable by both experiments. -/
```

## Source Excerpt

```lean
def juno_dune_predictions : String :=
  "JUNO: Δm²₂₁ at sub-1% → current 6.2× overshoot ruled out if NuFIT confirmed. " ++
  "DUNE: |Δm²₃₂| at sub-2% → +22.9% overshoot testable. " ++
  "Σm_ν = 0.089 eV (cosmological) independent of individual mass refinement."
```
