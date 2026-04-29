---
{
  "projection_kind": "taulib_declaration",
  "title": "no_free_parameters_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/no-free-parameters-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::no_free_parameters_check",
  "declaration_slug": "no-free-parameters-check",
  "kind": "def",
  "name": "no_free_parameters_check",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 219,
  "source_line_end": 243,
  "registry_ids": [
    "III.T42"
  ],
  "related_registry_items": [
    {
      "id": "III.T42",
      "title": "No Knobs Theorem",
      "url": "/registry/object/III.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L219-L243",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L219-L243",
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
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L219-L243)
- Source range: L219-L243
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T42` — No Knobs Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T42] No free parameters: all sector products are derivable from
    the primorial tower, which is itself uniquely determined by the primes.
    The primes are fixed by K0-K6. Hence: no knobs. -/
```

## Source Excerpt

```lean
def no_free_parameters_check (bound db : TauIdx) : Bool :=
  go 0 1 bound db ((bound + 1) * (db + 1))
where
  go (x k bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 bound db (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) bound db (fuel - 1)
      else
        -- Value is uniquely determined by reduce
        let val := reduce x k
        -- BNF is uniquely determined by val
        let nf := boundary_normal_form val k
        -- Sector products are uniquely determined by BNF
        let bp := split_zeta_b k
        let cp := split_zeta_c k
        let xp := split_zeta_x k
        -- Total product = Prim(k) (no free parameter)
        let determined := if pk > 0 then bp * cp * xp == pk else true
        -- BNF is consistent
        let consistent := (nf.b_part + nf.c_part + nf.x_part) % pk == val
        determined && consistent && go x (k + 1) bound db (fuel - 1)
  termination_by fuel
```
