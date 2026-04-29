---
{
  "projection_kind": "taulib_declaration",
  "title": "GenerativeCountingPrinciple",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/generative-counting-principle/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::GenerativeCountingPrinciple",
  "declaration_slug": "generative-counting-principle",
  "kind": "structure",
  "name": "GenerativeCountingPrinciple",
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 49,
  "source_line_end": 57,
  "registry_ids": [
    "I.D75"
  ],
  "related_registry_items": [
    {
      "id": "I.D75",
      "title": "Generative Counting Principle",
      "url": "/registry/object/I.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L49-L57",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L49-L57",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L49-L57)
- Source range: L49-L57
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D75` — Generative Counting Principle

## Immediate Comment / Docstring

```lean
/-- [I.D75] The generative counting principle: the map phi_g(n) = (g, n)
    simultaneously creates the n-th orbit element and assigns it index n.
    This is a bijection between Nat and the orbit ray O_g. -/
```

## Source Excerpt

```lean
structure GenerativeCountingPrinciple (g : Generator) (hg : g ≠ omega) where
  /-- The creation-enumeration map: n maps to the n-th orbit element -/
  phi : Nat -> TauObj
  /-- phi is defined as depth-n in orbit g -/
  phi_def : forall n, phi n = TauObj.mk g n
  /-- phi is injective (distinct depths yield distinct objects) -/
  phi_injective : forall n m, phi n = phi m -> n = m
  /-- phi is surjective onto O_g (every orbit element has a depth) -/
  phi_surjective : forall x, OrbitRay g x -> exists n, phi n = x
```
