---
{
  "projection_kind": "taulib_declaration",
  "title": "window_nnlo_period",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/window-nnlo-period/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::window_nnlo_period",
  "declaration_slug": "window-nnlo-period",
  "kind": "theorem",
  "name": "window_nnlo_period",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 619,
  "source_line_end": 623,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L619-L623",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L619-L623",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L619-L623)
- Source range: L619-L623
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- W₃(4)² = 25 governs NNLO: period structure. -/
```

## Source Excerpt

```lean
theorem window_nnlo_period :
    window_rg_period.w34 = 5 ∧
    window_rg_period.nnlo_value = 25 ∧
    window_rg_period.nnlo_value = window_rg_period.w34 * window_rg_period.w34 :=
  ⟨rfl, rfl, rfl⟩
```
