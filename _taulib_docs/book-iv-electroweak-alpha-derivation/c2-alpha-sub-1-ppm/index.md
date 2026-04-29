---
{
  "projection_kind": "taulib_declaration",
  "title": "c2_alpha_sub_1_ppm",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/c2-alpha-sub-1-ppm/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::c2_alpha_sub_1_ppm",
  "declaration_slug": "c2-alpha-sub-1-ppm",
  "kind": "theorem",
  "name": "c2_alpha_sub_1_ppm",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 437,
  "source_line_end": 439,
  "registry_ids": [
    "IV.P225"
  ],
  "related_registry_items": [
    {
      "id": "IV.P225",
      "title": "c₂ Numerical Bound from W₄(3)",
      "url": "/registry/object/IV.P225/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L437-L439",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L437-L439",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L437-L439)
- Source range: L437-L439
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P225` — c₂ Numerical Bound from W₄(3)

## Immediate Comment / Docstring

```lean
/-- [IV.P225] Two-loop α correction is sub-1 ppm:
    α·c₂·ι_τ² ≈ (1/137)·(1/18)·0.1165 ≈ 4.7×10⁻⁵ ≈ 0.5 ppm. -/
```

## Source Excerpt

```lean
theorem c2_alpha_sub_1_ppm :
    two_loop_window.c2_denom = 18 ∧
    two_loop_window.w3_4 = 5 := ⟨rfl, rfl⟩
```
