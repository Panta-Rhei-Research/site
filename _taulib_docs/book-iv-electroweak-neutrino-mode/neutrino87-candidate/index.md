---
{
  "projection_kind": "taulib_declaration",
  "title": "Neutrino87Candidate",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino87-candidate/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::Neutrino87Candidate",
  "declaration_slug": "neutrino87-candidate",
  "kind": "structure",
  "name": "Neutrino87Candidate",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 701,
  "source_line_end": 712,
  "registry_ids": [
    "V.T177"
  ],
  "related_registry_items": [
    {
      "id": "V.T177",
      "title": "(8/7, 6/7) Candidate: Neutrino Mass Ratio from Lemniscate n=7",
      "url": "/registry/object/V.T177/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L701-L712",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L701-L712",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L701-L712)
- Source range: L701-L712
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T177` — (8/7, 6/7) Candidate: Neutrino Mass Ratio from Lemniscate n=7

## Immediate Comment / Docstring

```lean
/-- [V.T177] (8/7,6/7) gives ratio 30.211 at −72589 ppm from PDG 32.576.
    4/3 ratio exact from lemniscate counting: (2×lobes)/sectors = 4/3.
    Grid (1.16,0.87) gives +18.5 ppm (τ-effective, V.T175). -/
```

## Source Excerpt

```lean
structure Neutrino87Candidate where
  /-- Numerator of Δpq fraction: 8/7. -/
  numerator : Nat := 8
  /-- Denominator shared by both fractions: n=7. -/
  denominator : Nat := 7
  /-- Δpr numerator: 6/7. -/
  numerator_pr : Nat := 6
  /-- Ratio Δpq/Δpr = 4/3 exactly. -/
  ratio_exact_43 : Bool := true
  /-- Span = |lobes| = 2. -/
  span_eq_lobes : Bool := true
  deriving Repr
```
