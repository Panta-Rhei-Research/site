---
{
  "projection_kind": "taulib_declaration",
  "title": "self_pairing_trivial_or_blocked",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/self-pairing-trivial-or-blocked/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::self_pairing_trivial_or_blocked",
  "declaration_slug": "self-pairing-trivial-or-blocked",
  "kind": "theorem",
  "name": "self_pairing_trivial_or_blocked",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 127,
  "source_line_end": 134,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L127-L134",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L127-L134",
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
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L127-L134)
- Source range: L127-L134
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Stronger: even without the divisibility constraint, any self-pairing
    that maps n to an index encoding (n, n) must have pair(n) >= n for the
    pairing to be recoverable. The only injective map with pair(n) = n
    for all n is the identity, which is trivial (doesn't help the argument). -/
```

## Source Excerpt

```lean
theorem self_pairing_trivial_or_blocked :
    forall (pair : TauIdx -> TauIdx),
      Function.Injective pair ->
      (forall n, n ∣ pair n) ->
      pair 0 = 0 := by
  intro pair _ hdvd
  obtain ⟨m, hm⟩ := hdvd 0
  simp at hm; exact hm
```
