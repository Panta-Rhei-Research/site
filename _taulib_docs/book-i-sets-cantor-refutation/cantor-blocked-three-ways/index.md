---
{
  "projection_kind": "taulib_declaration",
  "title": "cantor_blocked_three_ways",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/cantor-blocked-three-ways/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::cantor_blocked_three_ways",
  "declaration_slug": "cantor-blocked-three-ways",
  "kind": "theorem",
  "name": "cantor_blocked_three_ways",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 169,
  "source_line_end": 182,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L169-L182",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L169-L182",
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
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L169-L182)
- Source range: L169-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three failures are individually sufficient. -/
```

## Source Excerpt

```lean
theorem cantor_blocked_three_ways :
    -- P34: no extractor with avoiding diagonal
    (¬ exists (E : DecimalDiagonalExtractor),
      forall n, E.diagonal n ≠ E.extract n n) /\
    -- P35: no comprehension separator
    (¬ exists (Sep : ComprehensionSep),
      forall (P : TauIdx -> Prop) (a : TauIdx),
        tau_mem a (Sep P) <-> P a) /\
    -- P36: no nontrivial divisibility self-pairing
    (¬ exists (pair : TauIdx -> TauIdx),
      Function.Injective pair /\
      (forall n, pair n ≠ n) /\
      (forall n, n ∣ pair n)) :=
  ⟨no_unearned_decimal_diagonal, no_comprehension, no_free_cartesian_diagonal⟩
```
