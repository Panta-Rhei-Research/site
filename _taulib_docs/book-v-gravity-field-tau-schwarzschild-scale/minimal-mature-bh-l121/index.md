---
{
  "projection_kind": "taulib_declaration",
  "title": "minimal_mature_bh",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/minimal-mature-bh-l121/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschildScale`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschildScale::minimal_mature_bh",
  "declaration_slug": "minimal-mature-bh-l121",
  "kind": "theorem",
  "name": "minimal_mature_bh",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschildScale",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/",
  "source_line_start": 121,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L121-L126",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschildScale",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L121-L126",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschildScale](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschildScale.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L121-L126)
- Source range: L121-L126
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Minimal mature BH threshold exists and bounds population. -/
```

## Source Excerpt

```lean
theorem minimal_mature_bh :
    minimal_bh.threshold_exists = true ∧
    minimal_bh.below_unstable = true ∧
    minimal_bh.above_stable = true ∧
    minimal_bh.population_bounded = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
