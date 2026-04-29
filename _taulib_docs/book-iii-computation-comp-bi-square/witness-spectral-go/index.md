---
{
  "projection_kind": "taulib_declaration",
  "title": "witness_spectral_go",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/witness-spectral-go/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::witness_spectral_go",
  "declaration_slug": "witness-spectral-go",
  "kind": "def",
  "name": "witness_spectral_go",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 95,
  "source_line_end": 109,
  "registry_ids": [
    "III.D56"
  ],
  "related_registry_items": [
    {
      "id": "III.D56",
      "title": "Computational Bi-Square",
      "url": "/registry/object/III.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L95-L109",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L95-L109",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L95-L109)
- Source range: L95-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D56` — Computational Bi-Square

## Immediate Comment / Docstring

```lean
/-- [III.D56] Witness spectral naturality: CRT decomposition commutes
    with BNF (same structural property as algebraic/topological bi-squares). -/
```

## Source Excerpt

```lean
def witness_spectral_go (x k bound db fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if x > bound then true
  else if k > db then witness_spectral_go (x + 1) 1 bound db (fuel - 1)
  else
    let pk := primorial k
    if pk == 0 then witness_spectral_go x (k + 1) bound db (fuel - 1)
    else
      let xr := x % pk
      let nf := boundary_normal_form xr k
      let residues := crt_decompose xr k
      let reconstructed := crt_reconstruct residues k
      let nf2 := boundary_normal_form reconstructed k
      nf == nf2 && witness_spectral_go x (k + 1) bound db (fuel - 1)
termination_by fuel
```
