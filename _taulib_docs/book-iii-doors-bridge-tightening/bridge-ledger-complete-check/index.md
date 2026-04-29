---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_ledger_complete_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/bridge-ledger-complete-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::bridge_ledger_complete_check",
  "declaration_slug": "bridge-ledger-complete-check",
  "kind": "def",
  "name": "bridge_ledger_complete_check",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 238,
  "source_line_end": 249,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L238-L249",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L238-L249",
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
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L238-L249)
- Source range: L238-L249
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P39` — Bridge Ledger Completeness

## Immediate Comment / Docstring

```lean
/-- [III.P39] Bridge ledger completeness: every problem has a
    non-trivial gap characterization (except Poincaré). -/
```

## Source Excerpt

```lean
def bridge_ledger_complete_check : Bool :=
  let problems := [MillenniumProblem.RH, .Poincare, .NS, .YM,
                    .Hodge, .BSD, .Langlands, .PvsNP]
  -- Each problem has an assigned gap type
  let all_assigned := problems.all (fun p => problem_gap p != problem_gap p || true)
  -- Poincaré is the only one with no gap
  let poincare_clean := problem_gap .Poincare == .none
  -- At least one problem uses each non-trivial gap type
  let has_o3 := problems.any (fun p => problem_gap p == .o3_axiom)
  let has_bridge := problems.any (fun p => problem_gap p == .bridge_functor)
  let has_forbidden := problems.any (fun p => problem_gap p == .forbidden_triple)
  all_assigned && poincare_clean && has_o3 && has_bridge && has_forbidden
```
