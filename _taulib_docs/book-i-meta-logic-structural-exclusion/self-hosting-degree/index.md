---
{
  "projection_kind": "taulib_declaration",
  "title": "SelfHostingDegree",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/self-hosting-degree/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.MetaLogic.StructuralExclusion`.",
  "declaration_id": "TauLib.BookI.MetaLogic.StructuralExclusion::SelfHostingDegree",
  "declaration_slug": "self-hosting-degree",
  "kind": "inductive",
  "name": "SelfHostingDegree",
  "module_name": "TauLib.BookI.MetaLogic.StructuralExclusion",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/",
  "source_line_start": 42,
  "source_line_end": 49,
  "registry_ids": [
    "I.D80"
  ],
  "related_registry_items": [
    {
      "id": "I.D80",
      "title": "Self-Hosting Degree Classification",
      "url": "/registry/object/I.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L42-L49",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.StructuralExclusion",
        "url": "/verify/taulib/docs/book-i-meta-logic-structural-exclusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L42-L49",
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

- Module: [TauLib.BookI.MetaLogic.StructuralExclusion](/verify/taulib/docs/book-i-meta-logic-structural-exclusion/)
- Source path: [`TauLib/BookI/MetaLogic/StructuralExclusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/StructuralExclusion.lean#L42-L49)
- Source range: L42-L49
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `I.D80` — Self-Hosting Degree Classification

## Immediate Comment / Docstring

```lean
/-- [I.D80] Self-hosting degrees classify how much of a formal system's
    meta-theory is internalized within the system itself.

    - `none`: no self-hosting — the system is formalized entirely externally
    - `partial_`: some constructions are internalized but the meta-theory remains external
    - `fragment`: significant portions of the meta-theory are internal, but gaps remain
    - `full`: complete self-hosting — meta-language and object language coincide -/
```

## Source Excerpt

```lean
inductive SelfHostingDegree where
  | none      -- E₀: external CIC substrate
  | partial_  -- E₁: τ-internal type theory
  | fragment  -- E₂: τ-internal proof theory
  | full      -- E₃: fully self-hosted
  deriving DecidableEq, Repr

open SelfHostingDegree
```
