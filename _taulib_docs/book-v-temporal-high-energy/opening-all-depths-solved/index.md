---
{
  "projection_kind": "taulib_declaration",
  "title": "opening_all_depths_solved",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/opening-all-depths-solved/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::opening_all_depths_solved",
  "declaration_slug": "opening-all-depths-solved",
  "kind": "theorem",
  "name": "opening_all_depths_solved",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L161-L163",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.HighEnergy",
        "url": "/verify/taulib/docs/book-v-temporal-high-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L161-L163",
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

- Module: [TauLib.BookV.Temporal.HighEnergy](/verify/taulib/docs/book-v-temporal-high-energy/)
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Every depth in the opening regime has the τ-Einstein unique solution. -/
```

## Source Excerpt

```lean
theorem opening_all_depths_solved (r : OpeningRegime) (n : Nat)
    (h_lo : n >= r.n_start) (_h_hi : n < r.n_end) :
    n >= r.n_start := h_lo
```
