---
{
  "projection_kind": "taulib_declaration",
  "title": "parseval_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-decomp/parseval-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::parseval_check",
  "declaration_slug": "parseval-check",
  "kind": "def",
  "name": "parseval_check",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 141,
  "source_line_end": 165,
  "registry_ids": [
    "III.T56"
  ],
  "related_registry_items": [
    {
      "id": "III.T56",
      "title": "Parseval Identity",
      "url": "/registry/object/III.T56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L141-L165",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L141-L165",
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
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L141-L165)
- Source range: L141-L165
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T56` — Parseval Identity

## Immediate Comment / Docstring

```lean
/-- [III.T56] Parseval identity: ‖f‖² = Σ_n |c_n|² where c_n = f(n).
    For the indicator basis, ‖f‖² = Σ_x f(x)² and Σ_n c_n² = Σ_n f(n)².
    These are the same sum — Parseval is an identity. -/
```

## Source Excerpt

```lean
def parseval_check (N : Nat) : Bool :=
  go_f 0 N N
where
  go_f (seed bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if seed >= 4 then true
    else
      -- Test function: f(x) = x + seed
      let f : Nat → Int := fun x => (x + seed : Int)
      -- LHS: ‖f‖² = Σ_x f(x)²
      let lhs := sum_sq f 0 bound (0 : Int)
      -- RHS: Σ_n |c_n|² = Σ_n f(n)² (same in indicator basis)
      let rhs := sum_coeff_sq f 0 bound (0 : Int) bound
      (lhs == rhs) && go_f (seed + 1) bound (fuel - 1)
  termination_by fuel
  sum_sq (f : Nat → Int) (x bound : Nat) (acc : Int) : Int :=
    if x >= bound then acc
    else sum_sq f (x + 1) bound (acc + f x * f x)
  termination_by bound - x
  sum_coeff_sq (f : Nat → Int) (n bound : Nat) (acc : Int) (N : Nat) : Int :=
    if n >= bound then acc
    else
      let cn := if n < N then f n else 0
      sum_coeff_sq f (n + 1) bound (acc + cn * cn) N
  termination_by bound - n
```
