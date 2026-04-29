---
{
  "projection_kind": "taulib_declaration",
  "title": "MillenniumProblem",
  "permalink": "/verify/taulib/docs/book-iii-doors-master-schema/millennium-problem/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Doors.MasterSchema`.",
  "declaration_id": "TauLib.BookIII.Doors.MasterSchema::MillenniumProblem",
  "declaration_slug": "millennium-problem",
  "kind": "inductive",
  "name": "MillenniumProblem",
  "module_name": "TauLib.BookIII.Doors.MasterSchema",
  "module_url": "/verify/taulib/docs/book-iii-doors-master-schema/",
  "source_line_start": 38,
  "source_line_end": 47,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L38-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.MasterSchema",
        "url": "/verify/taulib/docs/book-iii-doors-master-schema/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L38-L47",
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

- Module: [TauLib.BookIII.Doors.MasterSchema](/verify/taulib/docs/book-iii-doors-master-schema/)
- Source path: [`TauLib/BookIII/Doors/MasterSchema.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/MasterSchema.lean#L38-L47)
- Source range: L38-L47
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The eight Millennium Problems (including Langlands as the 8th force). -/
```

## Source Excerpt

```lean
inductive MillenniumProblem where
  | RH : MillenniumProblem           -- Riemann Hypothesis
  | Poincare : MillenniumProblem     -- Poincaré Conjecture
  | NS : MillenniumProblem           -- Navier-Stokes Existence
  | YM : MillenniumProblem           -- Yang-Mills Mass Gap
  | Hodge : MillenniumProblem        -- Hodge Conjecture
  | BSD : MillenniumProblem          -- Birch and Swinnerton-Dyer
  | Langlands : MillenniumProblem    -- Langlands Program
  | PvsNP : MillenniumProblem        -- P vs NP
  deriving Repr, DecidableEq, BEq
```
