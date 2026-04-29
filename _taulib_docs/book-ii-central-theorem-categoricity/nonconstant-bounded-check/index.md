---
{
  "projection_kind": "taulib_declaration",
  "title": "nonconstant_bounded_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/nonconstant-bounded-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::nonconstant_bounded_check",
  "declaration_slug": "nonconstant-bounded-check",
  "kind": "def",
  "name": "nonconstant_bounded_check",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 93,
  "source_line_end": 122,
  "registry_ids": [
    "II.T41"
  ],
  "related_registry_items": [
    {
      "id": "II.T41",
      "title": "Liouville Categorical Dodge",
      "url": "/registry/object/II.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L93-L122",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L93-L122",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L93-L122)
- Source range: L93-L122
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T41` — Liouville Categorical Dodge

## Immediate Comment / Docstring

```lean
/-- [II.T41] Nonconstant bounded holomorphic function check:
    exhibit a nonconstant bounded function on the primorial tower.

    The function f(x, k) = reduce(x, k) is:
    - Bounded: 0 <= f(x, k) < P_k for all x
    - Nonconstant: f(0, k) = 0 but f(1, k) = 1 for k >= 1
    - Tower-coherent: reduce(f(x, k+1), k) = reduce(reduce(x, k+1), k)
      = reduce(x, k) = f(x, k)

    This is IMPOSSIBLE in classical complex analysis (Liouville's theorem).
    It works here because j^2 = +1 (wave type) allows bounded nonconstant
    solutions to the wave equation. -/
```

## Source Excerpt

```lean
def nonconstant_bounded_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- f(x, k) = reduce(x, k) is bounded by P_k
      let bounded_ok := check_bounded k 0 pk (pk + 1)
      -- f is nonconstant: f(0, k) = 0, f(1, k) = 1 (for k >= 1, P_k >= 2)
      let nc_ok := if pk >= 2
        then reduce 0 k != reduce 1 k
        else true
      -- Tower coherence: reduce(f(x, k+1), k) = f(x, k)
      let tc_ok := check_tower_coherence k 0 20 21
      bounded_ok && nc_ok && tc_ok && go (k + 1) (fuel - 1)
  termination_by fuel
  check_bounded (k x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else (reduce x k < pk) && check_bounded k (x + 1) pk (fuel - 1)
  termination_by fuel
  check_tower_coherence (k x bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let tc := reduce (reduce x (k + 1)) k == reduce x k
      tc && check_tower_coherence k (x + 1) bound (fuel - 1)
  termination_by fuel
```
