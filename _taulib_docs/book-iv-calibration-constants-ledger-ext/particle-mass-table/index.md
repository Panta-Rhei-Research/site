---
{
  "projection_kind": "taulib_declaration",
  "title": "ParticleMassTable",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/particle-mass-table/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.ConstantsLedgerExt`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedgerExt::ParticleMassTable",
  "declaration_slug": "particle-mass-table",
  "kind": "structure",
  "name": "ParticleMassTable",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/",
  "source_line_start": 88,
  "source_line_end": 96,
  "registry_ids": [
    "IV.D307"
  ],
  "related_registry_items": [
    {
      "id": "IV.D307",
      "title": "Particle Mass Table",
      "url": "/registry/object/IV.D307/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L88-L96",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.ConstantsLedgerExt",
        "url": "/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L88-L96",
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

- Module: [TauLib.BookIV.Calibration.ConstantsLedgerExt](/verify/taulib/docs/book-iv-calibration-constants-ledger-ext/)
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedgerExt.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedgerExt.lean#L88-L96)
- Source range: L88-L96
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D307` — Particle Mass Table

## Immediate Comment / Docstring

```lean
/-- [IV.D307] Particle mass table: predicted masses as functions
    of ι_τ and m_n, compared to experiment. -/
```

## Source Excerpt

```lean
structure ParticleMassTable where
  /-- Number of mass predictions. -/
  entry_count : Nat
  /-- Entries: m_e, m_p, m_W, m_Z, m_H, m_ν. -/
  entry_eq : entry_count = 6
  /-- Best precision achieved (m_e: 0.025 ppm). -/
  best_ppm_times_1000 : Nat
  best_eq : best_ppm_times_1000 = 25  -- 0.025 ppm × 1000
  deriving Repr
```
