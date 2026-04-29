---
{
  "projection_kind": "taulib_declaration",
  "title": "enriched_bisquare_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/enriched-bisquare-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.EnrichedBiSquare`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrichedBiSquare::enriched_bisquare_check",
  "declaration_slug": "enriched-bisquare-check",
  "kind": "def",
  "name": "enriched_bisquare_check",
  "module_name": "TauLib.BookIII.Arithmetic.EnrichedBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enriched-bi-square/",
  "source_line_start": 75,
  "source_line_end": 100,
  "registry_ids": [
    "III.D65"
  ],
  "related_registry_items": [
    {
      "id": "III.D65",
      "title": "Enriched Bi-Square at E₁⁺",
      "url": "/registry/object/III.D65/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L75-L100",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L75-L100",
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
- Source path: [`TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrichedBiSquare.lean#L75-L100)
- Source range: L75-L100
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D65` — Enriched Bi-Square at E₁⁺

## Immediate Comment / Docstring

```lean
/-- [III.D65] Enriched bi-square check: left face = sector-coupled tower
    coherence (BNF at k+1 projects to BNF at k), right face = Langlands
    functoriality (sector morphisms commute with spectral decomposition). -/
```

## Source Excerpt

```lean
def enriched_bisquare_check (bound db : TauIdx) : Bool :=
  -- Left face: tower coherence with sector coupling
  let left := tower_sector_go 0 1 bound db ((bound + 1) * (db + 1))
  -- Right face: functoriality
  let right := functoriality_check bound db
  -- Pasting: CRT = finite factorization
  let paste := finite_factorization_check bound db
  left && right && paste
where
  /-- Left face: BNF tower coherence with sector products. -/
  tower_sector_go (x k bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then tower_sector_go (x + 1) 1 bound db (fuel - 1)
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      if pk == 0 || pk1 == 0 then tower_sector_go x (k + 1) bound db (fuel - 1)
      else
        -- BNF at k+1 projects to BNF at k
        let nf_k := boundary_normal_form (x % pk) k
        let nf_k1 := boundary_normal_form (x % pk1) (k + 1)
        let sum_k := (nf_k.b_part + nf_k.c_part + nf_k.x_part) % pk
        let sum_k1 := (nf_k1.b_part + nf_k1.c_part + nf_k1.x_part) % pk
        sum_k == x % pk && sum_k1 == x % pk && tower_sector_go x (k + 1) bound db (fuel - 1)
  termination_by fuel
```
