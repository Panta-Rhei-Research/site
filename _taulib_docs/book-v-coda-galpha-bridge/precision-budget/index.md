---
{
  "projection_kind": "taulib_declaration",
  "title": "PrecisionBudget",
  "permalink": "/verify/taulib/docs/book-v-coda-galpha-bridge/precision-budget/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.GAlphaBridge`.",
  "declaration_id": "TauLib.BookV.Coda.GAlphaBridge::PrecisionBudget",
  "declaration_slug": "precision-budget",
  "kind": "structure",
  "name": "PrecisionBudget",
  "module_name": "TauLib.BookV.Coda.GAlphaBridge",
  "module_url": "/verify/taulib/docs/book-v-coda-galpha-bridge/",
  "source_line_start": 192,
  "source_line_end": 205,
  "registry_ids": [
    "V.P116"
  ],
  "related_registry_items": [
    {
      "id": "V.P116",
      "title": "Precision Budget",
      "url": "/registry/object/V.P116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L192-L205",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.GAlphaBridge",
        "url": "/verify/taulib/docs/book-v-coda-galpha-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L192-L205",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Coda.GAlphaBridge](/verify/taulib/docs/book-v-coda-galpha-bridge/)
- Source path: [`TauLib/BookV/Coda/GAlphaBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/GAlphaBridge.lean#L192-L205)
- Source range: L192-L205
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P116` — Precision Budget

## Immediate Comment / Docstring

```lean
/-- [V.P116] Precision budget for G via the bridge.

    - From α: 2.7 ppb (negligible, CODATA precision)
    - From c₁ = 3/π correction: ~3 ppm (dominant uncertainty)
    - From m_n: 0.6 ppm (mass measurement precision)
    - Total: ~3 ppm (dominated by c₁ theoretical uncertainty) -/
```

## Source Excerpt

```lean
structure PrecisionBudget where
  /-- Number of uncertainty sources. -/
  n_sources : Nat
  /-- Three sources. -/
  sources_eq : n_sources = 3
  /-- Dominant source is c₁. -/
  dominant_is_c1 : Bool := true
  /-- α contribution negligible. -/
  alpha_negligible : Bool := true
  /-- α precision (ppb). -/
  alpha_ppb : Nat := 3
  /-- c₁ precision (ppm). -/
  c1_ppm : Nat := 3
  deriving Repr
```
