---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma8_suppression_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/sigma8-suppression-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::sigma8_suppression_theorem",
  "declaration_slug": "sigma8-suppression-theorem",
  "kind": "theorem",
  "name": "sigma8_suppression_theorem",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 412,
  "source_line_end": 414,
  "registry_ids": [
    "V.T236"
  ],
  "related_registry_items": [
    {
      "id": "V.T236",
      "title": "σ₈ Suppression Theorem",
      "url": "/registry/object/V.T236/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L412-L414",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L412-L414",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L412-L414)
- Source range: L412-L414
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T236` — σ₈ Suppression Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T236] σ₈ suppressed: σ₈^(τ) < σ₈^(CMB). -/
```

## Source Excerpt

```lean
theorem sigma8_suppression_theorem :
    sigma8_canonical.sigma8_tau_x1000 < sigma8_canonical.sigma8_cmb_x1000 := by
  native_decide
```
