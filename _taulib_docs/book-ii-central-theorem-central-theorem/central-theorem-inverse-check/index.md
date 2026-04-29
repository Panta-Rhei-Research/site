---
{
  "projection_kind": "taulib_declaration",
  "title": "central_theorem_inverse_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-theorem-inverse-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_theorem_inverse_check",
  "declaration_slug": "central-theorem-inverse-check",
  "kind": "def",
  "name": "central_theorem_inverse_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 181,
  "source_line_end": 204,
  "registry_ids": [
    "II.T40"
  ],
  "related_registry_items": [
    {
      "id": "II.T40",
      "title": "Central Theorem",
      "url": "/registry/object/II.T40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L181-L204",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L181-L204",
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
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L181-L204)
- Source range: L181-L204
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] Central Theorem inverse direction:
    every holomorphic function restricts to a boundary character
    (spectral algebra element).

    Given a tower-coherent StageFun f:
    - At each stage k, f(x, k) is well-defined on Z/P_kZ
    - The B-channel gives sa.b_fn, the C-channel gives sa.c_fn
    - Idempotent decomposition ensures sa is idempotent-supported

    Test: for id_stage (tower-coherent), the restriction to boundary
    data gives a well-defined spectral algebra element. -/
```

## Source Excerpt

```lean
def central_theorem_inverse_check (db bound : TauIdx) : Bool :=
  go 1 2 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      let pk := primorial k
      -- Holomorphic function: id_stage
      -- Restriction to boundary: B(x) = id_stage.b_fun(x, k) = reduce(x, k)
      let b_val := id_stage.b_fun x k
      let c_val := id_stage.c_fun x k
      -- The restriction is periodic: f(x, k) = f(x + P_k, k)
      let b_per := id_stage.b_fun (x + pk) k
      let c_per := id_stage.c_fun (x + pk) k
      let periodic_ok := b_val == b_per && c_val == c_per
      -- Idempotent support: the sector pair decomposes
      let bp : SectorPair := ⟨(b_val : Int), (c_val : Int)⟩
      let fp := SectorPair.mul e_plus_sector bp
      let fm := SectorPair.mul e_minus_sector bp
      let is_ok := SectorPair.add fp fm == bp
      periodic_ok && is_ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
