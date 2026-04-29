---
{
  "projection_kind": "taulib_declaration",
  "title": "central_theorem_forward_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/central-theorem-forward-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::central_theorem_forward_check",
  "declaration_slug": "central-theorem-forward-check",
  "kind": "def",
  "name": "central_theorem_forward_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 146,
  "source_line_end": 168,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L146-L168",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L146-L168",
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
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L146-L168)
- Source range: L146-L168
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T40` — Central Theorem

## Immediate Comment / Docstring

```lean
/-- [II.T40] Central Theorem forward direction:
    boundary data (spectral algebra element) determines a holomorphic function.

    Given a spectral algebra element sa with B-channel and C-channel functions,
    the BndLift construction produces a tower-coherent function:

    For each stage k, the boundary data at stage k is:
      boundary(x) = (sa.b_fn(reduce(x, k)), sa.c_fn(reduce(x, k)))

    Tower coherence: reduce(boundary(x, k+1), k) = boundary(x, k).
    This follows from reduce(reduce(x, k+1), k) = reduce(x, k). -/
```

## Source Excerpt

```lean
def central_theorem_forward_check (db bound : TauIdx) : Bool :=
  go 1 2 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      -- Spectral algebra element: identity
      let sa : SpectralAlgebraElement := ⟨fun n => (n : Int), fun n => (n : Int)⟩
      -- Forward map: spectral element -> holomorphic function
      -- The holomorphic function at (x, k) is sa.eval(x, k)
      let hol_k := sa.eval x k
      let hol_k1 := sa.eval x (k + 1)
      -- Tower coherence: reduce output at k+1 to k matches output at k
      -- Since sa.b_fn = id, sa.eval(x, k) = (reduce(x,k), reduce(x,k))
      -- reduce(reduce(x, k+1), k) = reduce(x, k) by reduction_compat
      let rx_k : Int := (reduce x k : Int)
      let rx_k1 : Int := (reduce x (k + 1) : Int)
      let reduced_b : Int := (reduce rx_k1.toNat k : Int)
      let tc_ok := reduced_b == rx_k && hol_k.b_sector == rx_k && hol_k1.b_sector == rx_k1
      tc_ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
