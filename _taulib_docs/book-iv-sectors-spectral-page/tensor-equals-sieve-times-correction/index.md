---
{
  "projection_kind": "taulib_declaration",
  "title": "tensor_equals_sieve_times_correction",
  "permalink": "/verify/taulib/docs/book-iv-sectors-spectral-page/tensor-equals-sieve-times-correction/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.SpectralPage`.",
  "declaration_id": "TauLib.BookIV.Sectors.SpectralPage::tensor_equals_sieve_times_correction",
  "declaration_slug": "tensor-equals-sieve-times-correction",
  "kind": "theorem",
  "name": "tensor_equals_sieve_times_correction",
  "module_name": "TauLib.BookIV.Sectors.SpectralPage",
  "module_url": "/verify/taulib/docs/book-iv-sectors-spectral-page/",
  "source_line_start": 92,
  "source_line_end": 93,
  "registry_ids": [
    "IV.P179"
  ],
  "related_registry_items": [
    {
      "id": "IV.P179",
      "title": "E₁ Page Derivation of α-Coefficient",
      "url": "/registry/object/IV.P179/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L92-L93",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SpectralPage",
        "url": "/verify/taulib/docs/book-iv-sectors-spectral-page/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L92-L93",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Sectors.SpectralPage](/verify/taulib/docs/book-iv-sectors-spectral-page/)
- Source path: [`TauLib/BookIV/Sectors/SpectralPage.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SpectralPage.lean#L92-L93)
- Source range: L92-L93
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P179` — E₁ Page Derivation of α-Coefficient

## Immediate Comment / Docstring

```lean
/-- [IV.P179] Tensor square contains the sieve × correction factorization.
    (8/15)·(121/120) = 121/225.
    Cross-multiplied: 8 · 121 · 225 = 15 · 121 · 120. -/
```

## Source Excerpt

```lean
theorem tensor_equals_sieve_times_correction :
    8 * 121 * 225 = 15 * (121 : Nat) * 120 := by omega
```
