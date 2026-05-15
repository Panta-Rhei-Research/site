---
{
  "projection_kind": "taulib_declaration",
  "title": "ThresholdType",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/threshold-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.ThresholdLadder`.",
  "declaration_id": "TauLib.BookV.Cosmology.ThresholdLadder::ThresholdType",
  "declaration_slug": "threshold-type",
  "kind": "inductive",
  "name": "ThresholdType",
  "module_name": "TauLib.BookV.Cosmology.ThresholdLadder",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/",
  "source_line_start": 64,
  "source_line_end": 77,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L64-L77",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.ThresholdLadder",
        "url": "/corpus/taulib/docs/book-v-cosmology-threshold-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L64-L77",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Cosmology.ThresholdLadder](/corpus/taulib/docs/book-v-cosmology-threshold-ladder/)
- Source path: [`TauLib/BookV/Cosmology/ThresholdLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/ThresholdLadder.lean#L64-L77)
- Source range: L64-L77
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Threshold type classification. -/
```

## Source Excerpt

```lean
inductive ThresholdType where
  /-- Electroweak symmetry breaking. -/
  | EW
  /-- Baryogenesis. -/
  | Baryogenesis
  /-- Neutron threshold. -/
  | Neutron
  /-- Nucleosynthesis window. -/
  | Nucleosynthesis
  /-- Hydrogen recombination. -/
  | Hydrogen
  /-- Photon decoupling (CMB). -/
  | PhotonDecoupling
  deriving Repr, DecidableEq, BEq
```
