---
{
  "projection_kind": "taulib_declaration",
  "title": "mw_nlo_coefficient",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/mw-nlo-coefficient/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::mw_nlo_coefficient",
  "declaration_slug": "mw-nlo-coefficient",
  "kind": "theorem",
  "name": "mw_nlo_coefficient",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 245,
  "source_line_end": 248,
  "registry_ids": [
    "IV.D338"
  ],
  "related_registry_items": [
    {
      "id": "IV.D338",
      "title": "M_W NLO Formula",
      "url": "/registry/object/IV.D338/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L245-L248",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L245-L248",
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

- Module: [TauLib.BookIV.Electroweak.WeinbergNLO](/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/)
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L245-L248)
- Source range: L245-L248
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.D338` — M_W NLO Formula

## Immediate Comment / Docstring

```lean
/-- [IV.D338] M_W NLO coefficient windows: W₃(4)=5 and W₃(3)=17. -/
```

## Source Excerpt

```lean
theorem mw_nlo_coefficient :
    windowSum cf_head 3 4 = 5 ∧
    windowSum cf_head 3 3 = 17 := by
  exact ⟨w3_at_4, w3_at_3⟩
```
