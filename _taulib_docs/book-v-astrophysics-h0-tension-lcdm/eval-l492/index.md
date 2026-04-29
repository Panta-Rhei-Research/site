---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L492",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/eval-l492/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::#eval:492",
  "declaration_slug": "eval-l492",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 492,
  "source_line_end": 492,
  "registry_ids": [
    "V.P162",
    "V.R421"
  ],
  "related_registry_items": [
    {
      "id": "V.P162",
      "title": "f·σ₈ Comparison Table",
      "url": "/registry/object/V.P162/"
    },
    {
      "id": "V.R421",
      "title": "RSD Data Comparison",
      "url": "/registry/object/V.R421/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L492-L492",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L492-L492",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L492-L492)
- Source range: L492-L492
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.P162` — f·σ₈ Comparison Table
- `V.R421` — RSD Data Comparison

## Immediate Comment / Docstring

```lean
-- [V.P162] f·σ₈ comparison table: τ ~3% below ΛCDM at z = 0.3, 0.5, 0.7, 1.0.
-- [V.R421] RSD: DESI DR3 + Euclid at ~1-2% precision → decisive test.
```

## Source Excerpt

```lean
#eval growth_z03.fsigma8_tau_x1000     -- 470
```
