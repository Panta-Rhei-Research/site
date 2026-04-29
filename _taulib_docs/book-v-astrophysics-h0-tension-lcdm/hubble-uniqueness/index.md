---
{
  "projection_kind": "taulib_declaration",
  "title": "hubble_uniqueness",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/hubble-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::hubble_uniqueness",
  "declaration_slug": "hubble-uniqueness",
  "kind": "theorem",
  "name": "hubble_uniqueness",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 558,
  "source_line_end": 561,
  "registry_ids": [
    "V.T259"
  ],
  "related_registry_items": [
    {
      "id": "V.T259",
      "title": "Uniqueness of Hubble Formula",
      "url": "/registry/object/V.T259/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L558-L561",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L558-L561",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L558-L561)
- Source range: L558-L561
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T259` — Uniqueness of Hubble Formula

## Immediate Comment / Docstring

```lean
/-- [V.T259] Uniqueness: h = 2/3 + ι_τ²/17 is unique first-order correction. -/
```

## Source Excerpt

```lean
theorem hubble_uniqueness :
    hubble_derivation_data.free_params = 0 ∧
    hubble_derivation_data.derivation_steps = 2 := by
  native_decide
```
