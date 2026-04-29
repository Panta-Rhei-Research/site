---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_algebra_stage_ring_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/spectral-algebra-stage-ring-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::spectral_algebra_stage_ring_check",
  "declaration_slug": "spectral-algebra-stage-ring-check",
  "kind": "def",
  "name": "spectral_algebra_stage_ring_check",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 77,
  "source_line_end": 98,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L77-L98",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L77-L98",
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
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L77-L98)
- Source range: L77-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D60` — Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [II.D60] Stage ring check: verify that spectral algebra elements
    form a ring at each stage. We check:
    - Pointwise addition is well-defined (periodic)
    - Pointwise multiplication is well-defined (periodic)
    - Idempotent support holds (always true for SectorPair) -/
```

## Source Excerpt

```lean
def spectral_algebra_stage_ring_check (k_max bound : TauIdx) : Bool :=
  go 1 2 ((k_max + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      let pk := primorial k
      -- Test spectral algebra element: sa(n) = (n, n+1) in SectorPair coords
      let sa : SpectralAlgebraElement := ⟨fun n => (n : Int), fun n => (n : Int) + 1⟩
      -- Periodicity: sa.eval(x, k) = sa.eval(x + P_k, k)
      let v1 := sa.eval x k
      let v2 := sa.eval (x + pk) k
      let periodic_ok := v1 == v2
      -- Idempotent support: e_plus * bp + e_minus * bp = bp
      let bp := v1
      let fp := SectorPair.mul e_plus_sector bp
      let fm := SectorPair.mul e_minus_sector bp
      let is_ok := SectorPair.add fp fm == bp
      periodic_ok && is_ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
