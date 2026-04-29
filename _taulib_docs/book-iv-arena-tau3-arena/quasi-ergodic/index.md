---
{
  "projection_kind": "taulib_declaration",
  "title": "quasi_ergodic",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/quasi-ergodic/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::quasi_ergodic",
  "declaration_slug": "quasi-ergodic",
  "kind": "theorem",
  "name": "quasi_ergodic",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 151,
  "source_line_end": 157,
  "registry_ids": [
    "IV.P149"
  ],
  "related_registry_items": [
    {
      "id": "IV.P149",
      "title": "Quasi-ergodicity",
      "url": "/registry/object/IV.P149/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L151-L157",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.Tau3Arena",
        "url": "/verify/taulib/docs/book-iv-arena-tau3-arena/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L151-L157",
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

- Module: [TauLib.BookIV.Arena.Tau3Arena](/verify/taulib/docs/book-iv-arena-tau3-arena/)
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L151-L157)
- Source range: L151-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P149` — Quasi-ergodicity

## Immediate Comment / Docstring

```lean
/-- [IV.P149] Quasi-ergodicity: every sector contributes to every sufficiently
    deep orbit level. Formalized: all 5 sectors are active (positive coupling). -/
```

## Source Excerpt

```lean
theorem quasi_ergodic :
    gravity_sector.coupling_numer > 0 ∧
    weak_sector.coupling_numer > 0 ∧
    em_sector.coupling_numer > 0 ∧
    strong_sector.coupling_numer > 0 ∧
    higgs_sector.coupling_numer > 0 :=
  all_couplings_pos
```
