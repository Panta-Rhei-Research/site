---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_resolution_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-decomp/spectral-resolution-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::spectral_resolution_check",
  "declaration_slug": "spectral-resolution-check",
  "kind": "def",
  "name": "spectral_resolution_check",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 175,
  "source_line_end": 201,
  "registry_ids": [
    "III.P48"
  ],
  "related_registry_items": [
    {
      "id": "III.P48",
      "title": "ABC Gap Characterization",
      "url": "/registry/object/III.P48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L175-L201",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L175-L201",
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/verify/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L175-L201)
- Source range: L175-L201
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P48` — ABC Gap Characterization

## Immediate Comment / Docstring

```lean
/-- [III.P48] Spectral resolution: H_L = Σ_n λ_n P_n.
    Check: (Σ_n λ_n P_n)(f)(x) = H_L(f)(x) for test functions.
    For the discrete Laplacian, H_L(f)(x) = λ_x · f(x) in the eigenbasis.
    In the indicator basis, this is just f(x) · x². -/
```

## Source Excerpt

```lean
def spectral_resolution_check (N : Nat) : Bool :=
  go_f 0 N N
where
  go_f (seed bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if seed >= 4 then true
    else
      let f : Nat → Int := fun x => (x + seed : Int)
      go_x seed 0 bound bound f && go_f (seed + 1) bound (fuel - 1)
  termination_by fuel
  go_x (seed x bound fuel : Nat) (f : Nat → Int) : Bool :=
    if fuel = 0 then true
    else if x >= bound then true
    else
      -- LHS: H_L(f)(x) = x² · f(x) (diagonal in eigenbasis)
      let hlf := (lemniscate_eigenvalue x : Int) * f x
      -- RHS: Σ_n λ_n · P_n(f)(x) = λ_x · f(x) (only n=x contributes)
      let resolved := sum_projectors f x 0 bound (0 : Int) bound
      (hlf == resolved) && go_x seed (x + 1) bound (fuel - 1) f
  termination_by fuel
  sum_projectors (f : Nat → Int) (x n bound : Nat) (acc : Int) (N : Nat) : Int :=
    if n >= bound then acc
    else
      let pn_val := spectral_projector n f N x
      let lambda_n := (lemniscate_eigenvalue n : Int)
      sum_projectors f x (n + 1) bound (acc + lambda_n * pn_val) N
  termination_by bound - n
```
