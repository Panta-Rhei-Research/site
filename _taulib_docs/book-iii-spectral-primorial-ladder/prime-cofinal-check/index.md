---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_cofinal_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/prime-cofinal-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.PrimorialLadder`.",
  "declaration_id": "TauLib.BookIII.Spectral.PrimorialLadder::prime_cofinal_check",
  "declaration_slug": "prime-cofinal-check",
  "kind": "def",
  "name": "prime_cofinal_check",
  "module_name": "TauLib.BookIII.Spectral.PrimorialLadder",
  "module_url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/",
  "source_line_start": 115,
  "source_line_end": 128,
  "registry_ids": [
    "III.T09"
  ],
  "related_registry_items": [
    {
      "id": "III.T09",
      "title": "Primorial Cofinality",
      "url": "/registry/object/III.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L115-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.PrimorialLadder",
        "url": "/verify/taulib/docs/book-iii-spectral-primorial-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L115-L128",
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

- Module: [TauLib.BookIII.Spectral.PrimorialLadder](/verify/taulib/docs/book-iii-spectral-primorial-ladder/)
- Source path: [`TauLib/BookIII/Spectral/PrimorialLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/PrimorialLadder.lean#L115-L128)
- Source range: L115-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T09` — Primorial Cofinality

## Immediate Comment / Docstring

```lean
/-- [III.T09] Cofinality for prime moduli: for each prime p ≤ bound,
    p | Prim(k) for some k. -/
```

## Source Excerpt

```lean
def prime_cofinal_check (bound : TauIdx) : Bool :=
  go 1 1 (bound + 1)
where
  go (i fuel : Nat) (_dummy : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else
      -- nth_prime i is the i-th prime (1-indexed)
      let p := nth_prime i
      if p > bound then true
      else
        -- p divides Prim(i) by construction
        primorial i % p == 0 && go (i + 1) (fuel - 1) 0
  termination_by fuel
```
