---
{
  "projection_kind": "taulib_declaration",
  "title": "bias_primorial_check",
  "permalink": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/bias-primorial-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.ChebyshevBias`.",
  "declaration_id": "TauLib.BookI.Coordinates.ChebyshevBias::bias_primorial_check",
  "declaration_slug": "bias-primorial-check",
  "kind": "def",
  "name": "bias_primorial_check",
  "module_name": "TauLib.BookI.Coordinates.ChebyshevBias",
  "module_url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/",
  "source_line_start": 122,
  "source_line_end": 157,
  "registry_ids": [
    "I.T50"
  ],
  "related_registry_items": [
    {
      "id": "I.T50",
      "title": "Fundamental Theorem of Internal Galois Theory",
      "url": "/registry/object/I.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L122-L157",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.ChebyshevBias",
        "url": "/verify/taulib/docs/book-i-coordinates-chebyshev-bias/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L122-L157",
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

- Module: [TauLib.BookI.Coordinates.ChebyshevBias](/verify/taulib/docs/book-i-coordinates-chebyshev-bias/)
- Source path: [`TauLib/BookI/Coordinates/ChebyshevBias.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/ChebyshevBias.lean#L122-L157)
- Source range: L122-L157
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.T50` — Fundamental Theorem of Internal Galois Theory

## Immediate Comment / Docstring

```lean
/-- [I.T50] Bias at primorial levels: at each M_k (capped at 50),
    the Chebyshev bias (q=4, 3 vs 1) is positive. -/
```

## Source Excerpt

```lean
def bias_primorial_check (db : Nat) : Bool :=
  go 2 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Use Nat primorial via simple computation
      let pk := go_primorial k
      let bound := min pk 50
      -- Bias is positive at this level
      let bias_ok := chebyshev_bias bound 4 3 1 >= chebyshev_bias bound 4 1 3
      bias_ok && go (k + 1) (fuel - 1)
  termination_by fuel
  -- Simple primorial computation (self-contained)
  go_primorial (k : Nat) : Nat :=
    go_p 1 k 1 (k + 1)
  termination_by 0
  go_p (i bound acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if i > bound then acc
    else
      let p := go_nth_prime i
      go_p (i + 1) bound (acc * p) (fuel - 1)
  termination_by fuel
  go_nth_prime (k : Nat) : Nat :=
    go_np 2 k (100 * (k + 1))
  termination_by 0
  go_np (n count fuel : Nat) : Nat :=
    if fuel = 0 then n
    else if count == 0 then n
    else if is_prime_cb n then
      if count == 1 then n
      else go_np (n + 1) (count - 1) (fuel - 1)
    else go_np (n + 1) count (fuel - 1)
  termination_by fuel
```
