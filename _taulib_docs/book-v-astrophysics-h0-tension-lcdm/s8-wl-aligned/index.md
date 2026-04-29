---
{
  "projection_kind": "taulib_declaration",
  "title": "s8_wl_aligned",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/s8-wl-aligned/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::s8_wl_aligned",
  "declaration_slug": "s8-wl-aligned",
  "kind": "theorem",
  "name": "s8_wl_aligned",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 417,
  "source_line_end": 419,
  "registry_ids": [
    "V.P161"
  ],
  "related_registry_items": [
    {
      "id": "V.P161",
      "title": "S₈ Tension Resolution",
      "url": "/registry/object/V.P161/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L417-L419",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L417-L419",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L417-L419)
- Source range: L417-L419
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P161` — S₈ Tension Resolution

## Immediate Comment / Docstring

```lean
/-- [V.P161] S₈ on WL side: S₈^(τ) < S₈^(Planck). -/
```

## Source Excerpt

```lean
theorem s8_wl_aligned :
    sigma8_canonical.s8_tau_x1000 < sigma8_canonical.s8_planck_x1000 := by
  native_decide
```
