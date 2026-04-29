---
{
  "projection_kind": "taulib_declaration",
  "title": "CodonErrorCorrection",
  "permalink": "/verify/taulib/docs/book-vi-source-genetic-code/codon-error-correction/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.GeneticCode`.",
  "declaration_id": "TauLib.BookVI.Source.GeneticCode::CodonErrorCorrection",
  "declaration_slug": "codon-error-correction",
  "kind": "structure",
  "name": "CodonErrorCorrection",
  "module_name": "TauLib.BookVI.Source.GeneticCode",
  "module_url": "/verify/taulib/docs/book-vi-source-genetic-code/",
  "source_line_start": 77,
  "source_line_end": 88,
  "registry_ids": [
    "VI.T22"
  ],
  "related_registry_items": [
    {
      "id": "VI.T22",
      "title": "Codon Degeneracy as Error Correction",
      "url": "/registry/object/VI.T22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L77-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.GeneticCode",
        "url": "/verify/taulib/docs/book-vi-source-genetic-code/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L77-L88",
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

- Module: [TauLib.BookVI.Source.GeneticCode](/verify/taulib/docs/book-vi-source-genetic-code/)
- Source path: [`TauLib/BookVI/Source/GeneticCode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/GeneticCode.lean#L77-L88)
- Source range: L77-L88
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T22` — Codon Degeneracy as Error Correction

## Immediate Comment / Docstring

```lean
/-- [VI.T22] Codon Degeneracy as Error Correction Theorem.
    Standard code in top 0.01% for error minimization (Freeland-Hurst).
    Redundancy: 1.68 bits/codon (log₂(64/20) ≈ 1.68).
    Established result from information theory + computational biology. -/
```

## Source Excerpt

```lean
structure CodonErrorCorrection where
  /-- Percentile rank for error minimization. -/
  percentile_rank_x100 : Nat
  /-- Top 0.01% → 9999 out of 10000. -/
  rank_eq : percentile_rank_x100 = 9999
  /-- Redundancy in bits/codon (×100 for integer). -/
  redundancy_x100 : Nat
  /-- 1.68 bits → 168. -/
  redundancy_eq : redundancy_x100 = 168
  /-- Scope: established (Shannon + Freeland-Hurst). -/
  scope : String := "established"
  deriving Repr
```
