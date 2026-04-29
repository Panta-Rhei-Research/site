---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_determines_interior_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/boundary-determines-interior-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.HartogsExtension`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.HartogsExtension::boundary_determines_interior_check",
  "declaration_slug": "boundary-determines-interior-check",
  "kind": "def",
  "name": "boundary_determines_interior_check",
  "module_name": "TauLib.BookII.CentralTheorem.HartogsExtension",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/",
  "source_line_start": 180,
  "source_line_end": 212,
  "registry_ids": [
    "II.T37"
  ],
  "related_registry_items": [
    {
      "id": "II.T37",
      "title": "Hartogs Extension Uniqueness",
      "url": "/registry/object/II.T37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L180-L212",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.HartogsExtension",
        "url": "/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L180-L212",
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

- Module: [TauLib.BookII.CentralTheorem.HartogsExtension](/verify/taulib/docs/book-ii-central-theorem-hartogs-extension/)
- Source path: [`TauLib/BookII/CentralTheorem/HartogsExtension.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/HartogsExtension.lean#L180-L212)
- Source range: L180-L212
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T37` — Hartogs Extension Uniqueness

## Immediate Comment / Docstring

```lean
/-- [II.T37] Boundary determines interior check: for any two "functions"
    that agree on the boundary (all stage reductions agree), they must
    agree everywhere.

    We verify this by checking that reduce(x, k) is determined by
    the sequence of reduce(x, j) for j <= k. Specifically:
    if reduce(x, k) = reduce(y, k) for all k <= db, then x and y
    agree at all stages. -/
```

## Source Excerpt

```lean
def boundary_determines_interior_check (bound db : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      -- Check: if all stage reductions agree, then bndlift values agree
      let all_stages_agree := stages_agree x y 1 (db + 1)
      if all_stages_agree then
        -- If all stages agree, bndlift values must also agree
        let lifts_ok := lifts_agree x y 1 (db + 1)
        -- Additionally: Code extraction via bndlift produces same result
        -- (exercises Code/Decode pathway alongside direct lift comparison)
        let bnd_fn : TauIdx → Int := fun n => (bndlift n 1 : Int)
        let code_ok := db < 2 ||
          code_extract bnd_fn 2 x == code_extract bnd_fn 2 y
        lifts_ok && code_ok && go x (y + 1) (fuel - 1)
      else
        -- no constraint if they don't agree
        go x (y + 1) (fuel - 1)
  termination_by fuel
  stages_agree (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else (reduce x k == reduce y k) && stages_agree x y (k + 1) (fuel - 1)
  termination_by fuel
  lifts_agree (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else (bndlift x k == bndlift y k) && lifts_agree x y (k + 1) (fuel - 1)
  termination_by fuel
```
