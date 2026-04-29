---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorCoverageSummary",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/sector-coverage-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::SectorCoverageSummary",
  "declaration_slug": "sector-coverage-summary",
  "kind": "structure",
  "name": "SectorCoverageSummary",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 223,
  "source_line_end": 236,
  "registry_ids": [
    "V.D147"
  ],
  "related_registry_items": [
    {
      "id": "V.D147",
      "title": "Readout Artifact",
      "url": "/registry/object/V.D147/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L223-L236",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L223-L236",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L223-L236)
- Source range: L223-L236
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D147` — Readout Artifact

## Immediate Comment / Docstring

```lean
/-- [V.D147] Sector coverage summary: count of phenomena covered
    by each sector. -/
```

## Source Excerpt

```lean
structure SectorCoverageSummary where
  /-- Number of phenomena involving D-sector. -/
  d_count : Nat
  /-- Number involving B-sector. -/
  b_count : Nat
  /-- Number involving C-sector. -/
  c_count : Nat
  /-- Number involving A-sector. -/
  a_count : Nat
  /-- Number involving ω-sector. -/
  omega_count : Nat
  /-- Total phenomena. -/
  total : Nat
  deriving Repr
```
