---
{
  "projection_kind": "taulib_declaration",
  "title": "godel_i_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-incompleteness/godel-i-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.Incompleteness`.",
  "declaration_id": "TauLib.BookIII.Bridge.Incompleteness::godel_i_check",
  "declaration_slug": "godel-i-check",
  "kind": "def",
  "name": "godel_i_check",
  "module_name": "TauLib.BookIII.Bridge.Incompleteness",
  "module_url": "/verify/taulib/docs/book-iii-bridge-incompleteness/",
  "source_line_start": 107,
  "source_line_end": 128,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L107-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L107-L128",
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
- Source path: [`TauLib/BookIII/Bridge/Incompleteness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/Incompleteness.lean#L107-L128)
- Source range: L107-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T44` — Incompleteness as VM Boundary

## Immediate Comment / Docstring

```lean
/-- [III.T44] Godel I finite model: the Godel sentence at depth k is
    a valid code, but its "truth" (reduce-stability) and its "provability"
    (diagonal self-reference) can diverge. -/
```

## Source Excerpt

```lean
def godel_i_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 then go (k + 1) (fuel - 1)
      else
        let g := godel_sentence k
        -- G is a valid code at depth k
        let valid := g < pk
        -- G's diagonal is also valid
        let d_g := diagonal g k
        let d_valid := d_g < pk
        -- The divergence: G and d(G) are different codes
        -- (self-reference produces a different residue)
        -- This models "the Godel sentence differs from its own proof"
        let diverges := g != d_g || pk <= 3  -- trivially equal for very small pk
        valid && d_valid && diverges && go (k + 1) (fuel - 1)
  termination_by fuel
```
