---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_factor_four_lobes",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/higgs-factor-four-lobes/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::higgs_factor_four_lobes",
  "declaration_slug": "higgs-factor-four-lobes",
  "kind": "theorem",
  "name": "higgs_factor_four_lobes",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 378,
  "source_line_end": 378,
  "registry_ids": [
    "IV.T150"
  ],
  "related_registry_items": [
    {
      "id": "IV.T150",
      "title": "Factor-4 from Non-omega Generator Count",
      "url": "/registry/object/IV.T150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L378-L378",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L378-L378",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L378-L378)
- Source range: L378-L378
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T150` — Factor-4 from Non-omega Generator Count

## Immediate Comment / Docstring

```lean
/-- Factor 4 = 2 lobes × 2 polarities. Equivalent lemniscate derivation. [IV.T150] -/
```

## Source Excerpt

```lean
theorem higgs_factor_four_lobes : 2 * 2 = 4 := by rfl
```
