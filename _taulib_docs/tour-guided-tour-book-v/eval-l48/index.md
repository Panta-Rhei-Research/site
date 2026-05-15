---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L48",
  "permalink": "/corpus/taulib/docs/tour-guided-tour-book-v/eval-l48/",
  "summary_short": "`eval` declaration in `TauLib.Tour.GuidedTour.BookV`.",
  "declaration_id": "TauLib.Tour.GuidedTour.BookV::#eval:48",
  "declaration_slug": "eval-l48",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.GuidedTour.BookV",
  "module_url": "/corpus/taulib/docs/tour-guided-tour-book-v/",
  "source_line_start": 48,
  "source_line_end": 74,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L48-L74",
  "formal_status": "computed",
  "declaration_role": "computed check",
  "formal_status_label": "computed check",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.GuidedTour.BookV",
        "url": "/corpus/taulib/docs/tour-guided-tour-book-v/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L48-L74",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "role": "computed check",
      "status": "computed check"
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

- Module: [TauLib.Tour.GuidedTour.BookV](/corpus/taulib/docs/tour-guided-tour-book-v/)
- Source path: [`TauLib/Tour/GuidedTour/BookV.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/GuidedTour/BookV.lean#L48-L74)
- Source range: L48-L74
- Kind: `eval`
- Public role: `computed check`
- Formal status hint: `computed check`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval constants_ledger.length


-- ================================================================
-- HINGE 2: Gravity from Boundary Holonomy
-- ================================================================

/-
The τ-Einstein equation: R^H = κ_τ · T^mat.
An algebraic identity, not a nonlinear PDE.
Chart shadow recovers G_μν = (8πG/c⁴)T_μν.
-/

-- Gravitational coupling κ_τ = 1 - ι_τ
-- (Encoded in the sector parameters)


-- ================================================================
-- HINGE 3: Gravitational Closing Identity
-- ================================================================

/-
α_G = α^18 · √3 · (1 - 3α/π). G predicted to 3 ppm.
-/

-- Constants ledger tracks all predictions with scope labels
#check e1_complete
```
