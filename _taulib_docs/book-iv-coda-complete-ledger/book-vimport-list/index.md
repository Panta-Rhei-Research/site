---
{
  "projection_kind": "taulib_declaration",
  "title": "BookVImportList",
  "permalink": "/verify/taulib/docs/book-iv-coda-complete-ledger/book-vimport-list/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.CompleteLedger`.",
  "declaration_id": "TauLib.BookIV.Coda.CompleteLedger::BookVImportList",
  "declaration_slug": "book-vimport-list",
  "kind": "structure",
  "name": "BookVImportList",
  "module_name": "TauLib.BookIV.Coda.CompleteLedger",
  "module_url": "/verify/taulib/docs/book-iv-coda-complete-ledger/",
  "source_line_start": 207,
  "source_line_end": 220,
  "registry_ids": [
    "IV.D243"
  ],
  "related_registry_items": [
    {
      "id": "IV.D243",
      "title": "Book V import list",
      "url": "/registry/object/IV.D243/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L207-L220",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.CompleteLedger",
        "url": "/verify/taulib/docs/book-iv-coda-complete-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L207-L220",
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

- Module: [TauLib.BookIV.Coda.CompleteLedger](/verify/taulib/docs/book-iv-coda-complete-ledger/)
- Source path: [`TauLib/BookIV/Coda/CompleteLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/CompleteLedger.lean#L207-L220)
- Source range: L207-L220
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D243` — Book V import list

## Immediate Comment / Docstring

```lean
/-- [IV.D243] Book V Import List: what Book IV exports to Book V.

    Book V receives complete fiber T^2 physics:
    - All 10 coupling constants as rational functions of iota_tau (Lean-verified)
    - The defect functional on T^2 (all 9 regimes classified)
    - Phase transition taxonomy
    - Particle spectrum (quarks, leptons, bosons, generations)
    - Fine structure constant alpha
    - Mass ratio R = m_n/m_e
    - UV finiteness guarantee

    Book V adds: D-sector gravity, cosmology, temporal structure. -/
```

## Source Excerpt

```lean
structure BookVImportList where
  /-- Coupling constants exported. -/
  couplings : Nat := 10
  /-- Coupling constants Lean-verified. -/
  couplings_verified : Bool := true
  /-- Regimes classified. -/
  regimes : Nat := 9
  /-- Particle spectrum complete. -/
  spectrum_complete : Bool := true
  /-- Mass ratio R available. -/
  mass_ratio : Bool := true
  /-- UV finiteness guaranteed. -/
  uv_finite : Bool := true
  deriving Repr
```
