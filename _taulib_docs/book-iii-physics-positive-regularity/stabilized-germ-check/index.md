---
{
  "projection_kind": "taulib_declaration",
  "title": "stabilized_germ_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/stabilized-germ-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::stabilized_germ_check",
  "declaration_slug": "stabilized-germ-check",
  "kind": "def",
  "name": "stabilized_germ_check",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 115,
  "source_line_end": 136,
  "registry_ids": [
    "III.D42"
  ],
  "related_registry_items": [
    {
      "id": "III.D42",
      "title": "Stabilized ω-Germ",
      "url": "/registry/object/III.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L115-L136",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/verify/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L115-L136",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L115-L136)
- Source range: L115-L136
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D42` — Stabilized ω-Germ

## Immediate Comment / Docstring

```lean
/-- [III.D42] Stabilized germ check: the germ at level db is consistent
    with all lower levels (tower projection commutes with BNF). -/
```

## Source Excerpt

```lean
def stabilized_germ_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      let pdb := primorial db
      if pk == 0 || pdb == 0 then go x (k + 1) (fuel - 1)
      else
        -- Stabilized germ at top level
        let germ_top := stabilized_germ x db
        let top_sum := (germ_top.b_part + germ_top.c_part + germ_top.x_part) % pdb
        -- Germ at level k
        let germ_k := boundary_normal_form (x % pk) k
        let k_sum := (germ_k.b_part + germ_k.c_part + germ_k.x_part) % pk
        -- Tower projection: top_sum mod pk == k_sum
        let coherent := top_sum % pk == k_sum
        coherent && go x (k + 1) (fuel - 1)
  termination_by fuel
```
