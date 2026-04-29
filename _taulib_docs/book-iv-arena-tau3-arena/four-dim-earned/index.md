---
{
  "projection_kind": "taulib_declaration",
  "title": "four_dim_earned",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/four-dim-earned/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::four_dim_earned",
  "declaration_slug": "four-dim-earned",
  "kind": "theorem",
  "name": "four_dim_earned",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 165,
  "source_line_end": 168,
  "registry_ids": [
    "IV.P150"
  ],
  "related_registry_items": [
    {
      "id": "IV.P150",
      "title": "Four dimensions earned",
      "url": "/registry/object/IV.P150/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L165-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L165-L168",
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
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L165-L168)
- Source range: L165-L168
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P150` — Four dimensions earned

## Immediate Comment / Docstring

```lean
/-- [IV.P150] Four dimensions earned: 2 base generators + 3 fiber generators
    = 1 temporal + 3 spatial = 4 physical dimensions. -/
```

## Source Excerpt

```lean
theorem four_dim_earned :
    tau1_base.gen_count + fiber_t2.gen_count = 5 ∧
    tau1_base.gen_count = 2 ∧ fiber_t2.gen_count = 3 := by
  simp [tau1_base, fiber_t2]
```
