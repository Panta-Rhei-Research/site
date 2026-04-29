---
{
  "projection_kind": "taulib_declaration",
  "title": "DESISigma8Falsification",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/desisigma8-falsification/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::DESISigma8Falsification",
  "declaration_slug": "desisigma8-falsification",
  "kind": "structure",
  "name": "DESISigma8Falsification",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 505,
  "source_line_end": 514,
  "registry_ids": [
    "V.R453"
  ],
  "related_registry_items": [
    {
      "id": "V.R453",
      "title": "DESI σ₈ Falsification Window",
      "url": "/registry/object/V.R453/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L505-L514",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L505-L514",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L505-L514)
- Source range: L505-L514
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.R453` — DESI σ₈ Falsification Window

## Immediate Comment / Docstring

```lean
/-- [V.R453] DESI σ₈(z) falsification window.
    τ-prediction: (f·σ₈)_τ / (f·σ₈)_Λ ≈ 0.97, z-independent.
    DESI DR3 + Euclid DR1 at ~1% precision → decisive. -/
```

## Source Excerpt

```lean
structure DESISigma8Falsification where
  /-- τ/ΛCDM ratio (×1000): 0.97 → 970. -/
  tau_lcdm_ratio_x1000 : Nat := 970
  /-- DESI DR3 precision (×1000): 1% → 10. -/
  desi_precision_pct_x1000 : Nat := 10
  /-- z-independent (structural): 1 = yes. -/
  z_independent : Nat := 1
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
