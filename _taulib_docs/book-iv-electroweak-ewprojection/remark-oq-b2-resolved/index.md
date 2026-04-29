---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_oq_b2_resolved",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/remark-oq-b2-resolved/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::remark_oq_b2_resolved",
  "declaration_slug": "remark-oq-b2-resolved",
  "kind": "def",
  "name": "remark_oq_b2_resolved",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 195,
  "source_line_end": 197,
  "registry_ids": [
    "IV.R392"
  ],
  "related_registry_items": [
    {
      "id": "IV.R392",
      "title": "OQ-B2 Resolved",
      "url": "/registry/object/IV.R392/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L195-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWProjection",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L195-L197",
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L195-L197)
- Source range: L195-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R392` — OQ-B2 Resolved

## Immediate Comment / Docstring

```lean
/-- [IV.R392] OQ-B2 RESOLVED (τ-EFFECTIVE).

    Derivation chain:
    1. A_spec(L) has 15 boundary modes (5 generators × 3 configs)
    2. EW partition: V_EW (5) + V_strong (3) + V_complement (7) = 15
    3. Density: 5/7 = dim(V_EW) / dim(V_complement)
    4. CF bridge: 5 = W₃(4), 7 = W₃(3) − 2·W₃(4) (numerical match)
    5. NLO: sin²θ_W = ι(1−ι) · (1 + (5/7)·ι³)  at 86 ppm

    Residual open: WHY does CF[ι_τ] match the mode census?
    (CF Compression Thesis — foundational, beyond series scope) -/
```

## Source Excerpt

```lean
def remark_oq_b2_resolved : String :=
  "OQ-B2 RESOLVED: 5/7 = EW projection density on A_spec(L). " ++
  "V_EW (5) / V_complement (7) from carrier + polarity + mixing rules."
```
