---
{
  "projection_kind": "taulib_declaration",
  "title": "weinberg_equals_kappaAD",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/weinberg-equals-kappa-ad/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::weinberg_equals_kappaAD",
  "declaration_slug": "weinberg-equals-kappa-ad",
  "kind": "theorem",
  "name": "weinberg_equals_kappaAD",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 294,
  "source_line_end": 297,
  "registry_ids": [
    "IV.T61"
  ],
  "related_registry_items": [
    {
      "id": "IV.T61",
      "title": "Weinberg Angle Prediction",
      "url": "/registry/object/IV.T61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L294-L297",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L294-L297",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L294-L297)
- Source range: L294-L297
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T61` — Weinberg Angle Prediction

## Immediate Comment / Docstring

```lean
/-- [IV.T61] The Weinberg angle is determined by the (A,D) cross-coupling:
    sin²(θ_W) = κ(A,D) = ι_τ(1−ι_τ) ≈ 0.2249.

    This is NOT a fit — it is a structural consequence of the
    temporal complement theorem: A and D exhaust the depth-1
    coupling budget (κ_A + κ_D = 1), so their cross-coupling
    κ(A,D) = ι_τ(1−ι_τ) is the natural mixing parameter. -/
```

## Source Excerpt

```lean
theorem weinberg_equals_kappaAD :
    weinberg_angle_tau.sin2_numer = kappa_AD.numer ∧
    weinberg_angle_tau.sin2_denom = kappa_AD.denom :=
  weinberg_angle_tau.equals_kappaAD
```
