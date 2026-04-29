---
{
  "projection_kind": "taulib_declaration",
  "title": "trichotomy_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/trichotomy-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::trichotomy_check",
  "declaration_slug": "trichotomy-check",
  "kind": "def",
  "name": "trichotomy_check",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 59,
  "source_line_end": 90,
  "registry_ids": [
    "III.T14"
  ],
  "related_registry_items": [
    {
      "id": "III.T14",
      "title": "Spectral Trichotomy Lemma",
      "url": "/registry/object/III.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L59-L90",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L59-L90",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L59-L90)
- Source range: L59-L90
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T14` — Spectral Trichotomy Lemma

## Immediate Comment / Docstring

```lean
/-- [III.T14] Spectral trichotomy check: verify that the B+C+X decomposition
    is exact (sums back to original) and orthogonal (cross-terms zero). -/
```

## Source Excerpt

```lean
def trichotomy_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let residues := crt_decompose x k
      let (b_part, c_part, x_part) := trichotomy_decompose residues k
      -- Exactness: b + c + x = original (component-wise mod p_i)
      let exact_ok := check_exact residues b_part c_part x_part 0 k
      -- Orthogonality: B and C parts are disjoint (non-overlapping support)
      let ortho_ok := check_ortho b_part c_part 0 k
      exact_ok && ortho_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
  check_exact (orig b_part c_part x_part : List TauIdx) (i k : Nat) : Bool :=
    if i >= k then true
    else
      let p := nth_prime (i + 1)
      let sum_i := if p > 0 then
        (b_part.getD i 0 + c_part.getD i 0 + x_part.getD i 0) % p
      else 0
      let orig_i := if p > 0 then orig.getD i 0 % p else 0
      sum_i == orig_i && check_exact orig b_part c_part x_part (i + 1) k
  check_ortho (b_part c_part : List TauIdx) (i k : Nat) : Bool :=
    if i >= k then true
    else
      -- At most one of b, c is nonzero at each position
      let bi := b_part.getD i 0
      let ci := c_part.getD i 0
      (bi == 0 || ci == 0) && check_ortho b_part c_part (i + 1) k
```
