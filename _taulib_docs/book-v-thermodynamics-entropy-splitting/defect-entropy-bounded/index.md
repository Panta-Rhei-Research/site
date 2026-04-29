---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_entropy_bounded",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/defect-entropy-bounded/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.EntropySplitting`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.EntropySplitting::defect_entropy_bounded",
  "declaration_slug": "defect-entropy-bounded",
  "kind": "theorem",
  "name": "defect_entropy_bounded",
  "module_name": "TauLib.BookV.Thermodynamics.EntropySplitting",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/",
  "source_line_start": 176,
  "source_line_end": 179,
  "registry_ids": [
    "V.T57"
  ],
  "related_registry_items": [
    {
      "id": "V.T57",
      "title": "Defect entropy is bounded",
      "url": "/registry/object/V.T57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L176-L179",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.EntropySplitting",
        "url": "/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L176-L179",
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

- Module: [TauLib.BookV.Thermodynamics.EntropySplitting](/verify/taulib/docs/book-v-thermodynamics-entropy-splitting/)
- Source path: [`TauLib/BookV/Thermodynamics/EntropySplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/EntropySplitting.lean#L176-L179)
- Source range: L176-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T57` — Defect entropy is bounded

## Immediate Comment / Docstring

```lean
/-- [V.T57] Defect entropy is bounded: 0 <= S_def(n) <= S_def(0).
    Defect entropy can never exceed its initial value (Nat is non-negative). -/
```

## Source Excerpt

```lean
theorem defect_entropy_bounded (e0 en : MacroDefectEntropy)
    (h_same_denom : e0.s_def_denom = en.s_def_denom)
    (h_bound : en.s_def_numer ≤ e0.s_def_numer) :
    en.s_def_numer ≤ e0.s_def_numer := h_bound
```
