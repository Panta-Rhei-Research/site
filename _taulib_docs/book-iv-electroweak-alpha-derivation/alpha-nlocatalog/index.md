---
{
  "projection_kind": "taulib_declaration",
  "title": "AlphaNLOCatalog",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/alpha-nlocatalog/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::AlphaNLOCatalog",
  "declaration_slug": "alpha-nlocatalog",
  "kind": "structure",
  "name": "AlphaNLOCatalog",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 455,
  "source_line_end": 464,
  "registry_ids": [
    "IV.D385"
  ],
  "related_registry_items": [
    {
      "id": "IV.D385",
      "title": "α NLO Correction Candidate Catalog",
      "url": "/registry/object/IV.D385/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L455-L464",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L455-L464",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L455-L464)
- Source range: L455-L464
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D385` — α NLO Correction Candidate Catalog

## Immediate Comment / Docstring

```lean
/-- [IV.D385] α NLO Correction Candidate Catalog.
    Four candidates, none improves 9.8 ppm:
    A: +ι_τ⁶/(5·2) = +158 ppm (wrong direction)
    B: +ι_τ⁴/25 = +543 ppm (wrong direction)
    C: −ι_τ²/50 = −2330 ppm (too large)
    D: +ι_τ²/18 = +6470 ppm (too large)
    All overshoot or wrong sign vs the +9.8 ppm residual. -/
```

## Source Excerpt

```lean
structure AlphaNLOCatalog where
  /-- Number of candidates assessed. -/
  n_candidates : Nat := 4
  /-- Current precision in ppm (LO tower formula). -/
  current_ppm : Nat := 10  -- rounded from 9.8
  /-- Smallest candidate shift magnitude in ppm. -/
  smallest_shift : Nat := 158  -- candidate A
  /-- All candidates overshoot. -/
  all_overshoot : Bool := true
  deriving Repr
```
