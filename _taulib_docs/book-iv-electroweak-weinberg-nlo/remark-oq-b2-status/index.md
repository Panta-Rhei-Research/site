---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_oq_b2_status",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/remark-oq-b2-status/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::remark_oq_b2_status",
  "declaration_slug": "remark-oq-b2-status",
  "kind": "def",
  "name": "remark_oq_b2_status",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 205,
  "source_line_end": 206,
  "registry_ids": [
    "IV.R391"
  ],
  "related_registry_items": [
    {
      "id": "IV.R391",
      "title": "OQ-B2 Partial Resolution Status",
      "url": "/registry/object/IV.R391/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L205-L206",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L205-L206",
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
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L205-L206)
- Source range: L205-L206
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R391` — OQ-B2 Partial Resolution Status

## Immediate Comment / Docstring

```lean
/-- [IV.R391] OQ-B2 RESOLVED (τ-EFFECTIVE) via EW projection.
    The (5/7)·ι³ NLO correction has a structural derivation:
    5/7 = dim(V_EW) / dim(V_complement) on A_spec(L).
    See EWProjection.lean for the full derivation chain:
    A_spec(L) → EW partition (5+3+7=15) → density 5/7 → CF bridge → NLO.
    Residual: CF Compression Thesis (why CF matches mode census). -/
```

## Source Excerpt

```lean
def remark_oq_b2_status : String :=
  "OQ-B2 RESOLVED: 5/7 = EW projection density. See EWProjection.lean."
```
