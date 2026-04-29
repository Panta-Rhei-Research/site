---
{
  "projection_kind": "taulib_declaration",
  "title": "finite_factorization_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/finite-factorization-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrichedBiSquare`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrichedBiSquare::finite_factorization_check",
  "declaration_slug": "finite-factorization-check",
  "kind": "def",
  "name": "finite_factorization_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/",
  "source_line_start": 44,
  "source_line_end": 66,
  "registry_ids": [
    "III.T38"
  ],
  "related_registry_items": [
    {
      "id": "III.T38",
      "title": "Finite Factorization Pasting",
      "url": "/registry/object/III.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L44-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
        "url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L44-L66",
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

- Module: [TauLib.BookIII.Arithmetic.EnrichedBiSquare](/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/)
- Source path: [`TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L44-L66)
- Source range: L44-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T38` — Finite Factorization Pasting

## Immediate Comment / Docstring

```lean
/-- [III.T38] Finite factorization: every element decomposes via CRT into
    per-prime factors, and this decomposition is the bi-square pasting map.
    α_p ∧ α_q = α_{p×q} at the sector level. -/
```

## Source Excerpt

```lean
def finite_factorization_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        let xr := x % pk
        -- CRT factorization
        let residues := crt_decompose xr k
        let reconstructed := crt_reconstruct residues k
        -- Finite factorization: reconstruct = original
        let factored := reconstructed == xr
        -- Pasting: BNF of reconstructed = BNF of original
        let nf_orig := boundary_normal_form xr k
        let nf_recon := boundary_normal_form reconstructed k
        let pasted := nf_orig == nf_recon
        factored && pasted && go x (k + 1) (fuel - 1)
  termination_by fuel
```
