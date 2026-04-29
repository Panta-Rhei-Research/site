---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L157",
  "permalink": "/verify/taulib/docs/tour-physics/eval-l157/",
  "summary_short": "`eval` declaration in `TauLib.Tour.Physics`.",
  "declaration_id": "TauLib.Tour.Physics::#eval:157",
  "declaration_slug": "eval-l157",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.Tour.Physics",
  "module_url": "/verify/taulib/docs/tour-physics/",
  "source_line_start": 157,
  "source_line_end": 185,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L157-L185",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.Tour.Physics",
        "url": "/verify/taulib/docs/tour-physics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L157-L185",
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

- Module: [TauLib.Tour.Physics](/verify/taulib/docs/tour-physics/)
- Source path: [`TauLib/Tour/Physics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/Tour/Physics.lean#L157-L185)
- Source range: L157-L185
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- The tensor-to-scalar ratio r = ι_τ⁴ ≈ 0.0136 is a hard
-- falsification target for CMB-S4 at ~14σ:
```

## Source Excerpt

```lean
#eval tensor_scalar_data.cmbs4_sigma -- 14

-- ================================================================
-- PART 6: ROTATION CURVES (Book V, Chapter 34)
-- ================================================================

-- Flat galaxy rotation curves emerge from boundary holonomy
-- corrections to the D-sector (gravitational) coupling.
-- In the deep MOND regime: v_flat = (G·M·a₀)^{1/4}.
-- The acceleration scale a₀ is NOT free — it derives from ι_τ.

#check flat_rotation_theorem       -- v_flat = (G*M*a0)^(1/4)
#check mond_scale_from_iota        -- a₀ derives from ι_τ, not a free parameter
#check no_dark_halo                -- no dark matter halo required

-- The Radial Acceleration Relation follows from a single coupling:
#check rar_from_single_coupling    -- RAR from single D-sector coupling

-- ================================================================
-- PART 7: BARYOGENESIS (Book V, Chapter 56)
-- ================================================================

-- The baryon-to-photon ratio η_B ≈ 6 × 10⁻¹⁰ is derived from:
--   η_B = α · ι_τ¹⁵ · (5/6) = (121/270) · ι_τ¹⁹
-- where exponent 15 = dim(τ³) × |generators| = 3 × 5.

#check exponent_15_is_dim_times_generators  -- tau3_dim * [α,π,γ,η,ω].length = 15
#check exponent_15_structure                -- 3 * 5 = 15
#check tau_generator_count                  -- [α,π,γ,η,ω].length = 5
```
