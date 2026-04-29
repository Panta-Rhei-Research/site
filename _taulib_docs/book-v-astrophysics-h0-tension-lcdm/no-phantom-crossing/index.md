---
{
  "projection_kind": "taulib_declaration",
  "title": "NoPhantomCrossing",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/no-phantom-crossing/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::NoPhantomCrossing",
  "declaration_slug": "no-phantom-crossing",
  "kind": "structure",
  "name": "NoPhantomCrossing",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 332,
  "source_line_end": 339,
  "registry_ids": [
    "V.T235"
  ],
  "related_registry_items": [
    {
      "id": "V.T235",
      "title": "No Phantom Crossing Theorem",
      "url": "/registry/object/V.T235/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L332-L339",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L332-L339",
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
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L332-L339)
- Source range: L332-L339
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T235` — No Phantom Crossing Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T235] No Phantom Crossing:
    w(z) > −1 for all z. f_def ∈ [0,1] → w = −1 + (2/3)f_def/(1−f_def) ≥ −1.
    Topological constraint: defect fraction cannot be negative. -/
```

## Source Excerpt

```lean
structure NoPhantomCrossing where
  /-- w(z) ≥ −1 for all z. -/
  w_geq_minus_one : Bool := true
  /-- Phantom barrier never crossed. -/
  no_crossing : Bool := true
  /-- Falsifiable: if w < −1 observed → τ falsified. -/
  falsifiable : Bool := true
  deriving Repr
```
