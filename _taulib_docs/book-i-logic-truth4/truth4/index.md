---
{
  "projection_kind": "taulib_declaration",
  "title": "Truth4",
  "permalink": "/verify/taulib/docs/book-i-logic-truth4/truth4/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Logic.Truth4`.",
  "declaration_id": "TauLib.BookI.Logic.Truth4::Truth4",
  "declaration_slug": "truth4",
  "kind": "inductive",
  "name": "Truth4",
  "module_name": "TauLib.BookI.Logic.Truth4",
  "module_url": "/verify/taulib/docs/book-i-logic-truth4/",
  "source_line_start": 41,
  "source_line_end": 48,
  "registry_ids": [
    "I.D21"
  ],
  "related_registry_items": [
    {
      "id": "I.D21",
      "title": "Truth4 Logic",
      "url": "/registry/object/I.D21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L41-L48",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Truth4",
        "url": "/verify/taulib/docs/book-i-logic-truth4/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L41-L48",
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

- Module: [TauLib.BookI.Logic.Truth4](/verify/taulib/docs/book-i-logic-truth4/)
- Source path: [`TauLib/BookI/Logic/Truth4.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L41-L48)
- Source range: L41-L48
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D21` — Truth4 Logic

## Immediate Comment / Docstring

```lean
/-- [I.D21] The four truth values from bipolar evaluation.
    - T: both sectors confirm (overdetermined-true)
    - F: both sectors deny (underdetermined-false)
    - B: B-sector confirms, C-sector denies (overdetermined / "both")
    - N: neither sector confirms (underdetermined / "neither") -/
```

## Source Excerpt

```lean
inductive Truth4 where
  | T : Truth4
  | F : Truth4
  | B : Truth4
  | N : Truth4
  deriving DecidableEq, Repr, Inhabited

open Truth4
```
