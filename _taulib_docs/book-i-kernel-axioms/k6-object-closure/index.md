---
{
  "projection_kind": "taulib_declaration",
  "title": "K6_object_closure",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/k6-object-closure/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::K6_object_closure",
  "declaration_slug": "k6-object-closure",
  "kind": "theorem",
  "name": "K6_object_closure",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 128,
  "source_line_end": 135,
  "registry_ids": [
    "I.K6"
  ],
  "related_registry_items": [
    {
      "id": "I.K6",
      "title": "Object Closure (K6)",
      "url": "/registry/object/I.K6/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L128-L135",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/verify/taulib/docs/book-i-kernel-axioms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L128-L135",
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

- Module: [TauLib.BookI.Kernel.Axioms](/verify/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L128-L135)
- Source range: L128-L135
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.K6` — Object Closure (K6)

## Immediate Comment / Docstring

```lean
/-- [I.K6] **Object Closure**: Obj(τ) = {ω} ∪ O_α ∪ O_π ∪ O_γ ∪ O_η.
    No other objects exist.

    In our representation, this is definitional: every `TauObj` is constructed
    from a `Generator` seed, and `Generator` has exactly 5 constructors. -/
```

## Source Excerpt

```lean
theorem K6_object_closure (x : TauObj) :
    x.seed = alpha ∨ x.seed = pi ∨ x.seed = gamma ∨ x.seed = eta ∨ x.seed = omega := by
  cases x.seed with
  | alpha => exact Or.inl rfl
  | pi => exact Or.inr (Or.inl rfl)
  | gamma => exact Or.inr (Or.inr (Or.inl rfl))
  | eta => exact Or.inr (Or.inr (Or.inr (Or.inl rfl)))
  | omega => exact Or.inr (Or.inr (Or.inr (Or.inr rfl)))
```
