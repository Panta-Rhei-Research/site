---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_admissible_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/tau-admissible-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::tau_admissible_check",
  "declaration_slug": "tau-admissible-check",
  "kind": "def",
  "name": "tau_admissible_check",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 83,
  "source_line_end": 106,
  "registry_ids": [
    "III.D54"
  ],
  "related_registry_items": [
    {
      "id": "III.D54",
      "title": "τ-Admissibility (E₂)",
      "url": "/registry/object/III.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L83-L106",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.Admissibility",
        "url": "/verify/taulib/docs/book-iii-computation-admissibility/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L83-L106",
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

- Module: [TauLib.BookIII.Computation.Admissibility](/verify/taulib/docs/book-iii-computation-admissibility/)
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L83-L106)
- Source range: L83-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D54` — τ-Admissibility (E₂)

## Immediate Comment / Docstring

```lean
/-- [III.D54] τ-admissibility at E₂: a computation is τ-admissible if
    its interface width is finite. At the finite level, we check that
    the width is bounded by db. -/
```

## Source Excerpt

```lean
def tau_admissible_check (bound db : TauIdx) : Bool :=
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
        -- Run TTM at this depth
        let xr := x % pk
        let cfg := ttm_run (TTMConfig.mk 0 xr 1 k) 4
        -- Result is valid
        let valid := cfg.reg_a < pk
        -- BNF idempotence on result: BNF(BNF(result)) == BNF(result)
        let nf1 := boundary_normal_form cfg.reg_a k
        let s1 := (nf1.b_part + nf1.c_part + nf1.x_part) % pk
        let nf2 := boundary_normal_form s1 k
        let s2 := (nf2.b_part + nf2.c_part + nf2.x_part) % pk
        let idem_ok := s1 == s2
        valid && idem_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
