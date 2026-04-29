---
{
  "projection_kind": "taulib_declaration",
  "title": "s8_nnlo_within_hsc",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-nnlo-within-hsc/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::s8_nnlo_within_hsc",
  "declaration_slug": "s8-nnlo-within-hsc",
  "kind": "theorem",
  "name": "s8_nnlo_within_hsc",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 685,
  "source_line_end": 688,
  "registry_ids": [
    "V.T266"
  ],
  "related_registry_items": [
    {
      "id": "V.T266",
      "title": "S₈ NNLO Consistent with KiDS and HSC",
      "url": "/registry/object/V.T266/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L685-L688",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L685-L688",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L685-L688)
- Source range: L685-L688
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T266` — S₈ NNLO Consistent with KiDS and HSC

## Immediate Comment / Docstring

```lean
/-- [V.T266] S₈(τ,NNLO) within 1σ of HSC Y3:
    |0.757 − 0.763| = 0.006 < 0.033. -/
```

## Source Excerpt

```lean
theorem s8_nnlo_within_hsc :
    s8_nnlo_data.s8_nnlo_x10000 / 10 ≥ s8_nnlo_data.s8_hsc_x1000 - s8_nnlo_data.s8_hsc_sigma_x1000 ∧
    s8_nnlo_data.s8_nnlo_x10000 / 10 ≤ s8_nnlo_data.s8_hsc_x1000 + s8_nnlo_data.s8_hsc_sigma_x1000 := by
  native_decide
```
