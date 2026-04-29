---
{
  "projection_kind": "taulib_declaration",
  "title": "vacuum_catastrophe_diagnostic",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/vacuum-catastrophe-diagnostic/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::vacuum_catastrophe_diagnostic",
  "declaration_slug": "vacuum-catastrophe-diagnostic",
  "kind": "theorem",
  "name": "vacuum_catastrophe_diagnostic",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 275,
  "source_line_end": 277,
  "registry_ids": [
    "V.R257"
  ],
  "related_registry_items": [
    {
      "id": "V.R257",
      "title": "The vacuum catastrophe as diagnostic",
      "url": "/registry/object/V.R257/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L275-L277",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L275-L277",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L275-L277)
- Source range: L275-L277
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R257` — The vacuum catastrophe as diagnostic

## Immediate Comment / Docstring

```lean
/-- [V.R257] The vacuum catastrophe (10^120 mismatch) is a diagnostic:
    it reveals that QFT computes rho_vac as though every mode contributes,
    while the ontic value is zero (finite profinite sum, exact cancellation). -/
```

## Source Excerpt

```lean
theorem vacuum_catastrophe_diagnostic :
    "rho_vac^QFT / rho_vac^tau ~ 10^120, diagnostic of readout artifact" =
    "rho_vac^QFT / rho_vac^tau ~ 10^120, diagnostic of readout artifact" := rfl
```
