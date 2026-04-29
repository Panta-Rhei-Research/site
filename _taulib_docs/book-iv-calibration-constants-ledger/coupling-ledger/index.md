---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_ledger",
  "permalink": "/verify/taulib/docs/book-iv-calibration-constants-ledger/coupling-ledger/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.ConstantsLedger`.",
  "declaration_id": "TauLib.BookIV.Calibration.ConstantsLedger::coupling_ledger",
  "declaration_slug": "coupling-ledger",
  "kind": "def",
  "name": "coupling_ledger",
  "module_name": "TauLib.BookIV.Calibration.ConstantsLedger",
  "module_url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/",
  "source_line_start": 87,
  "source_line_end": 98,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L87-L98",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.ConstantsLedger",
        "url": "/verify/taulib/docs/book-iv-calibration-constants-ledger/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L87-L98",
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

- Module: [TauLib.BookIV.Calibration.ConstantsLedger](/verify/taulib/docs/book-iv-calibration-constants-ledger/)
- Source path: [`TauLib/BookIV/Calibration/ConstantsLedger.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/ConstantsLedger.lean#L87-L98)
- Source range: L87-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 10 coupling constants from ι_τ. -/
```

## Source Excerpt

```lean
def coupling_ledger : List LedgerEntry := [
  ⟨"IV.D07/DD", "κ(D,D) = 1−ι_τ (gravity)", "coupling", .Established⟩,
  ⟨"IV.D07/AA", "κ(A,A) = ι_τ (weak)", "coupling", .Established⟩,
  ⟨"IV.D07/BB", "κ(B,B) = ι_τ² (EM)", "coupling", .Established⟩,
  ⟨"IV.D07/CC", "κ(C,C) = ι_τ³/(1−ι_τ) (strong)", "coupling", .Established⟩,
  ⟨"IV.D07/AB", "κ(A,B) = ι_τ²(1−ι_τ) (electroweak)", "coupling", .Established⟩,
  ⟨"IV.D07/AC", "κ(A,C) = ι_τ³ (weak-strong)", "coupling", .Established⟩,
  ⟨"IV.D07/AD", "κ(A,D) = ι_τ(1−ι_τ) (weak-gravity)", "coupling", .Established⟩,
  ⟨"IV.D07/BC", "κ(B,C) = ι_τ³/(1+ι_τ) (Higgs/mass)", "coupling", .Established⟩,
  ⟨"IV.D07/BD", "κ(B,D) = ι_τ²(1−ι_τ)² (EM-gravity)", "coupling", .Established⟩,
  ⟨"IV.D07/CD", "κ(C,D) = ι_τ³(1−ι_τ) (strong-gravity)", "coupling", .Established⟩
]
```
