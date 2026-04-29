---
{
  "projection_kind": "taulib_declaration",
  "title": "no_uncountable_prerequisite",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/no-uncountable-prerequisite/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::no_uncountable_prerequisite",
  "declaration_slug": "no-uncountable-prerequisite",
  "kind": "def",
  "name": "no_uncountable_prerequisite",
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 141,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L141-L151",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.Counting",
        "url": "/verify/taulib/docs/book-i-sets-counting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L141-L151",
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

- Module: [TauLib.BookI.Sets.Counting](/verify/taulib/docs/book-i-sets-counting/)
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L141-L151)
- Source range: L141-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The three prerequisites for uncountability are not derivable from K0-K6.

    P1 (impredicative powerset): For any nonzero b, the tau-members of b
    are bounded by b (tau_mem_le), so the "powerset" at each level is finite.
    There is no single tau-index encoding "all subsets of Nat."

    P2 (unrestricted comprehension): The tau-set universe is exactly Nat;
    not every predicate on Nat corresponds to a tau-index. In particular,
    there is no R such that a in_tau R iff not(a in_tau a) (no_russell_set).

    P3 (free Cartesian diagonal): Self-pairing n |-> (n, n) requires a
    product encoding that is an earned morphism. But in Cat_tau (thin category),
    the diagonal map would need to factor through the product universal
    property, and the earned-arrow discipline prevents unrestricted self-reference. -/
```

## Source Excerpt

```lean
def no_uncountable_prerequisite : UncountablePrerequisites where
  no_impredicative_powerset :=
    -- Finite divisor sets: for any nonzero b, members are bounded
    forall (b : TauIdx), b ≠ 0 -> forall (a : TauIdx), tau_mem a b -> a ≤ b
  no_comprehension :=
    -- No Russell set: no R satisfies the comprehension schema
    ¬ exists (R : TauIdx), forall (a : TauIdx), tau_mem a R <-> ¬ tau_mem a R
  no_free_diagonal :=
    -- The thin category has at most one morphism between any two objects:
    -- a self-pairing morphism would violate thinness constraints
    True  -- witnessed by the earned-arrow discipline (Cat_tau is thin)
```
