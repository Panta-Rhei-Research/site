---
{
  "projection_kind": "taulib_declaration",
  "title": "l_function_spectral_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/l-function-spectral-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::l_function_spectral_check",
  "declaration_slug": "l-function-spectral-check",
  "kind": "def",
  "name": "l_function_spectral_check",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 185,
  "source_line_end": 204,
  "registry_ids": [
    "III.D32"
  ],
  "related_registry_items": [
    {
      "id": "III.D32",
      "title": "L-Function as Spectral Determinant",
      "url": "/registry/object/III.D32/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L185-L204",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/verify/taulib/docs/book-iii-doors-grand-grh/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L185-L204",
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

- Module: [TauLib.BookIII.Doors.GrandGRH](/verify/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L185-L204)
- Source range: L185-L204
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D32` — L-Function as Spectral Determinant

## Immediate Comment / Docstring

```lean
/-- [III.D32] L-function as spectral determinant at finite level:
    L_{≤k}(s) = ∏_{p ≤ p_k} (1 - p^{-s})^{-1}.
    At τ-level: the finite Euler product equals the primorial when
    all factors are included, and decomposes via the B/C/X labels. -/
```

## Source Excerpt

```lean
def l_function_spectral_check (db : TauIdx) : Bool :=
  go 1 1 ((db + 1) * (db + 1))
where
  go (i k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else if i > k then
      -- All factors checked at depth k; verify Euler product
      let pk := primorial k
      let b := split_zeta_b k
      let c := split_zeta_c k
      let x := split_zeta_x k
      let det_ok := if pk > 0 then b * c * x == pk else true
      det_ok && go 1 (k + 1) (fuel - 1)
    else
      -- Check: factor p_i is prime
      let p := nth_prime i
      let ok := if p >= 2 then is_prime_naive p else true
      ok && go (i + 1) k (fuel - 1)
  termination_by fuel
```
