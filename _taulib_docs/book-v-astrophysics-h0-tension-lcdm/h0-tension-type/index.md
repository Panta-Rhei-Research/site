---
{
  "projection_kind": "taulib_declaration",
  "title": "H0TensionType",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/h0-tension-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::H0TensionType",
  "declaration_slug": "h0-tension-type",
  "kind": "inductive",
  "name": "H0TensionType",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 131,
  "source_line_end": 140,
  "registry_ids": [
    "V.D149"
  ],
  "related_registry_items": [
    {
      "id": "V.D149",
      "title": "Depth-Projected Hubble Parameter",
      "url": "/registry/object/V.D149/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L131-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L131-L140",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L131-L140)
- Source range: L131-L140
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D149` — Depth-Projected Hubble Parameter

## Immediate Comment / Docstring

```lean
/-- [V.D149] H₀ tension type classification. -/
```

## Source Excerpt

```lean
inductive H0TensionType where
  /-- Statistical fluke (< 3σ, now excluded). -/
  | StatisticalFluke
  /-- Systematic error in one method. -/
  | SystematicError
  /-- New physics needed. -/
  | NewPhysics
  /-- Readout-scale artifact (τ-framework resolution). -/
  | ReadoutArtifact
  deriving Repr, DecidableEq, BEq
```
