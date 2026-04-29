---
{
  "projection_kind": "taulib_declaration",
  "title": "e2_e3_boundary_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-incompleteness/e2-e3-boundary-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.Incompleteness`.",
  "declaration_id": "TauLib.BookIII.Bridge.Incompleteness::e2_e3_boundary_check",
  "declaration_slug": "e2-e3-boundary-check",
  "kind": "def",
  "name": "e2_e3_boundary_check",
  "module_name": "TauLib.BookIII.Bridge.Incompleteness",
  "module_url": "/verify/taulib/docs/book-iii-bridge-incompleteness/",
  "source_line_start": 83,
  "source_line_end": 102,
  "registry_ids": [
    "III.T44"
  ],
  "related_registry_items": [
    {
      "id": "III.T44",
      "title": "Incompleteness as VM Boundary",
      "url": "/registry/object/III.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L83-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.Incompleteness",
        "url": "/verify/taulib/docs/book-iii-bridge-incompleteness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L83-L102",
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

- Module: [TauLib.BookIII.Bridge.Incompleteness](/verify/taulib/docs/book-iii-bridge-incompleteness/)
- Source path: [`TauLib/BookIII/Bridge/Incompleteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L83-L102)
- Source range: L83-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T44` — Incompleteness as VM Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T44] E2->E3 boundary detection: at each depth k, determine
    whether the diagonal self-reference "escapes" E2.

    The escape criterion: diagonal(diagonal(x, k), k) != diagonal(x, k)
    for the Godel sentence. This shows that self-reference applied twice
    (the analog of "this sentence talks about itself talking about itself")
    moves to a different residue class -- the E3 phenomenon.

    But: at the NEXT depth k+1, the two values may agree (the E3 level
    "sees" both). This is the boundary. -/
```

## Source Excerpt

```lean
def e2_e3_boundary_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        -- E2 self-reference: diagonal is well-defined
        let d_x := diagonal x k
        let d_d_x := diagonal d_x k
        -- Both are valid E2 codes (within primorial range)
        let e2_valid := d_x < pk && d_d_x < pk
        -- The diagonal is idempotent on reduce-stable elements
        let stable := reduce d_x k == d_x
        e2_valid && stable && go x (k + 1) (fuel - 1)
  termination_by fuel
```
