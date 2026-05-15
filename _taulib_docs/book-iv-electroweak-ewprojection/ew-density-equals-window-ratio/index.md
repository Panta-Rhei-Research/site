---
{
  "projection_kind": "taulib_declaration",
  "title": "ew_density_equals_window_ratio",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-ewprojection/ew-density-equals-window-ratio/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::ew_density_equals_window_ratio",
  "declaration_slug": "ew-density-equals-window-ratio",
  "kind": "theorem",
  "name": "ew_density_equals_window_ratio",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 167,
  "source_line_end": 174,
  "registry_ids": [
    "IV.T138"
  ],
  "related_registry_items": [
    {
      "id": "IV.T138",
      "title": "EW–CF Bridge",
      "url": "/registry/object/IV.T138/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L167-L174",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWProjection",
        "url": "/corpus/taulib/docs/book-iv-electroweak-ewprojection/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L167-L174",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/corpus/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L167-L174)
- Source range: L167-L174
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.T138` — EW–CF Bridge

## Immediate Comment / Docstring

```lean
/-- [IV.T138] Bridge theorem: the EW mode density equals the CF window ratio.
    |V_EW| = W₃(4) = 5 and |V_complement| = W₃(3) − 2·W₃(4) = 7.
    This links the structural partition to the CF algebra of ι_τ. -/
```

## Source Excerpt

```lean
theorem ew_density_equals_window_ratio :
    ewActiveModes.length = windowSum cf_head 3 4 ∧
    ewComplement.length = windowSum cf_head 3 3 - 2 * windowSum cf_head 3 4 := by
  constructor
  · -- |V_EW| = W₃(4) = 5
    native_decide
  · -- |V_complement| = W₃(3) − 2·W₃(4) = 17 − 10 = 7
    native_decide
```
