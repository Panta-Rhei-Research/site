---
{
  "projection_kind": "taulib_declaration",
  "title": "simply_connected_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-poincare/simply-connected-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.Poincare`.",
  "declaration_id": "TauLib.BookIII.Doors.Poincare::simply_connected_check",
  "declaration_slug": "simply-connected-check",
  "kind": "def",
  "name": "simply_connected_check",
  "module_name": "TauLib.BookIII.Doors.Poincare",
  "module_url": "/verify/taulib/docs/book-iii-doors-poincare/",
  "source_line_start": 42,
  "source_line_end": 62,
  "registry_ids": [
    "III.D35"
  ],
  "related_registry_items": [
    {
      "id": "III.D35",
      "title": "Simply Connected in Category τ",
      "url": "/registry/object/III.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L42-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.Poincare",
        "url": "/verify/taulib/docs/book-iii-doors-poincare/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L42-L62",
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

- Module: [TauLib.BookIII.Doors.Poincare](/verify/taulib/docs/book-iii-doors-poincare/)
- Source path: [`TauLib/BookIII/Doors/Poincare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L42-L62)
- Source range: L42-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D35` — Simply Connected in Category τ

## Immediate Comment / Docstring

```lean
/-- [III.D35] Simple connectivity at finite level k: every "loop" at
    primorial level k is contractible, meaning the transition function
    around a cycle is the identity.
    In τ-terms: for every x and every prime cycle p₁→p₂→...→p₁,
    the CRT decomposition is consistent (no monodromy). -/
```

## Source Excerpt

```lean
def simply_connected_check (bound db : TauIdx) : Bool :=
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
        -- Contractibility: CRT decompose then reconstruct = identity
        let residues := crt_decompose (x % pk) k
        let reconstructed := crt_reconstruct residues k
        -- No monodromy: going around the CRT cycle returns to start
        let no_monodromy := reconstructed == x % pk
        -- BNF is well-defined (no ambiguity in decomposition)
        let nf := boundary_normal_form (x % pk) k
        let well_defined := (nf.b_part + nf.c_part + nf.x_part) % pk == x % pk
        no_monodromy && well_defined && go x (k + 1) (fuel - 1)
  termination_by fuel
```
