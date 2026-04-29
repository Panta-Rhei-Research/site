---
{
  "projection_kind": "taulib_declaration",
  "title": "perturbative_hierarchy",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/perturbative-hierarchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::perturbative_hierarchy",
  "declaration_slug": "perturbative-hierarchy",
  "kind": "theorem",
  "name": "perturbative_hierarchy",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 211,
  "source_line_end": 222,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L211-L222",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L211-L222",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L211-L222)
- Source range: L211-L222
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The perturbative hierarchy: π³α² < √3/1000.
    The holonomy correction is 1000× smaller than the lemniscate correction.

    (Recall √3 ≈ 1.732, π³α² ≈ 0.00165, ratio ≈ 1050) -/
```

## Source Excerpt

```lean
theorem perturbative_hierarchy :
    -- π³α² × 1000 < √3 (at rational approximation scale)
    -- pi_cubed_numer × alpha_sq_numer × 1000 × sqrt3_denom <
    -- sqrt3_numer × pi_cubed_denom × alpha_sq_denom
    -- Using: sqrt3 from LemniscateCapacity would create a circular dependency,
    -- so we inline the value: √3 ≈ 17320508/10000000
    pi_cubed_numer * alpha_sq_numer * 1000 * 10000000 <
    17320508 * pi_cubed_denom * alpha_sq_denom := by
  simp [pi_cubed_numer, pi_cubed_denom,
        alpha_sq_numer, alpha_sq_denom,
        iota_fourth_numer, iota_fourth_denom,
        iota, iotaD, iota_tau_numer, iota_tau_denom]
```
