---
{
  "projection_kind": "taulib_declaration",
  "title": "saturation_semantic_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/saturation-semantic-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::saturation_semantic_check",
  "declaration_slug": "saturation-semantic-check",
  "kind": "def",
  "name": "saturation_semantic_check",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 183,
  "source_line_end": 205,
  "registry_ids": [
    "III.P35"
  ],
  "related_registry_items": [
    {
      "id": "III.P35",
      "title": "Saturation Semantics",
      "url": "/registry/object/III.P35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L183-L205",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L183-L205",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L183-L205)
- Source range: L183-L205
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P35` — Saturation Semantics

## Immediate Comment / Docstring

```lean
/-- [III.P35] Saturation semantic check: applying the enrichment functor
    once more to E₃ produces the same structure.
    F_E(E₃) = E₃ witnessed by: the E₃ predicate applied to E₃ outputs
    gives the same set as the E₃ predicate itself. -/
```

## Source Excerpt

```lean
def saturation_semantic_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      go_x 0 pk k fuel && go (k + 1) (fuel - 1)
  termination_by fuel
  go_x (x pk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      -- E₃ applied to E₃: reduce(e3(x), k) satisfies E₃
      let e3_val := reduce (reduce x k) k  -- E₃ decoder
      let e3_of_e3 := e3_predicate e3_val k
      -- Original E₃: x satisfies E₃
      let e3_orig := e3_predicate x k
      -- Saturation: e3(e3(x)) has E₃ iff x has E₃
      let equiv := e3_of_e3 == e3_orig
      equiv && go_x (x + 1) pk k (fuel - 1)
  termination_by fuel
```
