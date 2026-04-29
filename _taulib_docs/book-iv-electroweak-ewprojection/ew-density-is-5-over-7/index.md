---
{
  "projection_kind": "taulib_declaration",
  "title": "ew_density_is_5_over_7",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-density-is-5-over-7/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::ew_density_is_5_over_7",
  "declaration_slug": "ew-density-is-5-over-7",
  "kind": "theorem",
  "name": "ew_density_is_5_over_7",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 137,
  "source_line_end": 138,
  "registry_ids": [
    "IV.T137"
  ],
  "related_registry_items": [
    {
      "id": "IV.T137",
      "title": "EW Density = 5/7",
      "url": "/registry/object/IV.T137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L137-L138",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L137-L138",
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L137-L138)
- Source range: L137-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T137` — EW Density = 5/7

## Immediate Comment / Docstring

```lean
/-- [IV.T137] The EW projection density is 5/7.
    Cross-multiplied: |V_EW| × |V_complement_den| = |V_complement| × |V_EW_num|
    where both equal 35. -/
```

## Source Excerpt

```lean
theorem ew_density_is_5_over_7 :
    ewActiveModes.length * 7 = ewComplement.length * 5 := by native_decide
```
