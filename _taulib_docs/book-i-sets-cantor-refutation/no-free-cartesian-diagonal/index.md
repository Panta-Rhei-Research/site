---
{
  "projection_kind": "taulib_declaration",
  "title": "no_free_cartesian_diagonal",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/no-free-cartesian-diagonal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::no_free_cartesian_diagonal",
  "declaration_slug": "no-free-cartesian-diagonal",
  "kind": "theorem",
  "name": "no_free_cartesian_diagonal",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 110,
  "source_line_end": 121,
  "registry_ids": [
    "I.P36"
  ],
  "related_registry_items": [
    {
      "id": "I.P36",
      "title": "No Free Cartesian Diagonal",
      "url": "/registry/object/I.P36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L110-L121",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.CantorRefutation",
        "url": "/verify/taulib/docs/book-i-sets-cantor-refutation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L110-L121",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Sets.CantorRefutation](/verify/taulib/docs/book-i-sets-cantor-refutation/)
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L110-L121)
- Source range: L110-L121
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P36` — No Free Cartesian Diagonal

## Immediate Comment / Docstring

```lean
/-- The Cantor diagonal argument requires a self-pairing map
    pair : N -> N that encodes the "n-th element paired with itself"
    in a way that DIFFERS from n (so that digit modification can
    produce a new element).

    In tau-arithmetic, any map with n | pair(n) AND pair(n) != n
    fails at n = 0, since 0 | k implies k = 0.

    [I.P36] No nontrivial divisibility-respecting self-pairing exists. -/
```

## Source Excerpt

```lean
theorem no_free_cartesian_diagonal :
    ¬ exists (pair : TauIdx -> TauIdx),
      Function.Injective pair /\
      (forall n, pair n ≠ n) /\
      (forall n, n ∣ pair n) := by
  intro ⟨pair, _, hne, hdvd⟩
  -- pair(0): 0 | pair(0) means pair(0) = 0
  have h0 : pair 0 = 0 := by
    obtain ⟨m, hm⟩ := hdvd 0
    simp at hm; exact hm
  -- But pair(0) != 0 by the nontriviality condition
  exact hne 0 h0
```
