---
{
  "projection_kind": "taulib_declaration",
  "title": "Ladder4Level",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-few/ladder4-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Orbit.TooFew`.",
  "declaration_id": "TauLib.BookI.Orbit.TooFew::Ladder4Level",
  "declaration_slug": "ladder4-level",
  "kind": "inductive",
  "name": "Ladder4Level",
  "module_name": "TauLib.BookI.Orbit.TooFew",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-few/",
  "source_line_start": 65,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L65-L70",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooFew",
        "url": "/verify/taulib/docs/book-i-orbit-too-few/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L65-L70",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookI.Orbit.TooFew](/verify/taulib/docs/book-i-orbit-too-few/)
- Source path: [`TauLib/BookI/Orbit/TooFew.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L65-L70)
- Source range: L65-L70
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 4 hyperoperation levels (same as Gen5, but channel assignment fails). -/
```

## Source Excerpt

```lean
inductive Ladder4Level : Type where
  | rho_level : Ladder4Level
  | add_level : Ladder4Level
  | mul_level : Ladder4Level
  | exp_level : Ladder4Level
  deriving DecidableEq, Repr
```
