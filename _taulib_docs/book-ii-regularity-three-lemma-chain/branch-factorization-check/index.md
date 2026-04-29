---
{
  "projection_kind": "taulib_declaration",
  "title": "branch_factorization_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/branch-factorization-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::branch_factorization_check",
  "declaration_slug": "branch-factorization-check",
  "kind": "def",
  "name": "branch_factorization_check",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 58,
  "source_line_end": 79,
  "registry_ids": [
    "II.L08"
  ],
  "related_registry_items": [
    {
      "id": "II.L08",
      "title": "Branch Factorization",
      "url": "/registry/object/II.L08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L58-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.ThreeLemmaChain",
        "url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L58-L79",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L58-L79)
- Source range: L58-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L08` — Branch Factorization

## Immediate Comment / Docstring

```lean
/-- [II.L08] Branch factorization of the evolution operator output.
    For each point x and stages n, m: the evolution_op output decomposes
    via the idempotent decomposition into independent B and C branches.

    Specifically: the SectorPair formed from the ABCD chart of the
    evolved point decomposes as e₊ · sp + e₋ · sp = sp. -/
```

## Source Excerpt

```lean
def branch_factorization_check (bound db : TauIdx) : Bool :=
  go 2 1 1 ((bound + 1) * (db + 1) * (db + 1))
where
  go (x n m fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if n > db then go (x + 1) 1 1 (fuel - 1)
    else if m > db then go x (n + 1) 1 (fuel - 1)
    else
      -- Compute evolution output
      let evolved := evolution_op x n m
      -- Get ABCD chart and bipolar decomposition
      let p := from_tau_idx evolved
      let bp := interior_bipolar p
      -- Idempotent decomposition
      let (g_plus, g_minus) := idempotent_decompose bp
      -- Branch factorization: G = G₊ + G₋
      let recovery := SectorPair.add g_plus g_minus == bp
      -- Independence: G₊ and G₋ are orthogonal
      let ortho := SectorPair.mul g_plus g_minus == ⟨0, 0⟩
      recovery && ortho && go x n (m + 1) (fuel - 1)
  termination_by fuel
```
