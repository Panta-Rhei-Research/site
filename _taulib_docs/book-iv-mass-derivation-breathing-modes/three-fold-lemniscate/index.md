---
{
  "projection_kind": "taulib_declaration",
  "title": "ThreeFoldLemniscate",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/three-fold-lemniscate/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::ThreeFoldLemniscate",
  "declaration_slug": "three-fold-lemniscate",
  "kind": "structure",
  "name": "ThreeFoldLemniscate",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 142,
  "source_line_end": 147,
  "registry_ids": [
    "IV.D312"
  ],
  "related_registry_items": [
    {
      "id": "IV.D312",
      "title": "Lemniscate three-fold",
      "url": "/registry/object/IV.D312/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L142-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.BreathingModes",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L142-L147",
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

- Module: [TauLib.BookIV.MassDerivation.BreathingModes](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/)
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L142-L147)
- Source range: L142-L147
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D312` — Lemniscate three-fold

## Immediate Comment / Docstring

```lean
/-- [IV.D312] Three-fold lemniscate: Lobe_B, Lobe_C, Crossing_ω. -/
```

## Source Excerpt

```lean
structure ThreeFoldLemniscate where
  three_fold_data : LemniscateThreeFold
  sector_B : String := "EM (γ)"
  sector_C : String := "Strong (η)"
  sector_omega : String := "Higgs (γ∩η)"
  deriving Repr
```
