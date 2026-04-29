---
{
  "projection_kind": "taulib_declaration",
  "title": "LCDMLimitation",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/lcdmlimitation/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::LCDMLimitation",
  "declaration_slug": "lcdmlimitation",
  "kind": "inductive",
  "name": "LCDMLimitation",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 188,
  "source_line_end": 201,
  "registry_ids": [
    "V.D150"
  ],
  "related_registry_items": [
    {
      "id": "V.D150",
      "title": "Category Error (LCDM)",
      "url": "/registry/object/V.D150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L188-L201",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L188-L201",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L188-L201)
- Source range: L188-L201
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D150` — Category Error (LCDM)

## Immediate Comment / Docstring

```lean
/-- [V.D150] ΛCDM limitation: specific failures or tensions of the
    standard ΛCDM cosmological model, each resolved by the τ-framework. -/
```

## Source Excerpt

```lean
inductive LCDMLimitation where
  /-- Dark matter: no particle found despite decades of searches. -/
  | DarkMatterMissing
  /-- Dark energy: 120 orders of magnitude vacuum energy discrepancy. -/
  | DarkEnergyFinetuning
  /-- H₀ tension: >5σ early/late discrepancy. -/
  | H0Tension
  /-- σ₈ tension: low-z clustering weaker than CMB predicts. -/
  | Sigma8Tension
  /-- Inflation: ad hoc, inflaton not found, initial conditions unclear. -/
  | InflationAdHoc
  /-- Baryon asymmetry: insufficient CP violation in SM. -/
  | BaryonAsymmetry
  deriving Repr, DecidableEq, BEq
```
