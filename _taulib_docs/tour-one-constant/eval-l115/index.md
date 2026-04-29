---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L115",
  "permalink": "/verify/taulib/docs/tour-one-constant/eval-l115/",
  "summary_short": "`eval` declaration in `TauLib.Tour.OneConstant`.",
  "declaration_id": "TauLib.Tour.OneConstant::#eval:115",
  "declaration_slug": "eval-l115",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.OneConstant",
  "module_url": "/verify/taulib/docs/tour-one-constant/",
  "source_line_start": 115,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/OneConstant.lean#L115-L126",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.OneConstant",
        "url": "/verify/taulib/docs/tour-one-constant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/OneConstant.lean#L115-L126",
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

- Module: [TauLib.Tour.OneConstant](/verify/taulib/docs/tour-one-constant/)
- Source path: [`TauLib/Tour/OneConstant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/OneConstant.lean#L115-L126)
- Source range: L115-L126
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Tensor-to-scalar ratio: r = ι_τ⁴
-- Current bound: r < 0.036 (BICEP/Keck 2021)
-- τ: ≈ 0.0136 (comfortably below)
```

## Source Excerpt

```lean
#eval tensor_scalar_ratio    -- ≈ 0.01357


-- ============================================================
-- 4. GRAVITY & COSMOLOGY
-- ============================================================

/-
The D-sector (α-generator) governs gravity. The cosmological
constant Λ = 0 exactly in τ — not nearly zero, but exactly zero.
Dark energy is reinterpreted as a boundary holonomy effect.
-/
```
