---
{
  "projection_kind": "taulib_declaration",
  "title": "no_dark_prediction",
  "permalink": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/no-dark-prediction/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.FalsifiableSeams`.",
  "declaration_id": "TauLib.BookV.Orthodox.FalsifiableSeams::no_dark_prediction",
  "declaration_slug": "no-dark-prediction",
  "kind": "def",
  "name": "no_dark_prediction",
  "module_name": "TauLib.BookV.Orthodox.FalsifiableSeams",
  "module_url": "/verify/taulib/docs/book-v-orthodox-falsifiable-seams/",
  "source_line_start": 161,
  "source_line_end": 166,
  "registry_ids": [
    "V.T138"
  ],
  "related_registry_items": [
    {
      "id": "V.T138",
      "title": "No dark sectors",
      "url": "/registry/object/V.T138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L161-L166",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L161-L166",
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
- Source path: [`TauLib/BookV/Orthodox/FalsifiableSeams.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/FalsifiableSeams.lean#L161-L166)
- Source range: L161-L166
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T138` — No dark sectors

## Immediate Comment / Docstring

```lean
/-- [V.T138] No dark sectors: 5 generators exhaust the budget.

    Dark matter: no sixth sector, no dark particle.
    Dark energy: Lambda = 0, acceleration from defect transition.

    Testable via: direct dark matter detection experiments.
    If a dark matter particle is confirmed, tau is falsified. -/
```

## Source Excerpt

```lean
def no_dark_prediction : FalsifiablePrediction where
  name := "No dark sectors"
  prediction := "No dark matter particle; no dark energy substance"
  falsifier := "Confirmed detection of dark matter particle"
  strength := .Strong
  registry_id := "V.T138"
```
