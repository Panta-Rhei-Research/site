---
{
  "projection_kind": "taulib_declaration",
  "title": "fiber_t2",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/fiber-t2-l86/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::fiber_t2",
  "declaration_slug": "fiber-t2-l86",
  "kind": "def",
  "name": "fiber_t2",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 86,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L86-L94",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L86-L94",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L86-L94)
- Source range: L86-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical fiber T². -/
```

## Source Excerpt

```lean
def fiber_t2 : FiberT2 where
  gen_count := 3
  gen_count_eq := rfl
  em_gen := .gamma
  em_is_gamma := rfl
  strong_gen := .eta
  strong_is_eta := rfl
  higgs_gen := .omega
  higgs_is_omega := rfl
```
