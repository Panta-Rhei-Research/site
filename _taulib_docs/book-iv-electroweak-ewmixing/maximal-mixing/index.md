---
{
  "projection_kind": "taulib_declaration",
  "title": "MaximalMixing",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/maximal-mixing/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::MaximalMixing",
  "declaration_slug": "maximal-mixing",
  "kind": "structure",
  "name": "MaximalMixing",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 207,
  "source_line_end": 213,
  "registry_ids": [
    "IV.D132"
  ],
  "related_registry_items": [
    {
      "id": "IV.D132",
      "title": "Electroweak Coherence State",
      "url": "/registry/object/IV.D132/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L207-L213",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L207-L213",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L207-L213)
- Source range: L207-L213
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D132` — Electroweak Coherence State

## Immediate Comment / Docstring

```lean
/-- [IV.D132] Maximal mixing: the condition sin²(θ_W) = 1/4, which
    would mean equal W³ and B content in both γ and Z.
    In τ: sin²(θ_W) = ι_τ(1−ι_τ), which equals 1/4 iff ι_τ = 1/2.
    Since ι_τ ≈ 0.3415, mixing is SUB-maximal. -/
```

## Source Excerpt

```lean
structure MaximalMixing where
  /-- sin²(θ_W) at maximal mixing: 1/4. -/
  maximal_numer : Nat := 1
  maximal_denom : Nat := 4
  /-- Actual τ-value differs from 1/4. -/
  not_maximal : weinberg_angle_tau.sin2_numer * 4 ≠ weinberg_angle_tau.sin2_denom
  deriving Repr
```
