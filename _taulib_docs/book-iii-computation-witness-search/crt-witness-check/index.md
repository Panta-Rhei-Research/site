---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_witness_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/crt-witness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::crt_witness_check",
  "declaration_slug": "crt-witness-check",
  "kind": "def",
  "name": "crt_witness_check",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 85,
  "source_line_end": 103,
  "registry_ids": [
    "III.P22"
  ],
  "related_registry_items": [
    {
      "id": "III.P22",
      "title": "CRT Witness Decomposition",
      "url": "/registry/object/III.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L85-L103",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L85-L103",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L85-L103)
- Source range: L85-L103
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P22` — CRT Witness Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.P22] CRT witness decomposition: witness search at Prim(k)
    decomposes into independent per-prime searches. Each prime p_i
    contributes a search space of size p_i. -/
```

## Source Excerpt

```lean
def crt_witness_check (bound db : TauIdx) : Bool :=
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
        -- CRT decompose the witness
        let residues := crt_decompose (x % pk) k
        -- Reconstruct from per-prime residues
        let reconstructed := crt_reconstruct residues k
        -- Decomposition is faithful
        let faithful := reconstructed == x % pk
        faithful && go x (k + 1) (fuel - 1)
  termination_by fuel
```
