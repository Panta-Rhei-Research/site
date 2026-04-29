---
{
  "projection_kind": "taulib_declaration",
  "title": "bisquare_comparison_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/bisquare-comparison-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrichedBiSquare`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrichedBiSquare::bisquare_comparison_check",
  "declaration_slug": "bisquare-comparison-check",
  "kind": "def",
  "name": "bisquare_comparison_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/",
  "source_line_start": 110,
  "source_line_end": 135,
  "registry_ids": [
    "III.T39"
  ],
  "related_registry_items": [
    {
      "id": "III.T39",
      "title": "Enriched Bi-Square Comparison",
      "url": "/registry/object/III.T39/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L110-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L110-L135",
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
- Source path: [`TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L110-L135)
- Source range: L110-L135
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T39` — Enriched Bi-Square Comparison

## Immediate Comment / Docstring

```lean
/-- [III.T39] Bi-square comparison: the enriched bi-square (this) has the
    same shape as the algebraic (Book I) and topological (Book II) bi-squares.
    Shape = (left: tower coherence) × (right: spectral decomposition) with
    CRT pasting. Verified: all three check the same structural properties. -/
```

## Source Excerpt

```lean
def bisquare_comparison_check (bound db : TauIdx) : Bool :=
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
        -- Shape check 1: CRT roundtrip (same as algebraic bi-square)
        let residues := crt_decompose xr k
        let recon := crt_reconstruct residues k
        let shape1 := recon == xr
        -- Shape check 2: BNF decomposition (same as topological bi-square)
        let nf := boundary_normal_form xr k
        let shape2 := (nf.b_part + nf.c_part + nf.x_part) % pk == xr
        -- Shape check 3: sector products (enriched level)
        let bp := split_zeta_b k
        let cp := split_zeta_c k
        let xp := split_zeta_x k
        let shape3 := if pk > 0 then bp * cp * xp == pk else true
        shape1 && shape2 && shape3 && go x (k + 1) (fuel - 1)
  termination_by fuel
```
