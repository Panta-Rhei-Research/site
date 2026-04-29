---
{
  "projection_kind": "taulib_declaration",
  "title": "operational_closure_full_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/operational-closure-full-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::operational_closure_full_check",
  "declaration_slug": "operational-closure-full-check",
  "kind": "def",
  "name": "operational_closure_full_check",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 147,
  "source_line_end": 171,
  "registry_ids": [
    "III.T57"
  ],
  "related_registry_items": [
    {
      "id": "III.T57",
      "title": "Operational Closure Theorem",
      "url": "/registry/object/III.T57/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L147-L171",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L147-L171",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L147-L171)
- Source range: L147-L171
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T57` — Operational Closure Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T57] Full operational closure: every code-decode cycle
    produces a valid E₂ carrier element. -/
```

## Source Excerpt

```lean
def operational_closure_full_check (bound db : Nat) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (c k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if c > bound then true
    else if k > db then go (c + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go c (k + 1) (fuel - 1)
      else
        let cr := c % pk
        -- Decode step: apply each possible decoder
        go_d cr 0 pk k fuel && go c (k + 1) (fuel - 1)
  termination_by fuel
  go_d (c d pk k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if d >= pk then true
    else
      let result := (c + d) % pk
      -- Result is valid E₂ carrier: result < pk and reduce-stable
      let valid := result < pk
      let stable := reduce result k == result
      valid && stable && go_d c (d + 1) pk k (fuel - 1)
  termination_by fuel
```
