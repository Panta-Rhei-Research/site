---
{
  "projection_kind": "taulib_declaration",
  "title": "mode_interpretation_17",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/mode-interpretation-17/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeinbergNLO`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeinbergNLO::mode_interpretation_17",
  "declaration_slug": "mode-interpretation-17",
  "kind": "theorem",
  "name": "mode_interpretation_17",
  "module_name": "TauLib.BookIV.Electroweak.WeinbergNLO",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weinberg-nlo/",
  "source_line_start": 168,
  "source_line_end": 168,
  "registry_ids": [
    "IV.P181"
  ],
  "related_registry_items": [
    {
      "id": "IV.P181",
      "title": "Mode Interpretation of EW Coefficients",
      "url": "/registry/object/IV.P181/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L168-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L168-L168",
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
- Source path: [`TauLib/BookIV/Electroweak/WeinbergNLO.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeinbergNLO.lean#L168-L168)
- Source range: L168-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P181` — Mode Interpretation of EW Coefficients

## Immediate Comment / Docstring

```lean
/-- [IV.P181] Mode interpretation of 17: n_total + n_A = 15 + 2 = 17.
    17 = total boundary modes + weak-sector active modes.
    Equivalently: 17 = "EW-augmented total" on A_spec(L). -/
```

## Source Excerpt

```lean
theorem mode_interpretation_17 : (15 : Nat) + 2 = 17 := by omega
```
