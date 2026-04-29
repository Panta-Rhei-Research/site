---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_closer_to_desi",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/tau-closer-to-desi/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::tau_closer_to_desi",
  "declaration_slug": "tau-closer-to-desi",
  "kind": "theorem",
  "name": "tau_closer_to_desi",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 358,
  "source_line_end": 360,
  "registry_ids": [
    "V.P160"
  ],
  "related_registry_items": [
    {
      "id": "V.P160",
      "title": "DESI Comparison",
      "url": "/registry/object/V.P160/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L358-L360",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L358-L360",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L358-L360)
- Source range: L358-L360
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P160` — DESI Comparison

## Immediate Comment / Docstring

```lean
/-- [V.P160] τ closer to DESI than ΛCDM on w₀. -/
```

## Source Excerpt

```lean
theorem tau_closer_to_desi :
    cpl_canonical.w0_offset_x1000 < cpl_canonical.desi_w0_offset_x1000 := by
  native_decide
```
