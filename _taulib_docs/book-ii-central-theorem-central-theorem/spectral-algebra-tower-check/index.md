---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_algebra_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/spectral-algebra-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::spectral_algebra_tower_check",
  "declaration_slug": "spectral-algebra-tower-check",
  "kind": "def",
  "name": "spectral_algebra_tower_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 109,
  "source_line_end": 129,
  "registry_ids": [
    "II.D60"
  ],
  "related_registry_items": [
    {
      "id": "II.D60",
      "title": "Spectral Algebra",
      "url": "/registry/object/II.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L109-L129",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L109-L129",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L109-L129)
- Source range: L109-L129
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D60` — Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [II.D60] Spectral algebra tower check: the tower of spectral algebras
    forms an inverse system. The projection from stage k+1 to stage k
    is given by reduction:

    For sa at stage k+1, its restriction to stage k gives
    sa_restricted(x) = sa(reduce(x, k)).

    Verify: for the identity element, the restriction is consistent
    with the stage-k element. -/
```

## Source Excerpt

```lean
def spectral_algebra_tower_check (db bound : TauIdx) : Bool :=
  go 1 2 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      -- Stage-(k+1) spectral element: identity
      let sa_k1 : SpectralAlgebraElement := ⟨fun n => (n : Int), fun n => (n : Int)⟩
      -- Evaluate at stage k+1, then reduce to stage k
      let v_k1 := sa_k1.eval x (k + 1)
      let v_k1_b_reduced : Int := (reduce v_k1.b_sector.toNat k : Int)
      let v_k1_c_reduced : Int := (reduce v_k1.c_sector.toNat k : Int)
      -- Direct evaluation at stage k
      let sa_k : SpectralAlgebraElement := ⟨fun n => (n : Int), fun n => (n : Int)⟩
      let v_k := sa_k.eval x k
      -- Tower compatibility
      let tower_ok := v_k1_b_reduced == v_k.b_sector && v_k1_c_reduced == v_k.c_sector
      tower_ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
