---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_instantiation_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/sector-instantiation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::sector_instantiation_check",
  "declaration_slug": "sector-instantiation-check",
  "kind": "def",
  "name": "sector_instantiation_check",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 88,
  "source_line_end": 117,
  "registry_ids": [
    "III.T41"
  ],
  "related_registry_items": [
    {
      "id": "III.T41",
      "title": "Hinge Theorem",
      "url": "/registry/object/III.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L88-L117",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L88-L117",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L88-L117)
- Source range: L88-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T41` — Hinge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T41] Sector instantiation check: at each enrichment level,
    the sector products are determined by the tower coherence.
    For k in 1..db: BNF at k decomposes into sector products,
    and these products are compatible across levels. -/
```

## Source Excerpt

```lean
def sector_instantiation_check (bound db : TauIdx) : Bool :=
  go 1 db (db + 1)
where
  go (k db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 then go (k + 1) db (fuel - 1)
      else
        -- B * C * X = Prim(k) at each level
        let euler_ok := split_zeta_b k * split_zeta_c k * split_zeta_x k == pk
        -- BNF decomposition covers all values
        let bnf_ok := bnf_check_at bound k
        euler_ok && bnf_ok && go (k + 1) db (fuel - 1)
  termination_by fuel
  /-- Check BNF at a single depth. -/
  bnf_check_at (bound k : Nat) : Bool :=
    bnf_at_go 0 bound k (bound + 1)
  bnf_at_go (x bound k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let pk := primorial k
      if pk == 0 then true
      else
        let nf := boundary_normal_form x k
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        sum == x % pk && bnf_at_go (x + 1) bound k (fuel - 1)
  termination_by fuel
```
