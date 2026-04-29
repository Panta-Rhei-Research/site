---
{
  "projection_kind": "taulib_declaration",
  "title": "bestFitExponents",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/best-fit-exponents/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::bestFitExponents",
  "declaration_slug": "best-fit-exponents",
  "kind": "def",
  "name": "bestFitExponents",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 392,
  "source_line_end": 396,
  "registry_ids": [
    "IV.D343"
  ],
  "related_registry_items": [
    {
      "id": "IV.D343",
      "title": "Neutrino Exponent Best-Fit",
      "url": "/registry/object/IV.D343/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L392-L396",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L392-L396",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L392-L396)
- Source range: L392-L396
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D343` — Neutrino Exponent Best-Fit

## Immediate Comment / Docstring

```lean
/-- [IV.D343] Best-fit exponent summary with shape analysis.
    Scale invariance: R(p+n, q+n, r+n) = R(p, q, r) for all n.
    Best integer shape: (p, p+1, p-1) → ratio 39.45 (21.1% from PDG).
    Sprint 3: Δpq = 1.1 ≈ 14/13, Δpr = 0.9 ≈ 12/13 (CF correction). -/
```

## Source Excerpt

```lean
def bestFitExponents : SigmaPolarityMatrix × String :=
  (sprint3_best_fit,
   "Sprint 3: (3.7, 4.8, 2.8) → ratio 32.82 (PDG 32.58, 0.75%). " ++
   "Best integer (p,p+1,p-1) gives 39.45 (21.1%). " ++
   "CF-derived: Δpq = 14/13, Δpr = 12/13.")
```
