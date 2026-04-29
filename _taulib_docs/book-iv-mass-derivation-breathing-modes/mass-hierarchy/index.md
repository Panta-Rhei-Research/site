---
{
  "projection_kind": "taulib_declaration",
  "title": "MassHierarchy",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/mass-hierarchy/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::MassHierarchy",
  "declaration_slug": "mass-hierarchy",
  "kind": "structure",
  "name": "MassHierarchy",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 42,
  "source_line_end": 48,
  "registry_ids": [
    "IV.R336"
  ],
  "related_registry_items": [
    {
      "id": "IV.R336",
      "title": "Ten orders of magnitude from one constant",
      "url": "/registry/object/IV.R336/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L42-L48",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L42-L48",
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
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L42-L48)
- Source range: L42-L48
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R336` — Ten orders of magnitude from one constant

## Immediate Comment / Docstring

```lean
/-- [IV.R336] Three-tier mass hierarchy:
    bulk ι_τ^(-7) ≈ 1848, surface √3·ι_τ^(-2) ≈ 14.9,
    coupling π³α²·ι_τ^(-2) ≈ 0.014. -/
```

## Source Excerpt

```lean
structure MassHierarchy where
  bulk_approx : Nat := 1848000
  surface_approx : Nat := 14900
  coupling_approx : Nat := 14
  bulk_gt_surface : bulk_approx > surface_approx
  surface_gt_coupling : surface_approx > coupling_approx
  deriving Repr
```
