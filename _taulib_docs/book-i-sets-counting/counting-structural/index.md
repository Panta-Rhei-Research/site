---
{
  "projection_kind": "taulib_declaration",
  "title": "counting_structural",
  "permalink": "/verify/taulib/docs/book-i-sets-counting/counting-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.Counting`.",
  "declaration_id": "TauLib.BookI.Sets.Counting::counting_structural",
  "declaration_slug": "counting-structural",
  "kind": "theorem",
  "name": "counting_structural",
  "module_name": "TauLib.BookI.Sets.Counting",
  "module_url": "/verify/taulib/docs/book-i-sets-counting/",
  "source_line_start": 84,
  "source_line_end": 93,
  "registry_ids": [
    "I.P33"
  ],
  "related_registry_items": [
    {
      "id": "I.P33",
      "title": "Counting as Structural Feature",
      "url": "/registry/object/I.P33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L84-L93",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L84-L93",
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

- Module: [TauLib.BookI.Sets.Counting](/verify/taulib/docs/book-i-sets-counting/)
- Source path: [`TauLib/BookI/Sets/Counting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/Counting.lean#L84-L93)
- Source range: L84-L93
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P33` — Counting as Structural Feature

## Immediate Comment / Docstring

```lean
/-- [I.P33] Countability of Obj(tau) as a structural feature:
    it follows from generative counting (each orbit is counted)
    plus ontic closure (the universe is a finite union of orbits).

    The injection TauObj -> Nat witnesses countability. -/
```

## Source Excerpt

```lean
theorem counting_structural :
    (forall g, g ≠ omega -> exists f : Nat -> TauObj,
      Function.Injective f /\ forall x, OrbitRay g x -> exists n, f n = x) /\
    (exists enc : TauObj -> Nat, Function.Injective enc) := by
  constructor
  · intro g hg
    let gcp := generative_counting_principle g hg
    exact ⟨gcp.phi, fun _ _ h => gcp.phi_injective _ _ h,
           fun x hx => gcp.phi_surjective x hx⟩
  · exact tauObj_countable
```
