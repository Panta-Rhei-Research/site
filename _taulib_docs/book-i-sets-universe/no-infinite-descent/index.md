---
{
  "projection_kind": "taulib_declaration",
  "title": "no_infinite_descent",
  "permalink": "/verify/taulib/docs/book-i-sets-universe/no-infinite-descent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Universe`.",
  "declaration_id": "TauLib.BookI.Sets.Universe::no_infinite_descent",
  "declaration_slug": "no-infinite-descent",
  "kind": "theorem",
  "name": "no_infinite_descent",
  "module_name": "TauLib.BookI.Sets.Universe",
  "module_url": "/verify/taulib/docs/book-i-sets-universe/",
  "source_line_start": 101,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L101-L128",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Universe",
        "url": "/verify/taulib/docs/book-i-sets-universe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L101-L128",
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

- Module: [TauLib.BookI.Sets.Universe](/verify/taulib/docs/book-i-sets-universe/)
- Source path: [`TauLib/BookI/Sets/Universe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Universe.lean#L101-L128)
- Source range: L101-L128
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P13c] No Infinite Descent: there is no infinite descending
    chain of strict τ-membership through nonzero elements.

    Proof: from well-foundedness of tau_strict_mem_nz. An infinite
    descending chain would contradict the well-foundedness of the
    relation, since it would produce a sequence with no minimal element. -/
```

## Source Excerpt

```lean
theorem no_infinite_descent : ¬ ∃ f : Nat → TauIdx, is_descending_chain f := by
  intro ⟨f, hchain⟩
  have hwf := tau_strict_mem_wf
  -- Extract the accessibility predicate at f 0
  have hacc : Acc tau_strict_mem_nz (f 0) := hwf.apply (f 0)
  -- Show by induction that f n is accessible for all n, but the chain never terminates
  suffices ∀ n : Nat, Acc tau_strict_mem_nz (f n) by
    -- Build a descending sequence witnessing non-well-foundedness
    -- Actually, we use the fact that Acc is well-founded induction:
    -- if f(n) is accessible and f(n+1) < f(n), then f(n+1) is also accessible.
    -- But this just shows all are accessible — we need to show the chain
    -- contradicts accessibility directly.
    exact absurd hwf (by
      intro hwf'
      -- A well-founded relation has no infinite descending chain.
      -- We build the contradiction by strong induction.
      have : ∀ a : TauIdx, Acc tau_strict_mem_nz a → ∀ g : Nat → TauIdx,
          g 0 = a → (∀ n, tau_strict_mem_nz (g (n + 1)) (g n)) → False := by
        intro a hacc
        induction hacc with
        | intro x _ ih =>
          intro g hg0 hg
          exact ih (g 1) (hg0 ▸ hg 0) (fun n => g (n + 1)) rfl (fun n => hg (n + 1))
      exact this (f 0) (hwf'.apply (f 0)) f rfl hchain)
  intro n
  induction n with
  | zero => exact hacc
  | succ n ih => exact ih.inv (hchain n)
```
