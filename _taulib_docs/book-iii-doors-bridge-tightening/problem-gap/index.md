---
{
  "projection_kind": "taulib_declaration",
  "title": "problem_gap",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/problem-gap/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::problem_gap",
  "declaration_slug": "problem-gap",
  "kind": "def",
  "name": "problem_gap",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 225,
  "source_line_end": 234,
  "registry_ids": [
    "III.P39"
  ],
  "related_registry_items": [
    {
      "id": "III.P39",
      "title": "Bridge Ledger Completeness",
      "url": "/registry/object/III.P39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L225-L234",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L225-L234",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L225-L234)
- Source range: L225-L234
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P39` — Bridge Ledger Completeness

## Immediate Comment / Docstring

```lean
/-- [III.P39] Gap classification per problem. -/
```

## Source Excerpt

```lean
def problem_gap (p : MillenniumProblem) : GapType :=
  match p with
  | .RH => .o3_axiom
  | .Poincare => .none
  | .NS => .bridge_functor
  | .YM => .bridge_functor
  | .Hodge => .bridge_functor
  | .BSD => .bridge_functor
  | .Langlands => .bridge_functor
  | .PvsNP => .forbidden_triple
```
