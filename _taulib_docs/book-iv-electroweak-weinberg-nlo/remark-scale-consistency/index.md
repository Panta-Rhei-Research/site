---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_scale_consistency",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-scale-consistency/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::remark_scale_consistency",
  "declaration_slug": "remark-scale-consistency",
  "kind": "def",
  "name": "remark_scale_consistency",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 111,
  "source_line_end": 112,
  "registry_ids": [
    "IV.R389"
  ],
  "related_registry_items": [
    {
      "id": "IV.R389",
      "title": "Scale Consistency",
      "url": "/registry/object/IV.R389/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L111-L112",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeinbergNLO",
        "url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L111-L112",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L111-L112)
- Source range: L111-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R389` — Scale Consistency

## Immediate Comment / Docstring

```lean
/-- [IV.R389] Scale consistency: the tree value ι(1−ι) lives at μ* ≈ 4.8 GeV.
    The NLO correction (5/7)·ι³ captures 99.7% of SM 1-loop running from
    μ* to M_Z. The 86 ppm residual is from higher-loop and threshold effects. -/
```

## Source Excerpt

```lean
def remark_scale_consistency : String :=
  "Tree value at mu* ~ 4.8 GeV (near m_b). NLO captures 99.7% of 1-loop running to M_Z."
```
