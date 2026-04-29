---
{
  "projection_kind": "taulib_declaration",
  "title": "micro_macro_split",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/micro-macro-split/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::micro_macro_split",
  "declaration_slug": "micro-macro-split",
  "kind": "theorem",
  "name": "micro_macro_split",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 208,
  "source_line_end": 210,
  "registry_ids": [
    "IV.P151"
  ],
  "related_registry_items": [
    {
      "id": "IV.P151",
      "title": "Micro/Macro decomposition",
      "url": "/registry/object/IV.P151/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L208-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L208-L210",
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
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L208-L210)
- Source range: L208-L210
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P151` — Micro/Macro decomposition

## Immediate Comment / Docstring

```lean
/-- [IV.P151] Physics splits into microcosm (fiber T², Book IV)
    and macrocosm (base τ¹, Book V). -/
```

## Source Excerpt

```lean
theorem micro_macro_split :
    fiber_t2.gen_count = 3 ∧ tau1_base.gen_count = 2 := by
  simp [fiber_t2, tau1_base]
```
