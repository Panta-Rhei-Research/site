---
{
  "projection_kind": "taulib_declaration",
  "title": "nlo_from_windows",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/nlo-from-windows/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::nlo_from_windows",
  "declaration_slug": "nlo-from-windows",
  "kind": "theorem",
  "name": "nlo_from_windows",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 69,
  "source_line_end": 73,
  "registry_ids": [
    "IV.T134"
  ],
  "related_registry_items": [
    {
      "id": "IV.T134",
      "title": "Window Algebra Origin",
      "url": "/registry/object/IV.T134/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L69-L73",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L69-L73",
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
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L69-L73)
- Source range: L69-L73
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T134` — Window Algebra Origin

## Immediate Comment / Docstring

```lean
/-- [IV.T134] The 5/7 coefficient arises from the W₃ window algebra:
    both numerator and denominator are determined by two adjacent
    width-3 windows on the CF head of ι_τ. -/
```

## Source Excerpt

```lean
theorem nlo_from_windows :
    weinbergNLO.nlo_num = 5 ∧
    weinbergNLO.nlo_den = 7 ∧
    weinbergNLO.nlo_num + weinbergNLO.nlo_den = 12 := by
  exact ⟨rfl, rfl, rfl⟩
```
