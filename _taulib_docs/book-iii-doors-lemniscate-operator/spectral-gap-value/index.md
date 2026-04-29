---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_gap_value",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/spectral-gap-value/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::spectral_gap_value",
  "declaration_slug": "spectral-gap-value",
  "kind": "theorem",
  "name": "spectral_gap_value",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 207,
  "source_line_end": 210,
  "registry_ids": [
    "III.P09"
  ],
  "related_registry_items": [
    {
      "id": "III.P09",
      "title": "Discrete Spectrum of H_L",
      "url": "/registry/object/III.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L207-L210",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.LemniscateOperator",
        "url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L207-L210",
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/verify/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L207-L210)
- Source range: L207-L210
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P09` — Discrete Spectrum of H_L

## Immediate Comment / Docstring

```lean
/-- [III.P09] Structural: spectral gap value is 1. -/
```

## Source Excerpt

```lean
theorem spectral_gap_value :
    lemniscate_eigenvalue 1 = 1 := rfl

end Tau.BookIII.Doors
```
