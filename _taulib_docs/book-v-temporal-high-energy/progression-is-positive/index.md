---
{
  "projection_kind": "taulib_declaration",
  "title": "progression_is_positive",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/progression-is-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::progression_is_positive",
  "declaration_slug": "progression-is-positive",
  "kind": "theorem",
  "name": "progression_is_positive",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 198,
  "source_line_end": 201,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L198-L201",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L198-L201",
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
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L198-L201)
- Source range: L198-L201
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Progression rate is always positive (tower never stops). -/
```

## Source Excerpt

```lean
theorem progression_is_positive (h : RefinementRate)
    (hr : h.rate_numer > 0) :
    h.rate_numer > 0 ∧ h.rate_denom > 0 :=
  ⟨hr, h.denom_pos⟩
```
